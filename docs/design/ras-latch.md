# RAS Latch, Operator Release & Clipped-In Sensor: Design Spec v0.1

> 🚧 **DRAFT: not reviewed by a qualified engineer; not for use.** Not released until the MVP review gate. See [SAFETY-NOTICE](../../SAFETY-NOTICE.md).


Implements RAS-v0.1 §5 and REQ-O2, REQ-O3, REQ-O7, REQ-O8 and REQ-A3. Loads come from [analysis/load-analysis.md](../analysis/load-analysis.md). The IP constraints come from [research/patentability-fto.md](../research/patentability-fto.md): no wireless lock or unlock, and no spring-plate slide sensor of the kind in GM's patent.

## 1. Architecture
```
 TETHER (rider side)                        RECEIVER (seat side, RAS anchor)
 ┌──────────────────────┐                   ┌─────────────────────────────────────────┐
 │ webbing loop (sewn)  │                   │ housing bolted to seat structure        │
 │   │                  │   push to lock    │  ├─ twin latch pawls (A + B)            │
 │ TONGUE ──────────────┼──────────────────▶│  ├─ ejector spring                      │
 │  ├─ keyed asymmetric │                   │  ├─ mechanical indicator flag           │
 │  ├─ magnet           │                   │  ├─ Hall sensor (tongue present)        │
 │  └─ NFC tag (molded) │                   │  ├─ pawl switches A, B (latched)        │
 └──────────────────────┘                   │  ├─ NFC reader coil (gear identity)     │
                                            │  └─ operator release: key cam (+ wired) │
                                            └─────────────────────────────────────────┘
```

## 2. Tongue (on the tether)
| Item | Spec |
|---|---|
| Material | 17-4PH stainless (H900/H1025) or forged 4140 with Zn-Ni plating. Final choice after fatigue and corrosion tests |
| Envelope | About 30 mm wide, 5 mm thick, 55 mm long (TBD after the CAD and FEA in A4) |
| Keying | Asymmetric profile (one chamfered corner), so it fits **only one way**. The geometry stops gate loading and sideways loading (RAS-CT2) |
| Latch window | Rectangular window engaged by the two pawls |
| Magnet | Small NdFeB magnet potted in a polymer overmold at the tip; triggers the receiver's Hall sensor |
| Identity | Passive NFC tag (NTAG 424 DNA class) molded into the tongue's overmold. The **tongue carries the gear's identity**, so the anchor knows exactly which certified unit is latched at which seat position |
| Webbing joint | Bar-tacked loop through a slot in the tongue, or a captive pin. Never handled by the rider |
| Rated strength | MBS ≥ **30 kN** along its main axis (5 × the 6 kN design load per tether; see §6) |

## 3. Receiver (on the seat)
| Item | Spec |
|---|---|
| Latching | **Twin independent pawls** (A and B). **Each alone** holds the full rated load (redundancy, REQ-L5 spirit). Spring-biased closed, so the tongue latches with a push (≤ 40 N insertion force) |
| Ejector | A spring-loaded ejector pushes out any tongue that isn't fully latched. **A partly inserted tongue cannot stay in** (anti-false-latch, RAS-CT7, H24). Same principle as car seat-belt buckles |
| Indicator | A **mechanical** flag driven by pawl travel: GREEN only when both pawls are fully engaged, RED otherwise. Visible from the platform, and works with no power |
| Confirmation | Audible click from the pawls seating (REQ-O8) |
| Debris | Through-drain slot, so sand, ice or water drain out the bottom. Debris and ice cases are tested in RAS-CT7 |
| Mounting | At least 2 fasteners into seat structure; either alone holds the rated load. Prevailing-torque nuts and torque-stripe marking (RAS §4.4) |
| Housing | Cast aluminum or stainless; IP67 electronics compartment; −20 °C to +60 °C; salt spray ISO 9227, 500 h |

