import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import compressor_model as cm
import Fluid_CP as FCP

_DT_SH    = 4.0   
_DT_SC    = 4.0  
_DT_PINCH = 1.0   # approach temp [K]
_EH       = "CBar"
_MIN_PR   = 2.0  


def get_ac_performance(T_room: float, T_ambient: float,
                       refrigerant: str, bore_mm: float):
  
    T_ev = T_room    - _DT_PINCH - _DT_SH   # e.g. 15 - 1 - 4 = 10 °C
    T_co = T_ambient + _DT_PINCH + _DT_SC   # e.g. 35 + 1 + 4 = 40 °C

    # ── Pressure-ratio floor ─────────────────────────────────────────────
    p_ev = FCP.state(["T", "x"], [T_ev, 1], refrigerant, _EH)["p"]
    p_co = FCP.state(["T", "x"], [T_co, 0], refrigerant, _EH)["p"]

    if p_co / p_ev < _MIN_PR:
        target = _MIN_PR * p_ev
        lo, hi = T_co, T_co + 50.0
        for _ in range(60):
            mid = (lo + hi) / 2.0
            if FCP.state(["T", "x"], [mid, 0], refrigerant, _EH)["p"] < target:
                lo = mid
            else:
                hi = mid
        T_co = hi

    param = [T_ev, T_co, _DT_SH, _DT_SC, bore_mm]
    eta_is, m_dot = cm.recip_comp_corr_SP(param, refrigerant)

    s1    = FCP.state(["T", "x"], [T_ev, 1],                    refrigerant, _EH)
    s1_sh = FCP.state(["T", "p"], [T_ev + _DT_SH, s1["p"]],    refrigerant, _EH)
    s3    = FCP.state(["T", "x"], [T_co, 0],                    refrigerant, _EH)
    s3_sc = FCP.state(["p", "T"], [s3["p"], s3["T"] - _DT_SC],  refrigerant, _EH)
    s2_is = FCP.state(["p", "s"], [s3["p"], s1_sh["s"]],        refrigerant, _EH)

    h2    = s1_sh["h"] + (s2_is["h"] - s1_sh["h"]) / eta_is
    s4    = FCP.state(["h", "p"], [s3_sc["h"], s1["p"]],        refrigerant, _EH)

    q_cool = s1_sh["h"] - s4["h"]    # kJ/kg
    w_sp   = h2 - s1_sh["h"]         # kJ/kg

    COP_inner = q_cool / w_sp
    Q_AC_kW   = m_dot * q_cool       # kW

    return COP_inner, Q_AC_kW
