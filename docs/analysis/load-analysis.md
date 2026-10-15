# Load Analysis Plan v0.1 (Phase 5)

> 🚧 **DRAFT: not reviewed by a qualified engineer; not for use.** Not released until the MVP review gate. See [SAFETY-NOTICE](../../SAFETY-NOTICE.md).


## 1. Design peak load, first-order estimate (to refine)
Static case: rider mass m, peak ejection-direction acceleration a (in g).

    F_static = m × a × g

Worked example, for illustration only. Replace with real ride data.
- m = 136 kg (300 lb rider plus clothing; original placeholder, since replaced by the **160 kg** design mass, see §2b)
- a = 2 g in the ejection direction (placeholder; get the ride-specific −Gz or lateral peak from F2291 envelopes or measured accelerometer data)
- F_static ≈ 136 × 2 × 9.81 ≈ **2.7 kN**, shared between two tethers

Dynamic factor: if the primary restraint fails suddenly, the rider moves through the free travel (≤ 10 cm, REQ-L4) before the tethers load up. The peak force depends on tether stiffness and energy absorption. Model the rider as a mass on a spring and damper, starting with a relative velocity of v = √(2 × a × g × free travel).

- With a = 2 g and 0.10 m of free travel: v ≈ 2.0 m/s.
- Pick tether stiffness and absorber deployment so peak force ≤ 1.5 × F_static (target, TBD).

Design peak load (TBD) = F_static × dynamic factor. Breaking strength ≥ 5 × that (REQ-L2). With these placeholders, that comes to about **20 kN per tether**, close to common carabiner ratings of 22–25 kN. This suggests the target is achievable with off-the-shelf connector technology.

## 2. Analyses to perform
| ID | Analysis | Tool |
|---|---|---|
| A1 | Load cases for each ride class (coaster, drop tower, pendulum, swing) from F2291 envelopes and published or measured accelerometer traces | Spreadsheet / Python |
| A2 | Spring-damper arrest model: peak force vs. free travel, stiffness and absorber threshold | Python (scipy) |
| A3 | Multibody rider simulation with restraint failure, comparing Hip Belt alone vs. each module combination (waist belt as the control): pelvic, lumbar and abdominal loads, belt migration, submarining, excursion. Includes a tether-angle sweep to set REQ-L7 | MADYMO / LS-DYNA with ATD models (outsource) |
| A4 | FEA of the RAS anchor and its mounting bracket | Any FEA package |
| A5 | Wrap-strap friction and slip on round and square members | Test-driven, with a hand calculation (capstan equation) |

## 2a. A2 results: arrest model v0.1 (first run 2026-10-14; re-run at 160 kg 2026-10-15)
Script: [arrest_model.py](arrest_model.py). Full sweep: `arrest_results.csv`; plot: `arrest_sweep.png`. All figures below are for the **160 kg** design rider (task `ridebelt-requirements-003`; the first run used a 136 kg placeholder).

**Model:** 1-DOF, 160 kg rider (whole-body mass, conservative); half-sine ejection pulse (−Gz) of amplitude A and duration T_p; two side tethers at angle θ; webbing about 8% elongation at 11 kN; body and belt compliance k_b = 100 kN/m and damping 1.5 kN·s/m (**assumptions to replace with ATD data**); optional energy absorber with a force cap.

