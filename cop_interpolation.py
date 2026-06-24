import os, sys, pickle
import numpy as np
from scipy.interpolate import RegularGridInterpolator, NearestNDInterpolator

_DT_SH    = 4.0
_DT_SC    = 4.0
_DT_PINCH = 1.0

_TABLES = None   # loaded once on first call, then cached

def _load_tables():
    global _TABLES
    if _TABLES is not None:
        return
    pkl = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ac_lookup_tables.pkl")
    with open(pkl, "rb") as f:
        raw = pickle.load(f)
    _TABLES = {}
    for ref, bore_dict in raw.items():
        _TABLES[ref] = {}
        for bore, tbl in bore_dict.items():
            _TABLES[ref][bore] = _attach_interpolators(tbl)


def _attach_interpolators(tbl: dict) -> dict:
    T_room_grid = tbl["T_room_grid"]
    T_amb_grid  = tbl["T_amb_grid"]
    TT, TA = np.meshgrid(T_room_grid, T_amb_grid, indexing="ij")

    out = dict(tbl)
    for key, ikey in (("COP_inner", "_cop_interp"), ("Q_Ac", "_q_interp")):
        grid = tbl[key].copy()
        mask_nan = np.isnan(grid)
        if mask_nan.any():
            valid = ~mask_nan
            nn  = NearestNDInterpolator(
                np.column_stack([TT[valid].ravel(), TA[valid].ravel()]),
                grid[valid].ravel(),
            )
            pts = np.column_stack([TT[mask_nan].ravel(), TA[mask_nan].ravel()])
            grid[mask_nan] = nn(pts)
        out[ikey] = RegularGridInterpolator(
            (T_room_grid, T_amb_grid), grid,
            method="bicubic", bounds_error=False, fill_value=None,
        )
    return out


def get_ac_performance(T_room: float, T_ambient: float,
                       refrigerant: str, bore_mm: float):
   
    _load_tables()

    T_ev = T_room    - _DT_PINCH - _DT_SH
    T_co = T_ambient + _DT_PINCH + _DT_SC
    if T_ev >= T_co - 2.0:
        return 1.0, 0.001

    try:
        tbl = _TABLES[refrigerant][bore_mm]
    except KeyError:
        raise KeyError(
            f"No table for refrigerant={refrigerant!r}, bore={bore_mm} mm. "
            f"Available: { {r: list(b.keys()) for r,b in _TABLES.items()} }"
        )

    pt  = np.array([[T_room, T_ambient]])
    cop = float(tbl["_cop_interp"](pt)[0])
    q   = float(tbl["_q_interp"](pt)[0])

    if np.isnan(cop) or np.isnan(q) or q <= 0:
        return 1.0, 0.001

    return cop, q