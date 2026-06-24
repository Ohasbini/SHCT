import os, sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FixedLocator
from CoolProp.HumidAirProp import HAPropsSI

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from control_strategy import Controller


AC_PERFORMANCE = {
    "Propane":  {30: (3.99, 4.0345), 40: (3.99, 7.17245), 50: (3.99, 11.20695)},
    "R1234yf":  {30: (3.83, 2.84624), 40: (3.83, 5.05999), 50: (3.83, 7.90623)},
    "DME":      {30: (4.07, 2.82896), 40: (4.07, 5.02926), 50: (4.07, 7.85822)},
}


# ── Room / air properties ────────────────────────────────────────────────
Room_Vol = 10.0 * 6.0 * 3.0     # m³
Rho_air  = 1.225                 # kg/m³
cp_air   = 1.005                 # kJ/(kg·K)
Air_Mass = Rho_air * Room_Vol    # ≈ 220.5 kg
P_atm    = 101325.0              # Pa

Dt            = 150              # s, simulation timestep
M_dot         = Air_Mass / Dt    # kg/s
W_Ventilation = 0.090            # kW, ventilation fan power
i             = int(24 * 3600 / Dt)   # timesteps per day (576)
tau           = Air_Mass / M_dot      # s, ventilation time constant

T_initial  = 15.0                # °C, initial room temperature
Rh_initial = 0.60                # initial relative humidity
Rh_Outdoor = 0.60                # outdoor relative humidity

File_directory = os.path.dirname(os.path.abspath(__file__))
Refrigerants   = ["Propane", "R1234yf", "DME"]
Comp_Sizes     = [30, 40, 50]
Seasons = {
    "spring": "ambient temperature spring",
    "summer": "ambient temperature summer",
    "fall":   "ambient temperature fall",
    "winter": "ambient temperature winter",
}


# ── I/O helpers ──────────────────────────────────────────────────────────
def load(filename: str) -> np.ndarray:
    path = os.path.join(File_directory, filename)
    with open(path) as f:
        vals = [float(line.strip().rstrip(',')) for line in f if line.strip()]
    return np.array(vals)


def interpolate(data: np.ndarray) -> np.ndarray:
    raw       = np.linspace(0, 1, len(data))
    processed = np.linspace(0, 1, i)
    return np.interp(processed, raw, data)


# ── Humidity helpers ──────────────────────────────────────────────────────
def w_from_rh(T_C: float, RH: float) -> float:
    return HAPropsSI("W", "T", T_C + 273.15, "P", P_atm, "R", RH)

def rh_from_w(T_C: float, w: float) -> float:
    return HAPropsSI("R", "T", T_C + 273.15, "P", P_atm, "W", max(w, 0.0))

def dew_point_from_w(T_C: float, w: float) -> float:
    return HAPropsSI("D", "T", T_C + 273.15, "P", P_atm, "W", max(w, 0.0)) - 273.15

def w_sat(T_C: float) -> float:
    return HAPropsSI("W", "T", T_C + 273.15, "P", P_atm, "R", 1.0)


