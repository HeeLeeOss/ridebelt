"""Reproduce the adult anthropometry percentiles in docs/research/anthropometry-adult.md.

Inputs (download into a folder and pass it as the first argument):
  ANSUR II (US Army 2012 survey, public release):
    https://tools.openlab.psu.edu/publicData/ANSUR_II_MALE_Public.csv
    https://tools.openlab.psu.edu/publicData/ANSUR_II_FEMALE_Public.csv
  NHANES (CDC/NCHS, public domain):
    2021-2023:     https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.xpt
                   https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt
    2017-Mar 2020: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/P_BMX.xpt
                   https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/P_DEMO.xpt

Usage: python compute_percentiles.py <data_dir>    (requires pandas, numpy)
Prints markdown tables.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

PCTS = [1, 5, 50, 95, 99]


def weighted_percentiles(values, weights, pcts):
    """Percentiles of a weighted sample (linear interpolation of the weighted CDF midpoints)."""
    v = np.asarray(values, float)
    w = np.asarray(weights, float)
    m = ~(np.isnan(v) | np.isnan(w)) & (w > 0)
    v, w = v[m], w[m]
    order = np.argsort(v)
    v, w = v[order], w[order]
    cdf = (np.cumsum(w) - 0.5 * w) / w.sum()
    return np.interp(np.array(pcts) / 100, cdf, v), int(m.sum())


def md_table(title, rows, unit_note):
    out = [f"#### {title}", "", unit_note, "",
           "| Variable | Sex | n | " + " | ".join(f"P{p}" for p in PCTS) + " |",
           "|---|---|---|" + "---|" * len(PCTS)]
    out += rows
    return "\n".join(out) + "\n"


def ansur(data_dir: Path):
    variables = {  # ANSUR II variable -> label
        "waistcircumference": "Waist circumference",
        "buttockcircumference": "Hip (buttock) circumference",
        "hipbreadthsitting": "Hip breadth, sitting",
        "thighcircumference": "Thigh circumference (proximal)",
        "sittingheight": "Sitting height",
        "waistbacklength": "Waist back length (C7 to waist, back)",
        "waistfrontlengthsitting": "Waist front length, sitting (suprasternale to waist)",
        "crotchlengthomphalion": "Crotch length, omphalion (front waist via crotch to back waist)",
        "biacromialbreadth": "Biacromial (shoulder) breadth",
        "weightkg": "Body mass",
    }
    rows = []
    for var, label in variables.items():
        for sex, fname in (("M", "ANSUR_II_MALE_Public.csv"), ("F", "ANSUR_II_FEMALE_Public.csv")):
            d = pd.read_csv(data_dir / fname, encoding="latin-1")
            x = d[var].astype(float)
            if var == "weightkg":
                x = x / 10.0  # stored in hectograms
                fmt = "{:.1f}"
            else:
                fmt = "{:.0f}"
            p = np.percentile(x.dropna(), PCTS)
            rows.append(f"| {label} (`{var}`) | {sex} | {x.notna().sum()} | " + " | ".join(fmt.format(v) for v in p) + " |")
    return md_table("ANSUR II (US Army, 2012), unweighted", rows, "Units: mm; body mass in kg.")


def nhanes(data_dir: Path, bmx, demo, wt, label):
    b = pd.read_sas(data_dir / bmx, format="xport")
    d = pd.read_sas(data_dir / demo, format="xport")
    df = b.merge(d[["SEQN", "RIAGENDR", "RIDAGEYR", wt]], on="SEQN")
    df = df[df["RIDAGEYR"] >= 18]
    variables = {"BMXWAIST": ("Waist circumference", "{:.1f}"), "BMXHIP": ("Hip circumference", "{:.1f}"),
                 "BMXWT": ("Body mass", "{:.1f}"), "BMXHT": ("Stature", "{:.1f}")}
    rows = []
    for var, (name, fmt) in variables.items():
        for sex, code in (("M", 1), ("F", 2)):
            s = df[df["RIAGENDR"] == code]
            p, n = weighted_percentiles(s[var], s[wt], PCTS)
            rows.append(f"| {name} (`{var}`) | {sex} | {n} | " + " | ".join(fmt.format(v) for v in p) + " |")
    return md_table(f"NHANES {label}, adults 18+, survey-weighted (`{wt}`)", rows,
                    "Units: cm; body mass in kg.")


if __name__ == "__main__":
    data = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    print(ansur(data))
    print(nhanes(data, "BMX_L.xpt", "DEMO_L.xpt", "WTMEC2YR", "2021-2023"))
    print(nhanes(data, "P_BMX.xpt", "P_DEMO.xpt", "WTMECPRP", "2017-March 2020 (pre-pandemic)"))
