# RideBelt Requirements v0.1 (Phase 1)

> 🚧 **DRAFT: not reviewed by a qualified engineer; not for use.** Not released until the MVP review gate. See [SAFETY-NOTICE](../SAFETY-NOTICE.md).


Every requirement is numbered and testable. "TBD" values are set during Phase 1 from measured ride data and must be confirmed by a ride engineer. Test IDs refer to [testing/test-plan.md](testing/test-plan.md).

## Ride load envelope
| ID | Requirement | Verification |
|---|---|---|
| REQ-L1 | The system shall retain a rider through the worst sustained acceleration in the ASTM F2291 envelope for the ride class it is rated for, in every axis (±Gx, ±Gy, +Gz, and −Gz, i.e., ejection) | T-D1, T-D2 |
| REQ-L2 | Minimum breaking strength of every load-path component ≥ 5 × design peak load. **Preliminary design load: 6 kN per tether → MBS ≥ 30 kN.** Basis: 140 kg design rider (160 kg checked), −2.0 g ejection rating, slack ≤ 2 cm, and a **required** per-tether energy absorber capping tension at 4 kN (load-analysis §2a–2b). Confirm against the F2291-26a limits and measured ride data | T-S1, T-S2 |
| REQ-L3 | Peak force transmitted to the rider during arrest shall stay below injury thresholds (pelvis, lumbar, abdomen; plus shoulder and thorax with the Shoulder Module or Integrated Harness). Thresholds TBD from ATD criteria | T-D2 |
| REQ-L6 | Under every rated load case, the Hip Belt shall stay on the pelvis. Belt migration above the pelvic bones onto the abdomen ≤ TBD mm, measured on an ATD | T-D2, T-D3 |
| REQ-L7 | Tether anchor angle shall load the belt down and rearward (TBD 45–75° from horizontal). The RAS anchor position and wrap-strap application guides shall enforce this | T-D3, RAS-CT0 |
| REQ-L8 | Anchor mode (3-Point Tie-Down): the Convertible Center Strap shall run down and forward from the belt buckle and shall not load the groin. Length at the A stop ≤ TBD cm; strength meets REQ-L2. With all three points clipped, belt movement relative to the seat in any direction is ≤ TBD mm | T-D2, T-D5 |
| REQ-L9 | The Convertible Center Strap shall have a single free-end connector, so it cannot be clipped to the seat anchor and the belt rear at once. Length is set only at the two sewn stops (A and W), with no slip between them at rated load. A visible color band shows the mode | T-S2, T-F8 |
| REQ-L4 | Slack (free travel before load is taken up) ≤ 2 cm, achieved with self-retracting, inertia-locking tethers or a cinch. **Total rider excursion** under the rated load case (slack + webbing stretch + body/belt compression + absorber stroke) ≤ 10 cm. The arrest model shows slack is the main driver of peak load (see load-analysis §2a) | T-F1, T-D2 |
| REQ-L5 | Each rider attaches with **two independent tethers** to two anchors, and either one alone meets REQ-L2 | T-S1, analysis |

## Rider fit
| ID | Requirement | Verification |
|---|---|---|
| REQ-F1 | Harness sizes shall cover 5th-percentile female to 99th-percentile male torso and thigh girth (sizes TBD) | T-F2 |
| REQ-F2 | Minimum rider height and mass for the Hip Belt and for each module: TBD. No use below the ride's own minimum | Labeling review |
| REQ-F4 | The Hip Belt shall have a built-in position guide (e.g., contoured shape and a visual marker at the pelvic bones), so the wearer and operator can confirm low positioning in < 5 s | T-F3 |
| REQ-F3 | A fit check (gap gauge or "two-finger" rule) shall be possible in < 10 s | T-F3 |

## Operation
| ID | Requirement | Verification |
|---|---|---|
| REQ-O1 | Clip-in time (rider already wearing the harness) ≤ 15 s; release time by the operator ≤ 10 s per rider | T-F4 |
| REQ-O2 | The rider shall not be able to open an anchor-side connector. RAS latches release only with an operator key or tool. Wrap-strap snap hooks need a deliberate double action to open, and their gates are rated ≥ 16 kN (ANSI Z359.12) | T-S3 |
| REQ-O3 | An operator-only release shall exist (at the RAS anchor, or a tool-operated release on the wrap strap). It must be mechanical or wired, never wireless (see the FTO review) | T-F4 |
| REQ-O7 | **Release under load:** the operator release shall free a tether carrying up to **2.0 kN** (inverted hang ≈ 0.94 kN at 45°, with ≥ 2× margin), using **≤ 150 N** at the key, within ≤ TBD s, and without a sudden drop that injures the rider | T-F9 |
| REQ-O8 | RAS latch: push-to-lock with an audible and visual confirmation, one hand, ≤ 3 s per point. Geometry prevents sideways loading and incomplete latching (a partly inserted tongue cannot hold load without showing "unlatched") | T-S3, T-F4, RAS-CT2 |
| REQ-O4 | Shall not interfere with the ride's restraint closing, locking or sensing. Restraint position sensors read the same with and without RideBelt | T-F5 |
| REQ-O5 | No component shall extend outside the ride's patron clearance envelope during operation | T-F5 |
| REQ-O6 | Shall not slow emergency evacuation beyond the ride's evacuation plan time by more than TBD | T-F6 |

