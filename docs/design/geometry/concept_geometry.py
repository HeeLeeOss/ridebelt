"""Concept geometry drawings for RideBelt and RAS anchor placement (not CAD).

Generates side_view.png: seat profile, rider hip point (H-point), hip-belt
position, side-anchor zone for the 45-75 deg tether window, and the RAS-3
center-anchor zone. Every dimension is a parameter, to refine with real seat
data and ride manufacturers. Coordinates in mm, origin at the H-point,
x forward, z up.

Run: python concept_geometry.py
"""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Wedge

HERE = Path(__file__).parent

# --- parameters (mm) --------------------------------------------------------
SEAT_PAN_Z = -90            # seat pan surface below the H-point
SEAT_PAN_FRONT_X = 380
SEAT_BACK_X = -130          # seat back surface behind the H-point
BELT_X, BELT_Z = 40, -20    # belt line on the side of the pelvis (low, over the pelvic bones)
TETHER_LEN = (150, 300)     # tether length range (Tether Kit)
ANGLE_WIN = (45, 75)        # deg from horizontal, tether runs down and back (REQ-L7)
CENTER_ZONE_X = (110, 220)  # RAS-3 center anchor: forward of the H-point, between the thighs
CENTER_ZONE_Z = SEAT_PAN_Z


def side_view():
    fig, ax = plt.subplots(figsize=(9, 6.5))
    # seat
    ax.add_patch(Polygon([(SEAT_BACK_X - 60, SEAT_PAN_Z - 60), (SEAT_PAN_FRONT_X, SEAT_PAN_Z - 60),
                          (SEAT_PAN_FRONT_X, SEAT_PAN_Z), (SEAT_BACK_X, SEAT_PAN_Z),
                          (SEAT_BACK_X - 40, 600), (SEAT_BACK_X - 100, 600)],
                         closed=True, fc="#d9d9d9", ec="#555"))
    # rider outline (simplified)
    ax.add_patch(Polygon([(-110, -85), (360, -70), (380, 40), (90, 60), (-20, 520),
                          (-120, 520), (-125, 60)], closed=True, fc="#f3e1c7", ec="#8a6d4b", alpha=0.8))
    ax.add_patch(Circle((-70, 600), 85, fc="#f3e1c7", ec="#8a6d4b", alpha=0.8))
    # H-point
    ax.plot(0, 0, "k+", ms=14, mew=2)
    ax.annotate("H-point (0,0)", (0, 0), (-260, -40), arrowprops=dict(arrowstyle="->"))
    # hip belt
    ax.add_patch(Circle((BELT_X, BELT_Z), 28, fc="#2b6cb0", ec="k", zorder=5))
    ax.annotate("Hip Belt, side\n(low on the pelvis, NOT the waist)", (BELT_X, BELT_Z), (150, 300),
                arrowprops=dict(arrowstyle="->"), color="#2b6cb0")
    # side-anchor zone: tethers run down and BACK from the belt
    w = Wedge((BELT_X, BELT_Z), TETHER_LEN[1], 180 + ANGLE_WIN[0], 180 + ANGLE_WIN[1],
              width=TETHER_LEN[1] - TETHER_LEN[0], fc="#38a169", alpha=0.25, ec="#2f855a")
    ax.add_patch(w)
    for a in ANGLE_WIN:
        r = math.radians(180 + a)
        ax.plot([BELT_X, BELT_X + TETHER_LEN[1] * math.cos(r)],
                [BELT_Z, BELT_Z + TETHER_LEN[1] * math.sin(r)], "--", color="#2f855a")
        ax.text(BELT_X + 0.55 * TETHER_LEN[1] * math.cos(r) - 80, BELT_Z + 0.55 * TETHER_LEN[1] * math.sin(r),
                f"{a}°", color="#2f855a")
    ax.text(-330, -360, "Side RAS anchor zone\n(one each side, on seat structure)\n45–75° down and back",
            color="#2f855a")
    # center anchor zone
    ax.add_patch(Polygon([(CENTER_ZONE_X[0], CENTER_ZONE_Z), (CENTER_ZONE_X[1], CENTER_ZONE_Z),
                          (CENTER_ZONE_X[1], CENTER_ZONE_Z - 25), (CENTER_ZONE_X[0], CENTER_ZONE_Z - 25)],
                         closed=True, fc="#dd6b20", alpha=0.6, ec="#9c4221", zorder=6))
    ax.plot([BELT_X + 60, (CENTER_ZONE_X[0] + CENTER_ZONE_X[1]) / 2], [BELT_Z + 10, CENTER_ZONE_Z],
            color="#dd6b20", lw=2.5, zorder=6)
    ax.annotate("RAS-3 center anchor zone\n(seat pan, between thighs,\nFORWARD of H-point)\n"
                "center strap runs down and forward,\nnever up into the groin",
                ((CENTER_ZONE_X[0] + CENTER_ZONE_X[1]) / 2, CENTER_ZONE_Z - 12), (260, -330),
                arrowprops=dict(arrowstyle="->"), color="#9c4221")
    # keep-out: lap bar zone over thighs
    ax.add_patch(Polygon([(150, 40), (380, 60), (380, 160), (150, 140)], closed=True,
                         fc="none", ec="#c53030", ls=":", lw=1.5))
    ax.text(160, 165, "primary restraint (lap bar)\nkeep-out zone", color="#c53030", fontsize=8)

    ax.set_xlim(-420, 620)
    ax.set_ylim(-450, 720)
    ax.set_aspect("equal")
    ax.grid(alpha=0.2)
    ax.set_xlabel("x (mm, forward)")
    ax.set_ylabel("z (mm, up)")
    ax.set_title("RideBelt / RAS concept geometry: side view (NOT TO DIMENSION, all values TBD)")
    fig.tight_layout()
    fig.savefig(HERE / "side_view.png", dpi=120)


if __name__ == "__main__":
    side_view()
    print("wrote", HERE / "side_view.png")
