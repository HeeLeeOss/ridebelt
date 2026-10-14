# RideBelt Anchor Standard (RAS) — Draft v0.1

> 🚧 **DRAFT: not reviewed by a qualified engineer; not for use.** Not released until the MVP review gate. See [SAFETY-NOTICE](../../SAFETY-NOTICE.md).


> Working draft for discussion with ride manufacturers and ASTM F24. Values marked TBD are set from Phase 1 load cases.

## 1. Scope
This standard defines a secondary anchor point on amusement ride seats. Rider-worn RideBelt-certified equipment attaches to it. RAS anchors **add to** the ride's primary restraint system; they never replace it or change how it is designed.

## 2. Terms
- **Primary restraint:** the ride's engineered patron restraint (lap bar, OTSR, belt).
- **RAS anchor:** a rated attachment point that meets this standard.
- **Anchor pair:** two RAS anchors serving one seat position.
- **Operator release:** a mechanism that only the operator can work, which frees the rider's tethers from the anchors.

## 3. Placement requirements
3.1 Each seat position shall have one anchor pair, placed one on each side of the rider, below and slightly behind the hip point. A tightened tether shall run down and rearward at TBD 45–75° from horizontal (REQ-L7), so the Hip Belt is loaded onto the pelvis. The envelope is TBD relative to the seat reference point.
3.1a **RAS-3 (three-point seat):** seats may add a **center anchor** on the seat pan, between the rider's thighs and forward of the hip point. The front-center tether runs from the belt buckle down and slightly forward, and shall never be loaded upward into the groin. **RAS-3 is required for drop-tower and dangling-leg seats** that claim RAS conformance, and recommended for all other seats.
3.1b The center anchor shall not stop the primary restraint closing, and shall stay clear of center posts and shin bars (keep-out zone TBD).
3.1c Seats without a center anchor (**RAS-2**) depend on the rider's Convertible Center Strap in wearable (crotch-strap) mode for anti-submarine protection on ride classes that require it.
3.1d The center anchor shall use the same RAS latch receiver (§5.1) as the side anchors, so it accepts the tongue at the free end of the Convertible Center Strap.
3.2 Anchors shall mount to the **seat or car structure** through a load path **independent** of the primary restraint, its locking mechanism and its sensors.
3.3 No anchor or attached tether shall enter the patron clearance envelope or stop the primary restraint closing.
3.4 Anchor edges and the surrounding structure within TBD mm shall have a minimum radius of TBD mm (to protect the tether from abrasion).

## 4. Strength
4.1 Rated load per anchor: ≥ **30 kN** (5 × the preliminary 6 kN design load per tether, REQ-L2), in any direction within the tether angle window. To be confirmed against measured ride data.
4.2 No permanent deformation at 2 × design peak load (12 kN).
4.3 Anchor geometry shall load the connector along its major axis only (no gate loading or cross-loading).
4.4 Fasteners shall be redundant, or of a secured type (e.g., safety-wired or prevailing torque), with torque marking.

## 5. Interface
5.1 **RAS latch (primary):** a receiver for the standard RAS tongue (geometry TBD). It locks with a push, cannot be loaded sideways, and gives a positive indication when latched. A partly inserted tongue shall show "unlatched". Release is only by an operator key or tool, or by a **wired** actuator under ride control. **No wireless lock or unlock.**
5.2 **Release under load:** the receiver's release shall work while the tether carries load up to TBD kN, with ≤ TBD N of operator force and no uncontrolled drop of the rider (REQ-O7). Possible mechanism: a 3-ring-style or toggle release inside the receiver.
5.2a **Bar fallback:** a closed bar of TBD mm diameter next to the receiver, accepting a self-locking snap hook for gear without an RAS tongue. Gear clipped to the bar has no sensor and no release under load, so operators shall treat it as wrap-strap gear.
5.3 **Clipped-in sensor (optional):** dual-channel output (TBD electrical interface). If it is used in dispatch logic, it shall meet a performance level set by the ride's risk assessment (ISO 13849).
5.4 Visual indicator: green when engaged, visible to the operator from the platform.

## 6. Marking
Each anchor is marked with "RAS-2" or "RAS-3", the standard version, the rated load, the manufacturer, the serial number and the inspection due date.

## 7. Conformance tests
| ID | Test | Pass criteria |
|---|---|---|
| RAS-CT0 | Design review of the load path | Independent of the primary restraint (3.2) |
| RAS-CT1 | Static pull, in each loading direction | Holds the rated load for 3 min; no permanent set at 2× |
| RAS-CT2 | Connector orientation | Connector cannot be cross-loaded in any rider position |
| RAS-CT3 | Fatigue | TBD cycles at the ride's service load spectrum with no cracks. Pendulum rides repeat −1 g every swing, so the cycle count comes from the ride's lifetime cycles |
| RAS-CT4 | Sensor (if fitted) | Correct state in 100% of TBD engage/disengage cycles; single faults detected |
| RAS-CT6 | Release under load | Releases at the rated hang load within the force and time limits, with no uncontrolled drop (REQ-O7) |
| RAS-CT7 | False latch | A partly inserted tongue always shows "unlatched"; debris and ice cases tested |
| RAS-CT5 | Clearance | Fixture check with tethers attached and the primary restraint closed |

## 8. Operator procedures (informative)
- Rider use of RideBelt stays at the operator's discretion.
- Primary-restraint checks are **unchanged**. RAS adds a step and never replaces one.
- Evacuation plans include RAS release steps and timing.
