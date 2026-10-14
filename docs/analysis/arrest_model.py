"""RideBelt arrest model (analysis A2 in load-analysis.md).

One-degree-of-freedom model of a rider whose primary restraint has failed and
who is pushed out of the seat by a net ejection acceleration (-Gz). The rider is
held by two side tethers through a hip belt.

    rider mass m --(body/belt compliance k_b)--(2 tethers at angle theta, slack s,
                                                 energy absorber F_ea / stroke L_ea)-- seat

Simplifications (all flagged in load-analysis.md):
  * The whole-body mass moves with the pelvis (conservative).
  * Motion is vertical only. Each tether sits at angle theta from horizontal, so
    vertical force = 2 * T * sin(theta).
  * The seat can only push the rider up, never pull them down, so the rider
    rests on the seat until the ejection acceleration exceeds 0.
  * Tethers carry tension only. The absorber is rigid-plastic at F_ea up to
    stroke L_ea, then bottoms out.
  * Ejection pulse is a half-sine of amplitude A (g) and duration T_p. The
    restraint has already failed at t=0, which is worst case: the rider starts
    at rest with the full slack s available.

Run:  python arrest_model.py         -> prints tables, writes arrest_results.csv
                                         and arrest_sweep.png next to this file
"""
from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np

G = 9.81
HERE = Path(__file__).parent


@dataclass
class Params:
    m: float = 140.0          # kg, design rider mass (95th pct US male, heaviest age band; ride-acceleration-data.md)
    A: float = 2.0            # g, peak net ejection acceleration (-Gz)
    T_p: float = 0.5          # s, pulse duration
    slack: float = 0.05       # m, free travel before the tethers take load
    theta_deg: float = 60.0   # tether angle from horizontal
    L_t: float = 0.25         # m, tether length
    # Webbing stiffness: about 8% elongation at 11 kN (seat-belt-class polyester).
    k_t: float = 11000 / (0.08 * 0.25)  # N/m axial, per tether
    k_b: float = 100e3        # N/m vertical, body/belt compliance (ASSUMPTION)
    c_b: float = 1500.0       # N*s/m, body damping (ASSUMPTION)
    F_ea: float = math.inf    # N, absorber deployment force per tether (inf = none)
    L_ea: float = 0.10        # m, absorber stroke
    t_end: float = 1.5
    dt: float = 2e-5


def simulate(p: Params) -> dict:
    s = math.sin(math.radians(p.theta_deg))
    # Vertical stiffness of the tether pair, including geometry
    k_tv = 2 * p.k_t * s * s
    k = 1 / (1 / k_tv + 1 / p.k_b)  # tether pair and body in series

    x = v = 0.0            # rider vertical position (up = +) and velocity
    plastic = 0.0          # absorber deployment, measured vertically
    peak_F = peak_x = 0.0
    n = int(p.t_end / p.dt)
    for i in range(n):
        t = i * p.dt
        # Net ejection acceleration (-Gz): half-sine pulse, then back to normal seating (+1 Gz, pressed into the seat)
        a_ej = p.A * G * math.sin(math.pi * t / p.T_p) if t < p.T_p else -G
        stretch = x - p.slack - plastic
        F = 0.0
        if stretch > 0:
            F = k * stretch + (p.c_b * v if v > 0 else 0.0)
            # Absorber: per-tether tension = F / (2 s)
            T = F / (2 * s)
            if T > p.F_ea and plastic < p.L_ea * s:
                # Absorber yields: hold the force at its threshold and move the plastic offset
                F = p.F_ea * 2 * s
                plastic = x - p.slack - F / k
                plastic = min(plastic, p.L_ea * s)
        acc = a_ej - F / p.m
        if x <= 0 and acc < 0:  # seat stops the rider (no penetration)
            acc, v, x = 0.0, max(v, 0.0), 0.0
        v += acc * p.dt
        x += v * p.dt
        peak_F = max(peak_F, F)
        peak_x = max(peak_x, x)
    return {
        "peak_rider_force_kN": peak_F / 1e3,
        "peak_tether_tension_kN": peak_F / (2 * s) / 1e3,
        "static_tether_tension_kN": p.m * p.A * G / (2 * s) / 1e3,
        "dynamic_factor": peak_F / (p.m * p.A * G) if p.A > 0 else 0.0,
        "max_excursion_cm": peak_x * 100,
        "absorber_used_cm": plastic / s * 100,
    }


def sweep() -> list[dict]:
    rows = []
    for A in (1.0, 1.5, 2.0, 2.5):
        for T_p in (0.3, 1.0):
            for slack in (0.0, 0.05, 0.10):
                for F_ea in (math.inf, 4000.0):
                    p = Params(A=A, T_p=T_p, slack=slack, F_ea=F_ea)
                    r = simulate(p)
                    rows.append({"A_g": A, "T_p_s": T_p, "slack_cm": slack * 100,
                                 "absorber_kN": "none" if F_ea == math.inf else F_ea / 1e3,
                                 **{k: round(v, 2) for k, v in r.items()}})
    return rows


def angle_sweep() -> list[dict]:
    rows = []
    for th in (30, 45, 60, 75, 90):
        r = simulate(Params(theta_deg=th, A=2.0, T_p=0.5, slack=0.05))
        rows.append({"theta_deg": th, **{k: round(v, 2) for k, v in r.items()}})
    return rows


def inverted_hang(m: float = 140.0) -> list[dict]:
    """Static tether tension for a rider hanging inverted (-1 Gz), per tether."""
    return [{"theta_deg": th, "tension_per_tether_N": round(m * G / (2 * math.sin(math.radians(th))))}
            for th in (30, 45, 60, 75, 90)]


def md(rows: list[dict]) -> str:
    keys = list(rows[0])
    out = ["| " + " | ".join(keys) + " |", "|" + "---|" * len(keys)]
    out += ["| " + " | ".join(str(r[k]) for k in keys) + " |" for r in rows]
    return "\n".join(out)


if __name__ == "__main__":
    rows = sweep()
    with open(HERE / "arrest_results.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print("## Main sweep (theta = 60 deg, m = 140 kg)\n")
    print(md(rows))
    print("\n## Tether angle sweep (A = 2 g, T_p = 0.5 s, slack = 5 cm)\n")
    print(md(angle_sweep()))
    print("\n## Inverted hang, static (m = 140 kg)\n")
    print(md(inverted_hang()))

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(7, 4))
        for slack in (0.0, 0.05, 0.10):
            As = np.linspace(0.5, 3.0, 11)
            peaks = [simulate(Params(A=a, T_p=0.5, slack=slack))["peak_tether_tension_kN"] for a in As]
            ax.plot(As, peaks, marker="o", label=f"slack {slack*100:.0f} cm, no absorber")
        peaks = [simulate(Params(A=a, T_p=0.5, slack=0.10, F_ea=4000))["peak_tether_tension_kN"]
                 for a in np.linspace(0.5, 3.0, 11)]
        ax.plot(np.linspace(0.5, 3.0, 11), peaks, "k--", label="slack 10 cm, 4 kN absorber")
        ax.set_xlabel("Peak ejection acceleration, -Gz (g)")
        ax.set_ylabel("Peak tension per tether (kN)")
        ax.set_title("RideBelt arrest model: 140 kg rider, 60° tethers, 0.5 s pulse")
        ax.grid(alpha=0.3)
        ax.legend()
        fig.tight_layout()
        fig.savefig(HERE / "arrest_sweep.png", dpi=120)
    except Exception as e:  # plotting is optional
        print("plot skipped:", e)