## 4. Operator release (REQ-O3, REQ-O7)
| Item | Spec |
|---|---|
| Primary | **Mechanical key cam.** A ride-specific key (or a triangular or hex security tool) turns a cam that lifts **both pawls**. Riders have no way to release it |
| Optional | A **wired** solenoid lifts the pawls only on a ride-control command at the unload station. Power loss leaves the latch **closed**; the mechanical key always overrides. **No wireless actuation** (FTO, US 12,134,366) |
| Release under load | The key releases a tether loaded up to **2.0 kN** (the inverted-hang load of a 160 kg rider at 45° tethers ≈ 1.1 kN, with about 1.8× margin) using **≤ 150 N at the key**. Roller-faced pawls cut friction: about 0.15 × 2 kN ≈ 300 N at the pawl, through a ≥ 3:1 cam ratio, gives ≤ 100 N at the key |
| No sudden drop | Rescue procedure: the rescuer supports the rider (or a second line takes the load) before releasing; the release order goes center → side → side. An alternative under evaluation is a **3-ring-style cascade** inside the receiver, which releases at very low force and can pay out in a controlled way |
| Backup | A cutting tool in the operator rescue kit, with a webbing-cut point marked on every tether (H23) |

## 5. Clipped-in sensing (REQ-A3, RAS §5.3)
Two **independent** principles, so that any single fault is detected:

| Channel | Detects | Principle |
|---|---|---|
| CH1 | Tongue fully inserted | Hall-effect sensor sensing the magnet in the tongue |
| CH2 | Both pawls engaged | Two micro-switches, one per pawl, in series |
| ID | *Which* gear is latched | NFC reader coil reads the tongue's tag; a crypto-authentication challenge (REQ-T3) |

- **LATCHED** = CH1 ∧ CH2 ∧ (ID valid, if the ride uses gear compliance). A CH1/CH2 mismatch for more than 200 ms raises a fault.
- Output: dual-channel 24 V to the ride PLC. If used in dispatch logic, the performance level is set by the ride's risk assessment (ISO 13849, likely PL c–d).
- Self-test: both channels must change state on every latch and unlatch cycle. A channel that never changes is a fault.
- **Gear compliance check** (patent candidate #2): the reader checks the tag for authenticity, service-life date, any arrest-event retirement flag, and that the **modules required for that ride class** are registered on the belt. It reports pass or fail to the PLC or operator display. The decision logic belongs to the ride. RAS only supplies the signal.
- The sensing deliberately avoids a spring-biased plate-and-slide detector behind a loop bar (GM US 11,396,248).

## 6. Load basis
From the arrest model (A2, §2a–2b), with 60° tethers:
- 160 kg design rider (about the civilian P99) at a −2.0 g rating with slack ≤ 2 cm: ≤ 4.0 kN. With 10 cm slack (misuse) and no absorber it can reach 7.7 kN, so the 4 kN absorber is required.
- **Design load per tether: 6 kN** (preliminary; check against measured ride data). MBS ≥ **30 kN** (5:1). No permanent set at 12 kN (2×).
- Center anchor (anchor mode): it does positioning only, but is rated the same, so one latch part number fits all anchor positions.

## 7. Wrap-strap connector (non-RAS rides)
- ANSI Z359.12 / EN 362 **self-locking double-action snap hook**, captive eye, gate ≥ 16 kN (3,600 lbf), MBS ≥ 22 kN.
- Because 22 kN < 30 kN, wrap-strap gear relies on the **4 kN absorber cap**: 22 kN / 4 kN = 5.5:1, which meets the 5:1 margin. Wrap-strap tethers therefore **must** include the absorber. Without it they are limited to ride classes rated ≤ −1.0 g.
- No sensor and no release under load. Rescue uses the cut point and support procedure (§4).

## 8. Open items
- FEA of the tongue, pawls and housing (A4).
- Choose the pawl and cam geometry for the release-under-load force target; prototype a 3-ring cascade alternative.
- Check whether the key profile should be one universal RAS key or set per park.
- Prototype the Hall and NFC coexistence (the magnet near the NFC coil).
- Check against TEAM IX family claims once drawn (FTO §2).
