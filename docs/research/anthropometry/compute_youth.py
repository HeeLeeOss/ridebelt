"""Reproduce the youth (ages 6-17) anthropometry tables in docs/research/anthropometry-youth.md.

Inputs (CDC/NCHS NHANES, public domain), downloaded into <data_dir>:
  2021-2023:     https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.xpt
                 https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt
  2017-Mar 2020: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/P_BMX.xpt
                 https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/P_DEMO.xpt

Usage: python compute_youth.py <data_dir>     (requires pandas, numpy)
Prints markdown tables. Percentiles use the MEC exam weights.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from compute_percentiles import weighted_percentiles

PCTS = [5, 50, 95]
IN = 2.54
THRESHOLDS_IN = [42, 48, 54]  # common ride height limits (inches)
BANDS = [("< 42 in (< 106.7 cm)", 0, 42), ("42–47.9 in (106.7–121.9 cm)", 42, 48),
         ("48–53.9 in (121.9–137.2 cm)", 48, 54), ("≥ 54 in (≥ 137.2 cm)", 54, 99)]
VARS = {"BMXHT": ("Stature, cm", "{:.1f}"), "BMXWT": ("Body mass, kg", "{:.1f}"),
        "BMXWAIST": ("Waist circumference, cm", "{:.1f}"), "BMXHIP": ("Hip circumference, cm (ages 12+ only)", "{:.1f}"),
        "BMXLEG": ("Upper leg length, cm (ages 8+ only)", "{:.1f}")}


def load(data_dir, bmx, demo, wt):
    b = pd.read_sas(data_dir / bmx, format="xport")
    d = pd.read_sas(data_dir / demo, format="xport")
    df = b.merge(d[["SEQN", "RIAGENDR", "RIDAGEYR", wt]], on="SEQN").rename(columns={wt: "W"})
    return df[(df.RIDAGEYR >= 6) & (df.RIDAGEYR <= 17)]


def pct_row(s, var, fmt):
    if s[var].notna().sum() < 30:
        return ["n<30"] * len(PCTS), int(s[var].notna().sum())
    p, n = weighted_percentiles(s[var], s["W"], PCTS)
    return [fmt.format(v) for v in p], n


def by_age(df, label):
    out = [f"### By age group and sex — NHANES {label}", "",
           "| Measure | Age | Sex | n | P5 | P50 | P95 |", "|---|---|---|---|---|---|---|"]
    for var, (name, fmt) in VARS.items():
        for lo, hi in ((6, 8), (9, 11), (12, 14), (15, 17)):
            for sex, code in (("M", 1), ("F", 2)):
                s = df[(df.RIDAGEYR >= lo) & (df.RIDAGEYR <= hi) & (df.RIAGENDR == code)]
                vals, n = pct_row(s, var, fmt)
                if n == 0:
                    continue
                out.append(f"| {name} | {lo}–{hi} | {sex} | {n} | " + " | ".join(vals) + " |")
    return "\n".join(out) + "\n"


def by_band(df, label):
    out = [f"### By ride height band (ages 6–17, both sexes) — NHANES {label}", "",
           "| Height band | Measure | n | P5 | P50 | P95 |", "|---|---|---|---|---|---|"]
    for band, lo, hi in BANDS:
        s = df[(df.BMXHT >= lo * IN) & (df.BMXHT < hi * IN)]
        for var in ("RIDAGEYR", "BMXWT", "BMXWAIST", "BMXHIP"):
            name, fmt = ("Age, years", "{:.0f}") if var == "RIDAGEYR" else VARS[var]
            vals, n = pct_row(s, var, fmt)
            out.append(f"| {band} | {name} | {n} | " + " | ".join(vals) + " |")
    return "\n".join(out) + "\n"


def share_reaching(df, label):
    out = [f"### Share of children reaching each height limit, by age — NHANES {label}", "",
           "Weighted percentage of children at each age whose measured stature is at or above the limit.", "",
           "| Age | n | ≥ 42 in | ≥ 48 in | ≥ 54 in |", "|---|---|---|---|---|"]
    for age in range(6, 18):
        s = df[(df.RIDAGEYR == age) & df.BMXHT.notna() & (df.W > 0)]
        cells = []
        for t in THRESHOLDS_IN:
            share = (s.W * (s.BMXHT >= t * IN)).sum() / s.W.sum() * 100
            cells.append(f"{share:.0f}%")
        out.append(f"| {age} | {len(s)} | " + " | ".join(cells) + " |")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    data = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    cur = load(data, "BMX_L.xpt", "DEMO_L.xpt", "WTMEC2YR")
    old = load(data, "P_BMX.xpt", "P_DEMO.xpt", "WTMECPRP")
    print(share_reaching(cur, "2021–2023"))
    print(by_band(cur, "2021–2023"))
    print(by_band(old, "2017–March 2020 (cross-check)"))
    print(by_age(cur, "2021–2023"))