## Hazard controls
| ID | Requirement | Verification |
|---|---|---|
| REQ-H1 | No load-bearing strap shall be able to reach the rider's neck under any rider movement | T-F7 |
| REQ-H2 | All non-load straps have stowage and/or break-away (≤ TBD N) to prevent snagging | T-F7 |
| REQ-H3 | The Wrap Strap's instructions and labeling shall forbid anchoring to the primary restraint itself, unless the RAS application guide for that ride allows it | Label review |
| REQ-H4 | Module requirements by ride class (see the matrix in [design/concepts.md](design/concepts.md)): shoulder protection (the clip-on Shoulder Module **or** the one-piece Integrated Harness) is mandatory on inverting rides; drop towers and seats with dangling legs require shoulder protection plus anti-submarine protection (the Convertible Center Strap in anchor mode on RAS-3 seats, otherwise in wearable mode). Labeling, and the tag check where available (REQ-T3), shall enforce this | Label review, T-E5 |
| REQ-H6 | RideBelt shall not be rated for water rides where the vehicle can capsize, submerge or flood (drowning, H27). Water slides and splash rides with a non-capsizable vehicle need a ride-specific assessment | Label review, ride application guide |
| REQ-H5 | Inverted stop: with the required modules fitted, a rider held upside down for TBD min shall remain retained, with no airway restriction and loads tolerable for that time | T-D4 |

## Durability
| ID | Requirement | Verification |
|---|---|---|
| REQ-D1 | Keep ≥ 80% of rated strength after UV exposure (TBD h), 500 wash cycles and wet/chlorinated water immersion (TBD) | T-E1, T-E2 |
| REQ-D2 | Connectors pass corrosion testing (salt spray, TBD h) | T-E3 |
| REQ-D3 | Service life marked on product (TBD years); retire immediately after any arrest event, and an energy-absorber indicator shows deployment | T-E4, label review |
| REQ-D4 | Unique serial number and an anti-counterfeit mark on every load-bearing component | Inspection |

## Theming & electronics (post-launch; see [business/post-launch.md](business/post-launch.md))
| ID | Requirement | Verification |
|---|---|---|
| REQ-T1 | Themed shells shall attach only at defined zones and shall not cover buckles, connectors, inspection windows, labels or the absorber indicator | T-F5, design review |
| REQ-T2 | Shell elements shall be soft and low-profile, stay out of the neck zone and break away at ≤ TBD N | T-F7 |
| REQ-T3 | Every unit shall carry a sealed passive tag with a cryptographically authenticated, random ID that carries no personal data | T-E5 |
| REQ-T4 | Active modules shall use certified cells (UN 38.3 / IEC 62133), be IP67, be detachable and not be part of the load path | T-E6 |
| REQ-T5 | Active modules shall pass EMC testing and must not affect ride control systems | T-E7 |

## RAS anchor (summary; full detail in [standard/RAS-v0.1.md](standard/RAS-v0.1.md))
| ID | Requirement | Verification |
|---|---|---|
| REQ-A1 | Anchor rated load ≥ 5 × design peak load (REQ-L2) with no permanent deformation at 2× | RAS-CT1 |
| REQ-A2 | Anchors are mounted on the seat structure, in a load path independent of the primary restraint | RAS-CT0 (design review) |
| REQ-A4 | RAS-3 seats have a center anchor placed according to RAS §3.1a–b. It is required on drop-tower and dangling-leg seats | RAS-CT0, RAS-CT5 |
| REQ-A3 | Clipped-in sensor output with a defined interface. Optional in RAS v0.1, but **strongly recommended for use in dispatch logic**: the incident review found that restraints which were never locked or checked (mode R2) are as common as mechanical failures, and an unchecked optional belt doesn't fix that | RAS-CT4 |
