# Test Plan v0.1 (Phase 6)

> 🚧 **DRAFT: not reviewed by a qualified engineer; not for use.** Not released until the MVP review gate. See [SAFETY-NOTICE](../../SAFETY-NOTICE.md).


## Review gates (mandatory; see [GOVERNANCE.md](../../GOVERNANCE.md))
- **Drafting stage (now):** research, analysis, design and bench testing on rigs with dummies may go ahead without credentialed sign-off. All outputs stay **DRAFT** (rework risk, not injury risk). Optional early review of the hazard analysis is encouraged, because it reduces rework.
- **MVP gate (mandatory):** before **any person wears a prototype** (even static) or any content is marked RELEASED, an independent credentialed safety or ride engineer reviews, in one pass: `safety/`, `requirements.md`, `analysis/`, the RAS draft, the latch design, and the bench and dynamic test results (T-S*, T-D1–T-D3 with ATD). Human wear on a moving ride is then allowed only on a manufacturer-approved test track.
- **Certification gate:** third-party certification (e.g., TÜV SÜD, Intertek or SGS) before any sale or park pilot.

## Bench tests (static and component)
| ID | Test | Method reference | Pass |
|---|---|---|---|
| T-S1 | Static strength of the full harness, tether and connector system | EN 361 / EN 12277 style static | ≥ REQ-L2 load held for 3 min |
| T-S2 | Buckle and adjuster slip | EN 361 style | Slip ≤ TBD mm at TBD kN |
| T-S3 | Connector gate and cross-load | EN 362 / ANSI Z359.12 | Gate stays closed; meets major-axis rating |
| T-S4 | Tether abrasion over an edge | EN 795 style edge test | Retains ≥ 80% of strength |
| T-S5 | Wrap-strap slip on members of minimum and maximum diameter (round and square) | Custom | No slip at rated load |

## Dynamic tests
| ID | Test | Method | Pass |
|---|---|---|---|
| T-D1 | Drop-rig retention, with a torso dummy in a representative seat with the primary restraint removed | Custom drop rig, ejection pulse for each ride class | Dummy retained; excursion ≤ TBD |
| T-D2 | Sled test with an instrumented ATD (THOR preferred, for abdomen and submarining measurement). Matrix: Hip Belt alone, + center strap (anchor mode), + Shoulder, + Shoulder + anchor mode, + Shoulder + wearable mode, **Integrated Harness** (alone, + anchor mode, + wearable mode), each ride-class pulse. Compare the Integrated Harness with the clip-on Shoulder Module to confirm equal retention. **Head-to-head comparison: anchor mode vs. wearable mode on the drop-tower pulse.** Also test the misuse case: anchor mode clipped at the W length. **Control case:** a waist-position belt, to confirm why it is ruled out | Accredited crash lab | Injury criteria under REQ-L3; belt migration within REQ-L6. The results set the final ride rating matrix |
| T-D3 | Tether angle sweep (e.g., 30–90° from horizontal) with belt migration measured | Sled or drop rig | Defines the REQ-L7 angle window |
| T-D5 | 3-Point geometry: sweep the center-anchor position and tether length; measure groin and pelvic load and belt movement relative to the seat | Sled or drop rig with ATD | Meets REQ-L8; sets the RAS-3 center-anchor envelope |
| T-D4 | Inverted hang with the required modules, ATD first, then instrumented human volunteers under ethics approval, only after Gate 2 | Static inversion rig | REQ-H5 met; no airway restriction |

## Fit and operation
| ID | Test | Pass |
|---|---|---|
| T-F1 | Free travel measurement | ≤ 10 cm |
| T-F2 | Anthropometric fit trials (n ≥ TBD, covering the size range) | All sizes fit |
| T-F3 | Fit-check and belt-position check time; untrained users put the belt on at the correct low position (n ≥ TBD) | < 10 s; ≥ TBD% correct without help |
| T-F4 | Clip-in and operator release time | ≤ 15 s / ≤ 10 s |
| T-F5 | Restraint lock and sensor readings with and without RideBelt; clearance-envelope fixture | No difference; no intrusion |
| T-F6 | Timed evacuation drill | Within the REQ-O6 limit |
| T-F8 | Center-strap mode change: untrained users switch between A and W modes; operators identify the mode from the platform. Confirm the strap cannot be clipped in both modes at once | Mode change ≤ TBD s; ≥ TBD% correct; operators identify the mode correctly 100% of the time |
| T-F9 | Rescue release under load: weighted dummy hanging inverted on its tethers; operators release it using the RAS release and the wrap-strap rescue procedure | Meets REQ-O7 force, time and no-drop limits |
| T-F7 | Entanglement and neck-reach study (range of motion, snag probe) | No strap reaches the neck; break-aways release ≤ TBD N |

## Environmental and durability
| ID | Test | Pass |
|---|---|---|
| T-E1 | UV aging, then static strength | ≥ 80% retained |
| T-E2 | Wash and chlorinated-water cycles, then static strength | ≥ 80% retained |
| T-E3 | Salt spray on connectors | No function loss |
| T-E4 | Absorber deployment indicator | Visible after any deployment |
| T-E5 | Tag survival and read reliability after wash, UV and impact; clone-resistance check | ≥ TBD% read rate; cloned tags rejected |
| T-E6 | Plus module battery, ingress (IP67) and drop or impact | No leak, fire or detachment |
| T-E7 | EMC emissions and immunity of the Plus module | Pass; no effect on ride controls in a bench test with the manufacturer |

## Traceability (requirement → test)
| Requirement | Tests |
|---|---|
| REQ-L1 | T-D1, T-D2 |
| REQ-L2 | T-S1, T-S2 |
| REQ-L3 | T-D2 |
| REQ-L4 | T-F1 |
| REQ-L5 | T-S1 |
| REQ-L6 | T-D2, T-D3 |
| REQ-L7 | T-D3, RAS-CT0 |
| REQ-L8 | T-D2, T-D5 |
| REQ-L9 | T-S2, T-F8 |
| REQ-A4 | RAS-CT0, RAS-CT5 |
| REQ-F1 | T-F2 |
| REQ-F3, REQ-F4 | T-F3 |
| REQ-H5 | T-D4 |
| REQ-O1, REQ-O3 | T-F4 |
| REQ-O7 | T-F9, RAS-CT6 |
| REQ-O8 | T-S3, T-F4, RAS-CT2, RAS-CT7 |
| REQ-O2 | T-S3 |
| REQ-O4, REQ-O5 | T-F5 |
| REQ-O6 | T-F6 |
| REQ-H1, REQ-H2 | T-F7 |
| REQ-D1 | T-E1, T-E2 |
| REQ-D2 | T-E3 |
| REQ-D3 | T-E4 |
| REQ-A1 to REQ-A3 | RAS-CT0 to RAS-CT5 |
| REQ-T1 | T-F5 |
| REQ-T2 | T-F7 |
| REQ-T3 | T-E5 |
| REQ-T4 | T-E6 |
| REQ-T5 | T-E7 |
| REQ-F2, REQ-H3, REQ-H4, REQ-D4 | Labeling and inspection review |
| REQ-H6 | Labeling review and the ride application guide (capsizable water rides excluded) |
