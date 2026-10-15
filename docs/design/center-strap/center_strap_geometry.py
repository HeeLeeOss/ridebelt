"""DRAFT Convertible Center Strap lengths and drawing (task ridebelt-design-004). Not for use: see SAFETY-NOTICE.md.

Derives the wearable-mode (W) stop ladder for each Hip Belt size from ANSUR II crotch length
(crotchlengthomphalion), using a linear fit on fit girth (buttock circumference + 4 cm clothing),
and draws a dimensioned straight layout of the size M strap.

Inputs: ANSUR_II_MALE_Public.csv, ANSUR_II_FEMALE_Public.csv in <data_dir> (see
docs/research/anthropometry/compute_percentiles.py for URLs). Requires numpy and pandas.
Run: python center_strap_geometry.py <data_dir>
"""
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
SIZES = [("XS", 82, 102), ("S", 98, 118), ("M", 114, 134), ("L", 130, 150), ("XL", 146, 166)]
CLOTHING_CM = 4.0       # same allowance as docs/design/sizing.md (SZ-A1)
BELT_LINE_DEDUCT = 12.0  # CS-A2: belt front and rear sit about 6 cm below omphalion level each (ASSUMPTION)
W_STEP = 3.0             # CS-A4: spacing of sewn W stops (cm)
A_STOPS = (10.0, 13.0, 16.0)  # CS-A1: A-mode deployed strap lengths (cm), three sewn stops
Z = 2.326                # one-sided z for P1/P99


def w_ladders(data_dir):
    d = pd.concat([pd.read_csv(Path(data_dir) / f, encoding="latin-1")
                   for f in ("ANSUR_II_MALE_Public.csv", "ANSUR_II_FEMALE_Public.csv")])
    g = d.buttockcircumference.values / 10 + CLOTHING_CM
    c = d.crotchlengthomphalion.values / 10
    b, a = np.polyfit(g, c, 1)
    sd = float(np.std(c - (a + b * g)))
    rows = []
    for name, lo, hi in SIZES:
        need_lo = a + b * lo - Z * sd - BELT_LINE_DEDUCT
        need_hi = a + b * hi + Z * sd - BELT_LINE_DEDUCT
        first = math.floor(need_lo / W_STEP) * W_STEP
        last = math.ceil(need_hi / W_STEP) * W_STEP
        n = int(round((last - first) / W_STEP)) + 1
        rows.append(dict(size=name, lo=need_lo, hi=need_hi, first=first, last=last, n=n))
    return (a, b, sd, len(g)), rows


def table(fit, rows):
    a, b, sd, n = fit
    out = [f"Fit (ANSUR II, n = {n}): crotch length omphalion ≈ {a:.1f} + {b:.3f} × fit girth (cm); residual SD {sd:.2f} cm.", "",
           "| Belt size | Required W length, P1–P99 (cm) | W stop ladder (cm) | Number of W stops (every 3 cm) |",
           "|---|---|---|---|"]
    for r in rows:
        out.append(f"| {r['size']} | {r['lo']:.1f}–{r['hi']:.1f} | {r['first']:.0f}–{r['last']:.0f} | {r['n']} |")
    return "\n".join(out)


