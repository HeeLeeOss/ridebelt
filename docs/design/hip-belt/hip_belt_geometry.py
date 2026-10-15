"""DRAFT Hip Belt geometry and drawing generator (task ridebelt-design-001). Not for use: see SAFETY-NOTICE.md.

Derives per-size layout dimensions from the size chart in docs/design/sizing.md and writes:
  - hip_belt_layout_M.svg : dimensioned flat-layout drawing (size M) plus a side-view tether-angle sketch
  - prints a markdown table of per-size dimensions

Pure standard library. Run: python hip_belt_geometry.py
All parameters are DRAFT values; each one is listed with its source/assumption ID in hip-belt-spec.md.
"""
from pathlib import Path

HERE = Path(__file__).parent

# Size chart (fit girth over clothing, cm) from docs/design/sizing.md
SIZES = [("XS", 82, 102), ("S", 98, 118), ("M", 114, 134), ("L", 130, 150), ("XL", 146, 166)]

PAD_WIDTH_MM = 100        # HB-A1: load-spreading pad width at sides and rear
WEB_WIDTH_MM = 50         # HB-A2: load webbing width (polyester, materials-webbing.md)
PAD_THICK_MM = 12         # HB-A3: total pad thickness (≤ 15 mm, for lap-bar clearance, REQ-O4)
PAD_EXTENSION_CM = 10     # HB-A4: pad extends this far past each side ring toward the front
TETHER_WINDOW = (45, 75)  # REQ-L7 window, degrees below horizontal, down and rearward


def size_dims(name, gmin, gmax):
    gmid = (gmin + gmax) / 2
    ring_from_rear = gmid / 4              # side rings on the lateral midline at mid-size girth
    pad_len = gmid / 2 + 2 * PAD_EXTENSION_CM  # rear + sides, fixed length
    front_min = gmin - pad_len             # adjustable front section (two adjusters + buckle)
    front_max = gmax - pad_len
    ring_shift = (gmax - gmin) / 8         # how far the ring moves off the true lateral line at size limits
    return dict(size=name, gmin=gmin, gmax=gmax, gmid=gmid, ring=ring_from_rear, pad=pad_len,
                fmin=front_min, fmax=front_max, shift=ring_shift)


def table():
    rows = ["| Size | Fit girth (cm) | Fixed padded section, rear + sides (cm) | Side ring from rear centre, each side (cm) "
            "| Adjustable front section (cm) | Ring offset from true side at size limits (± cm) |",
            "|---|---|---|---|---|---|"]
    for s in map(lambda x: size_dims(*x), SIZES):
        rows.append(f"| {s['size']} | {s['gmin']}–{s['gmax']} | {s['pad']:.0f} | {s['ring']:.1f} | "
                    f"{s['fmin']:.0f}–{s['fmax']:.0f} | {s['shift']:.1f} |")
    return "\n".join(rows)