# ── One-day simulation ────────────────────────────────────────────────────
def day_simulation(T_amb: np.ndarray, Q_server: np.ndarray, refrigerant: str,
                   cylinder_size: float, T_init: float = T_initial) -> dict:

    COP_inner, Q_Ac = AC_PERFORMANCE[refrigerant][cylinder_size]
    
    T_amb    = interpolate(T_amb)
    Q_server = interpolate(Q_server)

    T_room = np.empty(i);  T_room[0] = T_init
    w_room = np.empty(i);  w_room[0] = w_from_rh(T_init, Rh_initial)
    mode   = np.empty(i, dtype=int)
    Q_cool = np.zeros(i)
    W_comp = np.zeros(i)
    W_vent = np.zeros(i)
    ac_plr = np.zeros(i)

    controller = Controller(Dt, M_dot, cp_air)

    for k in range(i - 1):
        mode[k] = controller.step(T_room[k], T_amb[k], Q_server[k])

        if mode[k] == 0:                                        # ── off ──
            T_room[k + 1] = T_room[k] + Q_server[k] * Dt / (Air_Mass * cp_air)
            w_room[k + 1] = w_room[k]

        elif mode[k] == 1:                                      # ── ventilation ──
            T_ss = T_amb[k] + Q_server[k] / (M_dot * cp_air)
            T_room[k + 1] = T_ss + (T_room[k] - T_ss) * np.exp(-Dt / tau)

            Q_cool[k] = Air_Mass * cp_air * (T_room[k + 1] - T_room[k]) / Dt - Q_server[k]
            W_vent[k] = W_Ventilation

            w_outdoor     = w_from_rh(T_amb[k], Rh_Outdoor)
            w_room[k + 1] = w_room[k] + (w_outdoor - w_room[k]) * (1.0 - np.exp(-Dt / tau))

        elif mode[k] == 2:                                      # ── AC on/off ──
            # Part-load ratio for COP_res correction (task sheet formula)
            x       = min(Q_server[k] / Q_Ac, 1.0)
            COP_res = COP_inner * x / (0.1 + 0.9 * x) if x > 0 else COP_inner

            Q_cool[k] = -Q_Ac                  
            W_comp[k] = Q_Ac / COP_res         
            W_vent[k] = W_Ventilation
            ac_plr[k] = x

            dT = (Q_cool[k] + Q_server[k]) * Dt / (Air_Mass * cp_air)
            T_room[k + 1] = T_room[k] + dT    

            T_ev  = T_room[k] - 5.0
            T_dew = dew_point_from_w(T_room[k], w_room[k])
            dw = (M_dot * (w_sat(T_ev) - w_room[k]) * Dt / Air_Mass) if T_ev < T_dew else 0.0
            w_room[k + 1] = w_room[k] + dw

    RH_room = np.array([rh_from_w(T_room[k], w_room[k]) for k in range(i)])
    for arr in (Q_cool, W_comp, W_vent, ac_plr):
        arr[-1] = arr[-2]
    mode[-1] = mode[-2]

    return {
        "t":        np.linspace(0, 24, i, endpoint=False),
        "T_room":   T_room,
        "T_amb":    T_amb,
        "mode":     mode,
        "Q_server": Q_server,
        "Q_cool":   Q_cool,
        "W_comp":   W_comp,
        "W_vent":   W_vent,
        "ac_plr":   ac_plr,
        "w_room":   w_room * 1e3,      # g/kg
        "RH_room":  RH_room * 100.0,   # %
    }


# ── Metrics ───────────────────────────────────────────────────────────────
def metrics(results: dict) -> dict:
    mode = results["mode"]
    ac_starts  = int(np.sum((mode[1:] == 2) & (mode[:-1] != 2)))
    dt_h       = 24.0 / i
    E_comp_kWh = np.sum(results["W_comp"]) * dt_h
    E_vent_kWh = np.sum(results["W_vent"]) * dt_h
    return {
        "E_comp_kWh":  E_comp_kWh,
        "E_vent_kWh":  E_vent_kWh,
        "E_total_kWh": E_comp_kWh + E_vent_kWh,
        "ac_starts":   ac_starts,
        "frac_off":    float(np.mean(mode == 0)) * 100,
        "frac_vent":   float(np.mean(mode == 1)) * 100,
        "frac_ac":     float(np.mean(mode == 2)) * 100,
        "T_max":       float(np.max(results["T_room"])),
        "T_min":       float(np.min(results["T_room"])),
    }