**Findings**
| Finding | Evidence | Design consequence |
|---|---|---|
| **Slack is the dominant variable.** Dynamic factor ≈ 1.0–1.4 with zero slack; ≈ 1.3–3.2 with 5–10 cm | Main sweep | Make slack as small as possible. **Promote the self-retracting, inertia-locking tether** from open question to the preferred design; tighten REQ-L4's goal to ≤ 2 cm |
| Peak tension per tether ≤ **5.6 kN** across all swept cases (A ≤ 2.5 g, slack ≤ 10 cm, θ = 60°, k_b 100 kN/m); ≤ 3.1 kN with zero slack | Main sweep | Preliminary **design load 6 kN per tether → MBS ≥ 30 kN** (5:1) |
| **Tether angle:** tension rises steeply below 45° (5.6 kN at 30° vs 3.4 kN at 60°, 2 g case), and excursion barely changes | Angle sweep | Keep the REQ-L7 window at **45–75°**, with a 60–75° target |
| Excursion is dominated by **body/belt compliance**, not webbing stretch: about 3–4 cm at zero slack, 11 cm or more at 5 cm slack | Excursion column; k_b sensitivity | REQ-L4 should limit **total excursion** (slack + stretch + body compression), not just slack. Measure k_b in ATD tests (T-D2); belt padding stiffness is a design lever |
| Stiffer body/belt coupling plus slack → **higher** peak force (at 136 kg in the first run: k_b 400 kN/m with 5 cm slack gave 4.4 kN vs 2.95 kN at 100 kN/m; see §2b for the 160 kg stiff-body cases) | k_b sensitivity | Don't over-stiffen the belt; padding helps |
| A **4 kN** absorber only acts in the worst cases (2.5 g, short pulse, 10 cm slack), capping tension at 4 kN with about 6 cm of stroke | Main sweep | Fit an absorber at **about 4 kN per tether** as a load cap. It makes the design load independent of the ride's exact acceleration profile |
| **Inverted hang** (−1 Gz, static): 1.11 kN per tether at 45°, 0.91 kN at 60° | Inverted-hang table | Release-under-load rating **2 kN** (REQ-O7) gives about 1.8× margin at 45° (2.2× at 60°) |
| Peak force on the rider's pelvis is ≤ about 9.7 kN in the worst case, with no absorber and 10 cm slack | Main sweep | **Needs ATD validation** (T-D2). It's in the range of car lap-belt loads, but pelvic and abdominal tolerance under this load direction is unverified |

### 2b. Check against researched design cases (2026-10-14)
Inputs: design rider mass **160 kg**, about the US civilian 99th percentile (NHANES P99: 155.8 kg men and 146.6 kg women in 2021–2023; 159.2 kg and 155.9 kg in 2017–2020; see [research/anthropometry-adult.md](../research/anthropometry-adult.md)). It replaces the earlier 140 kg value, which was only the 95th percentile of the heaviest US male age band. Load cases from [research/ride-acceleration-data.md](../research/ride-acceleration-data.md): proposed first rating **−2.0 g ejection** (pulse from 0.3 s up to 3 s), plus −1.0 g sustained (inverted stop). The F2291 −Gz limits themselves are in the paid standard and still unverified.

| Case (−2.0 g, 60° tethers) | Peak tension per tether |
|---|---|
| 160 kg, slack ≤ 2 cm, 0.3 s, k_b 100 kN/m | 3.1 kN |
| 160 kg, slack ≤ 2 cm, worst (0.3 s, stiff body k_b 400 kN/m) | 3.96 kN |
| 160 kg, **10 cm slack**, 0.3 s, stiff body, **no absorber** | **7.7 kN** (exceeds the 6 kN design load) |
| 160 kg, 10 cm slack, with a **4 kN absorber** | 4.0 kN (absorber stroke 6 cm; excursion 18 cm, which fails REQ-L4) |

**Conclusion (unchanged by the 160 kg design mass):** the **6 kN design load / 30 kN MBS holds**, provided slack is ≤ 2 cm (REQ-L4) **and** a 4 kN absorber is fitted as a backstop against misuse. Both are now required. Long or sustained pulses (≥ 1 s) behave like static loading (dynamic factor ≈ 1), so short pulses with slack are the governing case. Pendulum rides repeat the −Gz load on every swing, so add a **fatigue load case** (cycles TBD) for tethers, absorbers and anchors (RAS-CT3). Drop-tower braking (about +5 g into the seat) governs the **center strap's anti-submarine function**, not tether strength. Check it in T-D2.

**Limits of this model:** 1-DOF only (no rotation or jackknifing, no lateral or longitudinal loads, no submarining); assumed body compliance; pulse shapes are idealized. A3 (multibody/ATD simulation) and T-D2 (sled tests) replace it.

## 3. Outputs feeding other documents
- Final numbers for REQ-L2, REQ-L3 and REQ-L4 → `requirements.md`
- RAS rated load → `standard/RAS-v0.1.md` §4
- Absorber deployment threshold → `design/concepts.md`
