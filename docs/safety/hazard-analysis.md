# Hazard Analysis v0.1 (Phase 2, ISO 12100 method)

> 🚧 **DRAFT: not reviewed by a qualified engineer; not for use.** Not released until the MVP review gate. See [SAFETY-NOTICE](../../SAFETY-NOTICE.md).


**Scope:** hazards RideBelt is meant to reduce **and** hazards RideBelt itself creates. A backup restraint that adds more risk than it removes must not ship.

Severity (S): 1 minor, 2 moderate, 3 serious, 4 fatal. Likelihood (L): 1 remote to 4 frequent. Risk = S × L. Risk ≥ 8 needs a design mitigation, not just a warning label.

| ID | Hazard | Cause | S | L (pre) | Mitigation | L (post) | Req / Test |
|---|---|---|---|---|---|---|---|
| H1 | Rider ejected despite RideBelt | Anchored to the failed restraint | 4 | 3 | Wrap-strap rules, RAS anchors on structure, labeling, training | 1 | REQ-H3, REQ-A2 |
| H2 | Abdominal or spinal injury during arrest | Belt worn at the waist, or migrates onto the abdomen | 4 | 3 | Low hip-belt design, position guide, downward tether angle, crotch strap on drop towers, energy absorber | 1 | REQ-L3, REQ-L6, REQ-L7, REQ-F4 |
| H3 | Rider strikes the structure while partly ejected | Tether too long | 4 | 2 | ≤ 10 cm free travel, short adjustable tethers | 1 | REQ-L4 |
| H4 | Strangulation or entanglement | Strap reaches the neck, or snags on moving parts | 4 | 2 | Routing geometry, stowage, break-aways | 1 | REQ-H1, REQ-H2 |
| H5 | Delayed evacuation or medical response | Connectors hard to release | 3 | 3 | Operator release, release-time requirement, operator training | 1 | REQ-O1, REQ-O3, REQ-O6 |
| H6 | Ride restraint doesn't lock fully | Harness bulk under the lap bar or OTSR | 4 | 2 | Low-profile design, sensor and position verification | 1 | REQ-O4 |
| H7 | Connector opens in use | Gate loaded against the bar, rider fiddling | 4 | 2 | RAS latch that only an operator key or tool releases; double-action captive-eye snap hooks; two tethers | 1 | REQ-O2, REQ-L5 |
| H8 | Component failure from degradation | UV, chlorine, abrasion, previous arrest | 4 | 2 | Durability specs, inspection, retirement indicator | 1 | REQ-D1 to REQ-D3 |
| H9 | Counterfeit or modified gear | Market knockoffs | 4 | 2 | Serial numbers, anti-counterfeit mark, RAS-certified gear only | 1 | REQ-D4 |
| H10 | False sense of security | Rider or operator skips primary restraint checks | 4 | 2 | Messaging ("backup only"), operator procedures unchanged, optional RAS interlock adds a check | 1 | Ops guide |
| H11 | Projectile hazard | Loose hardware on rides with high spin | 2 | 2 | Captive hardware, stowage | 1 | REQ-H2 |
| H17 | Rider slides out from under the belt (submarining) | Belt high or loose; legs dangling; no crotch strap | 4 | 2 | Low position, minimal slack, crotch strap required on dangling-leg rides | 1 | REQ-L4, REQ-L6, REQ-H4 |
| H18 | Upper body folds out during inversion | Hip Belt alone on an inverting ride | 4 | 2 | Shoulder Module mandatory on inverting rides | 1 | REQ-H4 |
| H19 | Harm from hanging inverted when a ride stops upside down | Long hang time held only at the pelvis | 3 | 2 | Shoulder Module shares the load; inverted-hang test; evacuation priority | 1 | REQ-H5 |
| H20 | Groin or pelvic injury from the front-center tether | Center anchor behind the buckle, or tether loaded upward | 3 | 2 | Anchor forward of the hip point, downward and forward tether angle, short stiff tether | 1 | REQ-L8, REQ-A4 |
| H21 | Center tether interferes with the restraint, or is left unclipped | Clash with a lap-bar center post; rider forgets the third clip | 3 | 3 | RAS keep-out zone, center-anchor clipped sensor, operator check | 1 | REQ-O4, REQ-A4 |
| H22 | Center strap in the wrong mode or wrong length | Clipped to the anchor at the W length (slack); tail left loose; attempt to use both modes at once | 3 | 3 | Single free-end connector, sewn A/W stops, color band, stow pocket, operator check | 1 | REQ-L9 |
| H23 | Rider can't be freed from a loaded tether during a rescue | Carabiners and snap hooks can't open under load; ride stopped inverted | 4 | 2 | Release that works under load in the RAS receiver; rescue procedure; cut-tool backup in the operator kit | 1 | REQ-O7 |
| H24 | Latch looks closed but isn't (false latch) | Tongue partly inserted, or debris in the receiver | 4 | 2 | Positive-latch geometry, sensor and visual indicator, operator check | 1 | REQ-O8 |
| H27 | **Drowning:** a tethered rider is held underwater | A water-ride boat or raft capsizes, sinks or floods | 4 | 2 | **Not rated for capsizable water rides** (rafts, log and boat rides where the vehicle can roll or flood). Elsewhere, only with an operator-approved rapid self-release | 1 | REQ-H6 |
| H28 | RideBelt worn but not clipped, or not checked | Same human-check failure as the primary restraint (incident mode R2) | 4 | 3 | RAS clipped-in sensor wired into ride dispatch (RAS §5.3) is the real fix; the visual flag supports operator checks | 2 | REQ-A3 |
| H12 | Wrong fit, wrong product or missing module | Child or small rider in an adult belt; missing required module | 4 | 2 | Size labels, fit check, SKU ratings, tag-based SKU check at the anchor | 1 | REQ-F1 to REQ-F3, REQ-H4, REQ-T3 |
| H13 | Themed shell hides damage or interferes with the restraint | Covers over buckles or inspection windows; bulk under the lap bar | 4 | 2 | Theming Rules TR-1 to TR-6; T-F5 for each themed SKU | 1 | REQ-T1, REQ-T2 |
| H14 | Decorations become projectiles or snag | Rigid ears, horns or other add-ons | 3 | 3 | TR-3: soft, low-profile, break-away only | 1 | REQ-T2, REQ-H2 |
| H15 | Battery fire, leak or projectile (Plus module) | Impact, water, defective cell | 3 | 2 | Certified cells, IP67, stowed pocket, removed on high-energy rides | 1 | REQ-T4 |
| H16 | RF interference with ride controls | Active module emissions | 4 | 1 | EMC testing; manufacturer EMC sign-off for each ride | 1 | REQ-T5 |

## Open questions for safety-engineer review #1
1. What ATD injury criteria apply to pelvic, abdominal and thoracic arrest loads at amusement-ride G levels? Which ATD best detects submarining and belt migration onto the abdomen (e.g., THOR's abdomen instrumentation)?
2. Should RAS require the clipped-in sensor to be part of ride dispatch logic (ISO 13849 performance level)?
3. How should the energy absorber be tuned so it doesn't add free travel (H3) while limiting peak force (H2)?
