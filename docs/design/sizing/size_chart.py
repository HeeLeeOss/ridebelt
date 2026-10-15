"""DRAFT size-chart coverage calculator for the Hip Belt and Integrated Harness (task ridebelt-sizing-001).

Not for use: see SAFETY-NOTICE.md. Computes, for a proposed size chart, the share of US adults whose
fit dimension falls inside each size's adjustment range.

Inputs (same files as docs/research/anthropometry/compute_percentiles.py), in <data_dir>:
  NHANES 2021-2023 BMX_L.xpt + DEMO_L.xpt (survey-weighted, adults 18+)
  ANSUR II ANSUR_II_MALE_Public.csv + ANSUR_II_FEMALE_Public.csv (unweighted)

Usage: python size_chart.py <data_dir>     (requires pandas, numpy)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "research" / "anthropometry"))
from compute_percentiles import weighted_percentiles  # noqa: E402

# ---- design parameters (all ASSUMPTIONS for engineer review) ----
CLOTHING_ALLOWANCE_CM = 4.0   # belt worn over clothing; added to measured hip circumference
BELT_SIZES = [               # (name, min girth cm, max girth cm): 20 cm adjustment, 4 cm overlap
    ("XS", 82, 102), ("S", 98, 118), ("M", 114, 134), ("L", 130, 150), ("XL", 146, 166)]
SHOULDER_ARC_CM = 10.0        # strap path over the top of the shoulder, added to front + back torso lengths
HARNESS_STRAP_RANGE = (76, 116)  # cm, shoulder-strap path length range: front + back adjusters of 20 cm each


def nhanes_adults(data_dir):
    b = pd.read_sas(data_dir / "BMX_L.xpt", format="xport")
    d = pd.read_sas(data_dir / "DEMO_L.xpt", format="xport")
    df = b.merge(d[["SEQN", "RIAGENDR", "RIDAGEYR", "WTMEC2YR"]], on="SEQN")
    df = df[(df.RIDAGEYR >= 18) & df.BMXHIP.notna() & (df.WTMEC2YR > 0)].copy()
    df["girth"] = df.BMXHIP + CLOTHING_ALLOWANCE_CM
    return df


def belt_table(df):
    w = df.WTMEC2YR
    rows = ["| Size | Adjustment range (cm, over clothing) | Fits (all adults) | Fits (men) | Fits (women) |",
            "|---|---|---|---|---|"]
    for name, lo, hi in BELT_SIZES:
        cells = []
        for mask in (np.ones(len(df), bool), (df.RIAGENDR == 1).values, (df.RIAGENDR == 2).values):
            s, ws = df[mask], w[mask]
            cells.append(f"{(ws * ((s.girth >= lo) & (s.girth <= hi))).sum() / ws.sum() * 100:.1f}%")
        rows.append(f"| {name} | {lo}–{hi} | " + " | ".join(cells) + " |")
    lo_all, hi_all = BELT_SIZES[0][1], BELT_SIZES[-1][2]
    tot = []
    for mask in (np.ones(len(df), bool), (df.RIAGENDR == 1).values, (df.RIAGENDR == 2).values):
        s, ws = df[mask], w[mask]
        inside = (ws * ((s.girth >= lo_all) & (s.girth <= hi_all))).sum() / ws.sum() * 100
        below = (ws * (s.girth < lo_all)).sum() / ws.sum() * 100
        above = (ws * (s.girth > hi_all)).sum() / ws.sum() * 100
        tot.append((inside, below, above))
    rows.append("| **All sizes** | {}–{} | {:.1f}% | {:.1f}% | {:.1f}% |".format(lo_all, hi_all, *[t[0] for t in tot]))
    rows.append("| Below smallest | < {} | {:.1f}% | {:.1f}% | {:.1f}% |".format(lo_all, *[t[1] for t in tot]))
    rows.append("| Above largest | > {} | {:.1f}% | {:.1f}% | {:.1f}% |".format(hi_all, *[t[2] for t in tot]))
    p, n = weighted_percentiles(df.girth, w, [1, 5, 50, 95, 99])
    note = (f"Fit girth = NHANES hip circumference + {CLOTHING_ALLOWANCE_CM:.0f} cm clothing allowance; n = {n}; "
            f"weighted P1/P5/P50/P95/P99 = " + " / ".join(f"{v:.1f}" for v in p) + " cm. "
            "Sizes overlap, so a rider near a boundary fits two sizes and the per-size shares sum to more than the total.")
    return "\n".join(rows) + "\n\n" + note + "\n"


def harness_table(data_dir):
    rows = ["| Sex | n | P1 | P5 | P50 | P95 | P99 | Inside strap range |", "|---|---|---|---|---|---|---|---|"]
    lo, hi = HARNESS_STRAP_RANGE
    for sex, f in (("M", "ANSUR_II_MALE_Public.csv"), ("F", "ANSUR_II_FEMALE_Public.csv")):
        d = pd.read_csv(data_dir / f, encoding="latin-1")
        path = (d.waistfrontlengthsitting + d.waistbacklength) / 10 + SHOULDER_ARC_CM
        p = np.percentile(path, [1, 5, 50, 95, 99])
        inside = ((path >= lo) & (path <= hi)).mean() * 100
        rows.append(f"| {sex} | {len(path)} | " + " | ".join(f"{v:.1f}" for v in p) + f" | {inside:.1f}% |")
    return ("\n".join(rows) + f"\n\nStrap path = waist front length (sitting) + waist back length + {SHOULDER_ARC_CM:.0f} cm "
            f"shoulder arc (ANSUR II, cm). Strap adjustment range {lo}–{hi} cm. ANSUR II is a military sample, so upper "
            "percentiles are lower bounds for civilians.\n")


if __name__ == "__main__":
    data = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    print("### Hip Belt: coverage by size (NHANES 2021–2023, adults 18+, survey-weighted)\n")
    print(belt_table(nhanes_adults(data)))
    print("### Integrated Harness: shoulder-strap path length (ANSUR II)\n")
    print(harness_table(data))
