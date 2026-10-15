# RideBelt

**An optional, rider-worn backup restraint for amusement rides — plus a free, open anchor standard (RAS) that ride designers can build into seats.**

A [Hee-Lee Oss](https://github.com/HeeLeeOss) good-deed project. Content is [CC BY 4.0](LICENSE); code is [MIT](LICENSE-CODE).

> ⚠️ **DRAFT: not reviewed by a qualified engineer, not tested, not for use.** Do not build, wear or attach anything to a ride based on this repository. Read the **[Safety Notice](SAFETY-NOTICE.md)**. Nothing is released until it passes the MVP review gate in [GOVERNANCE.md](GOVERNANCE.md).

**Start here:** [PLAN.md](PLAN.md) (project plan) · [TASKS.md](TASKS.md) (work for contributors) · [GOVERNANCE.md](GOVERNANCE.md) (reviewers and gates)

## The problem
Riders have been killed or badly hurt when a ride's primary restraint (lap bar, over-the-shoulder harness or seat belt) failed, was out of adjustment, or didn't fit the rider. Once the primary restraint has failed, the rider has nothing else holding them in.

## The idea
1. **RideBelt wearables.** A rider puts on a low hip belt with short, auto-locking tethers, and adds clip-on shoulder or crotch-strap modules for higher-risk rides. A one-piece **Integrated Harness** version has the belt and shoulder straps sewn together, so there's nothing to clip on or forget.
2. **RideBelt Anchor Standard (RAS).** A standardized, rated anchor point that ride manufacturers design into seat structures. It is an **open standard**, free to implement. The aim is to contribute it to ASTM F24.
3. **Universal Wrap Strap.** On legacy rides without an RAS anchor, a rated webbing loop wraps a structural member of the seat, so the rider can clip in.

If the ride's restraint fails, the tethers keep the rider attached to the seat structure.

## Key design principles
- **Keep the rider in the seat, not catch them in the air.** Short tethers hold the pelvis down on the seat pan, the way a car or aircraft lap belt does, so no leg loops are needed. The belt is worn **low on the pelvis, never at the waist** (a waist belt loads the abdomen). Shoulder and crotch-strap modules are added for inverting rides and drop towers.
- **Full strength, simpler design.** If the primary restraint fails, the backup must take the ride's full peak loads with a 5:1 margin. It does not have to copy the primary restraint's design or comfort features.
- **Anchor to structure, never to the part that might fail.** A tether clipped to a failed lap bar protects nothing.
- **Short tethers.** Minimal free travel, so a partly ejected rider can't strike the structure.
- **Rescue-compatible.** Riders can't open the connectors. RAS seats use push-to-lock latches that only an operator key or tool can release, and the release works **even while the tether is loaded** (e.g., a ride stopped upside down). Wrap-strap rides use self-locking snap hooks.
- **No interference** with ride restraint sensors, clearance envelopes or evacuation.
- **Park opt-in.** Rider use is always at the operator's discretion.

## Product family
| Module | Rides |
|---|---|
| RideBelt Hip Belt (primary) | All rides |
| + Shoulder Module (clip-on) | Required on inverting rides (this or the Integrated Harness) |
| RideBelt Integrated Harness | Hip Belt with built-in, non-removable shoulder straps. Meets the shoulder requirement on every ride; suited to rental fleets, younger riders, and inverting rides and drop towers |
| + Convertible Center Strap | One strap, two modes. **Anchor mode** clips it short to an RAS-3 seat center anchor (a 3-point tie-down, with nothing between the legs). **Wearable mode** uses it as a crotch strap on seats with no center anchor. One mode is required on drop towers and dangling-leg seats, and anchor mode is recommended everywhere |
| Tether Kit | All |
| Universal Wrap Strap | Legacy rides without RAS anchors |

The full ride rating matrix is in [docs/design/concepts.md](docs/design/concepts.md).

## Repository map
| Path | Contents |
|---|---|
| [docs/research/](docs/research/) | Incident review (26 cases), standards map (current editions), [ride acceleration data & design load cases](docs/research/ride-acceleration-data.md), prior art, [patent & freedom-to-operate review](docs/research/patentability-fto.md) (the project chose open publication, not patents) |
| [docs/requirements.md](docs/requirements.md) | Numbered, testable requirements |
| [docs/safety/](docs/safety/) | Hazard analysis and FMEA |
| [docs/design/](docs/design/) | Concepts and trade studies, [RAS latch/release/sensor spec](docs/design/ras-latch.md), [concept geometry](docs/design/geometry/side_view.png) |
| [docs/standard/](docs/standard/) | RAS v0.1 draft standard |
| [docs/analysis/](docs/analysis/) | Load analysis, [arrest model](docs/analysis/arrest_model.py) and its results |
| [docs/testing/](docs/testing/) | Test plan and traceability |
| [docs/business/](docs/business/) | Open-standard adoption model, stakeholders, and the [post-launch plan](docs/business/post-launch.md) (theming, rider ID, connected experiences) |

## Roadmap
| Phase | Gate |
|---|---|
| 0 Research | Incident and standards baseline complete |
| 1 Requirements | Load cases confirmed against measured ride data |
| 2 Hazard analysis | Draft complete (early engineer review optional) |
| 3 Concepts | Hip belt + modules architecture confirmed by sled tests |
| 4 RAS draft | Reviewed by at least one ride manufacturer |
| 5 Analysis | Draft complete |
| **MVP gate** | **Independent credentialed engineer review of all safety content and bench/ATD results, before any human wear or any RELEASED content** |
| 6 Prototype & test | Third-party certification |
| 7 Adoption | RAS submitted to ASTM F24; certification program; legal and product-liability sign-off |
| 8 Post-launch (L1–L4) | Themed shells, rider ID, connected experiences; privacy review before each stage |