def svg(rM):
    k = 9.0  # px per cm
    W, H = 1250, 470
    x0, y = 60, 190
    stow = 6.0                         # fixed end + fold allowance before the first stop
    a_lo, a_hi = A_STOPS[0], A_STOPS[-1]
    w_lo, w_hi = rM["first"], rM["last"]
    total = w_hi + stow + 8             # tongue at the free end (8 cm incl. tongue body)
    L = lambda cm: x0 + cm * k
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="13">',
         '<defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z"/></marker></defs>',
         '<rect width="100%" height="100%" fill="#ffffff"/>',
         '<text x="20" y="28" font-size="17" font-weight="bold">Convertible Center Strap, size M: straight layout (DRAFT, NOT FOR USE, NOT FOR MANUFACTURE)</text>',
         f'<text x="20" y="48" fill="#555">Lengths measured from the slider stop to the tongue tip = deployed length. Scale {k:.0f} px = 1 cm. Values DRAFT; see center-strap-spec.md.</text>']
    # strap body
    o.append(f'<rect x="{L(0):.1f}" y="{y:.1f}" width="{total*k:.1f}" height="30" fill="#e2e8f0" stroke="#2d3748" stroke-width="2"/>')
    # fixed end at buckle
    o.append(f'<rect x="{L(0)-16:.1f}" y="{y-10:.1f}" width="16" height="50" fill="#a0aec0" stroke="#1a202c"/>')
    o.append(f'<text x="{L(0)-40:.1f}" y="{y+70:.1f}">fixed end, sewn at front buckle</text>')
    # The deployed length is measured from the stop to the tongue tip, so stops are placed from the tongue end.
    tip = L(total)
    def stop_x(dep):  # x position of a stop giving deployed length dep
        return tip - dep * k
    # A ladder (green)
    for dep in A_STOPS:
        x = stop_x(dep)
        o.append(f'<rect x="{x-3:.1f}" y="{y-4:.1f}" width="6" height="38" fill="#38a169"/>')
    o.append(f'<text x="{stop_x(a_hi)-10:.1f}" y="{y-16:.1f}" fill="#276749">A stops {A_STOPS[0]:.0f}/{A_STOPS[1]:.0f}/{A_STOPS[2]:.0f} cm (green band)</text>')
    # W ladder (blue)
    dep = w_lo
    while dep <= w_hi + 1e-6:
        x = stop_x(dep)
        o.append(f'<rect x="{x-3:.1f}" y="{y-4:.1f}" width="6" height="38" fill="#3182ce"/>')
        dep += W_STEP
    o.append(f'<text x="{stop_x(w_hi):.1f}" y="{y-16:.1f}" fill="#2b6cb0">W stops {w_lo:.0f}–{w_hi:.0f} cm, every {W_STEP:.0f} cm (blue band)</text>')
    # pad sleeve on the deployed part near mid-W length
    pad_c = (w_lo + w_hi) / 2 * 0.55
    o.append(f'<rect x="{stop_x(pad_c + 12):.1f}" y="{y-8:.1f}" width="{24*k:.1f}" height="46" rx="8" fill="#fbd38d" fill-opacity="0.6" stroke="#975a16"/>')
    o.append(f'<text x="{stop_x(pad_c + 12)-60:.1f}" y="{y+92:.1f}" fill="#975a16">captive padded sleeve, 24 cm (crotch crossing, W mode)</text>')
    # tongue
    o.append(f'<rect x="{tip-8*k:.1f}" y="{y-2:.1f}" width="{8*k:.1f}" height="34" fill="#4a5568" stroke="#1a202c"/>')
    o.append(f'<text x="{tip-110:.1f}" y="{y+70:.1f}">RAS tongue (single free-end connector)</text>')
    # dimensions
    def dim(x1, x2, yy, lab):
        o.append(f'<line x1="{x1:.1f}" y1="{yy:.1f}" x2="{x2:.1f}" y2="{yy:.1f}" stroke="#000" marker-start="url(#a)" marker-end="url(#a)"/>')
        o.append(f'<text x="{(x1+x2)/2-90:.1f}" y="{yy-6:.1f}">{lab}</text>')
    dim(stop_x(a_lo), tip, y + 110, f"A deployed {A_STOPS[0]:.0f}–{A_STOPS[-1]:.0f} cm")
    dim(stop_x(w_lo), tip, y + 150, f"shortest W deployed {w_lo:.0f} cm")
    dim(stop_x(w_hi), tip, y + 190, f"longest W deployed {w_hi:.0f} cm")
    dim(L(0), tip, y + 230, f"overall strap ≈ {total:.0f} cm")
    o.append('<text x="20" y="455" fill="#c53030">One connector only: the strap can be latched to the seat anchor OR to the belt rear receiver, never both (REQ-L9).</text>')
    o.append("</svg>")
    return "\n".join(o)


if __name__ == "__main__":
    fit, rows = w_ladders(sys.argv[1] if len(sys.argv) > 1 else ".")
    (HERE / "center_strap_layout_M.svg").write_text(svg(rows[2]), encoding="utf-8")
    print(table(fit, rows))