# ── Plotting ──────────────────────────────────────────────────────────────
def plot_day(result: dict, title: str) -> plt.Figure:
    t      = result["t"]
    mode   = result["mode"]
    ac_plr = result["ac_plr"]

    fig, axes = plt.subplots(4, 1, figsize=(11, 12), sharex=True)
    fig.suptitle(title, fontsize=13)

    # Panel 1: temperatures
    ax = axes[0]
    ax.plot(t, result["T_room"], "b-",  lw=1.4, label="T_room")
    ax.plot(t, result["T_amb"],  "g--", lw=1.0, label="T_ambient")
    ax.axhline(15, color="r",      ls=":", lw=0.8, label="T_ON = 15 °C")
    ax.axhline(13, color="orange", ls=":", lw=0.8, label="T_OFF = 13 °C")
    ax.set_ylabel("Temperature [°C]")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, lw=0.3)

    # Panel 2: mode bands — AC height shows Q_server/Q_Ac ratio
   # Panel 2: mode bands
    ax = axes[1]
    ax.fill_between(t, 0.0, 1.0,
                where=(mode == 1), step="post",
                alpha=0.5, color="green", label="Ventilation")
    ax.fill_between(t, 1.15, 2.15,
                where=(mode == 2), step="post",
                alpha=0.6, color="red", label="AC")
    ax.set_yticks([0.5, 1.65])
    ax.set_yticklabels(["Vent.", "AC"])
    ax.set_ylim(-0.1, 2.4)
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, lw=0.3, axis="x")
    # Panel 3: power flows
    ax = axes[2]
    ax.plot(t, result["Q_server"],             "r-",  lw=1.2, label="Q_server [kW]")
    ax.plot(t, -result["Q_cool"],              "b-",  lw=1.2, label="Q_cooling [kW]")
    ax.plot(t, result["W_comp"],               "k--", lw=0.9, label="W_comp [kW]")
    ax.plot(t, result["W_vent"] * (mode > 0),  "m:",  lw=0.9, label="W_vent [kW]")
    ax.set_ylabel("Power [kW]")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, lw=0.3)

    # Panel 4: humidity
    ax  = axes[3]
    ax2 = ax.twinx()
    ax.plot(t,  result["w_room"],  "b-",  lw=1.2, label="Abs. humidity [g/kg]")
    ax2.plot(t, result["RH_room"], "g--", lw=1.0, label="RH [%]")
    ax.set_xlabel("Time [h]")
    ax.set_ylabel("Absolute humidity [g/kg]")
    ax2.set_ylabel("Relative humidity [%]")
    ax.legend(fontsize=8, loc="upper left")
    ax2.legend(fontsize=8, loc="upper right")
    ax.grid(True, lw=0.3)

    # X axis: major every 2 h, minor at every timestep
    step_edges = np.linspace(0, 24, i + 1)
    for a in axes:
        a.set_xlim(0, 24)
        a.xaxis.set_major_locator(MultipleLocator(2))
        a.xaxis.set_minor_locator(FixedLocator(step_edges))
        a.tick_params(axis="x", which="major", length=6)
        a.tick_params(axis="x", which="minor", length=2.5, color="0.5")

    plt.tight_layout()
    return fig


# ── Driver ────────────────────────────────────────────────────────────────
def run_all(refrigerant: str, bore_mm: float):
    Q_server = load("server heating power")
    results  = {}

    print(f"\nSimulating: {refrigerant}, D = {bore_mm} mm")
    for season, fname in Seasons.items():
        print(f"  {season:7s}...", end="  ", flush=True)
        T_amb = load(fname)
        results[season] = day_simulation(T_amb, Q_server, refrigerant, bore_mm)
        m = metrics(results[season])
        print(f"E_total = {m['E_total_kWh']:7.3f} kWh | AC starts = {m['ac_starts']:3d} | "
              f"off/vent/ac = {m['frac_off']:4.0f}/{m['frac_vent']:4.0f}/{m['frac_ac']:4.0f}% | "
              f"T_max = {m['T_max']:5.2f} °C")

        fig = plot_day(results[season], f"{season.capitalize()} — {refrigerant}, D={bore_mm} mm")
        fname_out = f"plot_{season}_{refrigerant}_{bore_mm}mm.png"
        fig.savefig(os.path.join(File_directory, fname_out), dpi=150, bbox_inches="tight")
        plt.close(fig)

    return results


if __name__ == "__main__":
    # run_all("R1234yf", 30)
    # run_all("R1234yf", 40)
    # run_all("R1234yf", 50)
    # run_all("DME", 30)
    # run_all("DME", 40)
    # run_all("DME", 50)
    run_all("Propane", 30)
    run_all("Propane", 40)
    run_all("Propane", 50)