def svg_layout(s):
    """Flat layout of size M, unrolled from rear centre (x = 0) to both front ends, plus side-view angle sketch."""
    k = 6.0                                   # px per cm
    W, H = 1250, 640
    cx, y0 = W / 2, 150                       # rear centre at middle top
    padw = PAD_WIDTH_MM / 10 * k
    webw = WEB_WIDTH_MM / 10 * k
    half_pad = s["pad"] / 2 * k
    half_front_mid = (s["gmid"] - s["pad"]) / 4 * k  # each side of the front section, at mid adjustment
    ring = s["ring"] * k
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="13">',
           '<rect width="100%" height="100%" fill="#ffffff"/>',
           f'<text x="20" y="28" font-size="17" font-weight="bold">RideBelt Hip Belt, size {s["size"]}: flat layout (DRAFT, NOT FOR USE, NOT FOR MANUFACTURE)</text>',
           f'<text x="20" y="48" fill="#555">Unrolled from rear centre; drawn at mid-adjustment (fit girth {s["gmid"]:.0f} cm). Scale {k:.0f} px = 1 cm. All values DRAFT; see hip-belt-spec.md.</text>']
    # pad (rear + sides)
    out.append(f'<rect x="{cx-half_pad:.1f}" y="{y0:.1f}" width="{2*half_pad:.1f}" height="{padw:.1f}" rx="10" fill="#cfe0f5" stroke="#2b6cb0" stroke-width="2"/>')
    # load webbing through the whole loop
    wy = y0 + (padw - webw) / 2
    left_end = cx - half_pad - half_front_mid
    right_end = cx + half_pad + half_front_mid
    out.append(f'<rect x="{left_end:.1f}" y="{wy:.1f}" width="{right_end-left_end:.1f}" height="{webw:.1f}" fill="none" stroke="#1a202c" stroke-width="2" stroke-dasharray="6 3"/>')
    # front buckle halves at the two ends (they join when the belt is closed)
    for x, lab in ((left_end, "buckle (male)"), (right_end, "buckle (female)")):
        out.append(f'<rect x="{x-12:.1f}" y="{wy-8:.1f}" width="24" height="{webw+16:.1f}" fill="#a0aec0" stroke="#1a202c"/>')
        out.append(f'<text x="{x-40:.1f}" y="{wy+webw+40:.1f}">{lab}</text>')
    # adjusters (one each front side)
    for x in (cx - half_pad - half_front_mid / 2, cx + half_pad + half_front_mid / 2):
        out.append(f'<rect x="{x-10:.1f}" y="{wy-6:.1f}" width="20" height="{webw+12:.1f}" fill="#fbd38d" stroke="#975a16"/>')
        out.append(f'<text x="{x-58:.1f}" y="{y0-48:.1f}" fill="#975a16">adjuster + range window</text>')
    # side rings and tether exits
    for x, side in ((cx - ring, "L"), (cx + ring, "R")):
        out.append(f'<circle cx="{x:.1f}" cy="{y0+padw:.1f}" r="11" fill="#38a169" stroke="#1c4532" stroke-width="2"/>')
        out.append(f'<text x="{x-60:.1f}" y="{y0+padw+32:.1f}" fill="#1c4532">side ring {side} (tether, sewn)</text>')
        # position marker at pelvic-bone line, just forward of the ring
        mx = x - 0.08 * s["gmid"] * k if side == "L" else x + 0.08 * s["gmid"] * k
        out.append(f'<polygon points="{mx:.1f},{y0-4:.1f} {mx-8:.1f},{y0-18:.1f} {mx+8:.1f},{y0-18:.1f}" fill="#e53e3e"/>')
        out.append(f'<text x="{mx-52:.1f}" y="{y0-24:.1f}" fill="#c53030">position marker (REQ-F4)</text>')
    # rear centre receiver (centre strap W mode)
    out.append(f'<rect x="{cx-14:.1f}" y="{y0+padw-6:.1f}" width="28" height="22" fill="#dd6b20" stroke="#7b341e"/>')
    out.append(f'<text x="{cx-70:.1f}" y="{y0+padw+52:.1f}" fill="#7b341e">rear receiver (centre strap, W mode)</text>')
    # dimension lines
    def dim(x1, x2, y, label):
        out.append(f'<line x1="{x1:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y:.1f}" stroke="#000" marker-start="url(#a)" marker-end="url(#a)"/>')
        out.append(f'<text x="{(x1+x2)/2-60:.1f}" y="{y-6:.1f}">{label}</text>')
    out.insert(1, '<defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z"/></marker></defs>')
    dim(cx - half_pad, cx + half_pad, y0 + padw + 95, f"fixed padded section {s['pad']:.0f} cm (rear + sides)")
    dim(cx - ring, cx, y0 + padw + 130, f"{s['ring']:.1f} cm")
    dim(cx, cx + ring, y0 + padw + 130, f"{s['ring']:.1f} cm")
    dim(left_end, right_end, y0 + padw + 165, f"total loop {s['gmin']}–{s['gmax']} cm (adjustable)")
    # vertical dimension: pad width
    xv = right_end + 45
    out.append(f'<line x1="{xv:.1f}" y1="{y0:.1f}" x2="{xv:.1f}" y2="{y0+padw:.1f}" stroke="#000" marker-start="url(#a)" marker-end="url(#a)"/>')
    out.append(f'<text x="{xv+6:.1f}" y="{y0+padw/2+4:.1f}">pad width {PAD_WIDTH_MM} mm</text>')
    out.append(f'<text x="{xv+6:.1f}" y="{y0+padw/2+22:.1f}">webbing {WEB_WIDTH_MM} mm · thickness ≤ {PAD_THICK_MM} mm</text>')
    # side-view tether window sketch
    sx, sy = 170, 540
    out.append(f'<text x="{sx-150:.1f}" y="{sy-70:.1f}" font-weight="bold">Side view at side ring: tether direction window (REQ-L7)</text>')
    out.append(f'<circle cx="{sx}" cy="{sy-40}" r="10" fill="#38a169"/>')
    import math
    for a in TETHER_WINDOW:
        r = math.radians(a)
        x2, y2 = sx - 120 * math.cos(r), sy - 40 + 120 * math.sin(r)
        out.append(f'<line x1="{sx}" y1="{sy-40}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#2f855a" stroke-width="2" stroke-dasharray="5 3"/>')
        out.append(f'<text x="{x2-34:.1f}" y="{y2+14:.1f}" fill="#2f855a">{a}°</text>')
    out.append(f'<line x1="{sx-150}" y1="{sy-40}" x2="{sx+80}" y2="{sy-40}" stroke="#999"/>')
    out.append(f'<text x="{sx+20}" y="{sy-46}" fill="#555">horizontal (forward →)</text>')
    out.append(f'<text x="{sx+120}" y="{sy+10}" fill="#555">Tether leaves the ring down and rearward, 45–75° below horizontal.</text>')
    out.append('</svg>')
    return "\n".join(out)


if __name__ == "__main__":
    m = size_dims(*SIZES[2])
    (HERE / "hip_belt_layout_M.svg").write_text(svg_layout(m), encoding="utf-8")
    print(table())
