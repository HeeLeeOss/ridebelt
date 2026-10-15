# Concept Design & Trade Study v0.2 (Phase 3)

> 🚧 **DRAFT: not reviewed by a qualified engineer; not for use.** Not released until the MVP review gate. See [SAFETY-NOTICE](../../SAFETY-NOTICE.md).


> **v0.2 change:** the primary product is now a **low hip belt with no leg loops**, with add-on modules for higher-risk rides. The reasons are explained below. v0.1 made a full harness with leg loops primary, which would be a hard sell to ordinary riders.

## Design principle: keep the rider *in the seat*, don't catch them *in the air*
Leg loops come from fall arrest, where a person hangs in free space. RideBelt's tethers are short (≤ 10 cm of free travel, REQ-L4), so the rider never leaves the seat. The job is to **hold the pelvis down onto the seat pan**, and the seat itself carries the rider. Car and aircraft lap belts work this way, and many coasters already use a plain seat belt as a secondary restraint.

Two things make this work:
1. **Belt position:** low, across the pelvic bones and the tops of the thighs. **Never at the waist.** A waist-high belt rides onto the soft abdomen ("seat belt syndrome") and lets the rider slide out from under it.
2. **Tether geometry:** tethers run **down and slightly rearward** to anchors low on each side of the seat, roughly 45–75° from horizontal (TBD by simulation), with almost no slack. Loading pulls the belt down onto the pelvis, never up toward the abdomen.

## Modular product family
| Module | Description | Required for |
|---|---|---|
| **RideBelt Hip Belt** (core, primary SKU) | Wide (≥ TBD mm), semi-rigid, padded belt worn low on the pelvis. Two short side tethers to low anchors. Fit guide shows the correct position | Every ride |
| **Shoulder Module** (clip-on) | Two shoulder straps that clip to the Hip Belt; a sternum strap keeps them on the shoulders. Not part of the main load path | Shoulder protection for riders who also ride lower-energy rides and want to remove it. Required on inverting rides (this module or the Integrated Harness). Keeps the upper body from folding out, and gives support if the ride stops with riders upside down |
| **RideBelt Integrated Harness** (one piece) | Hip Belt and shoulder straps **permanently sewn together**, with nothing to clip on or remove. Same hip-belt load path and side tethers as the Hip Belt; the shoulder straps and sternum strap are built in. Fit is adjusted by waist and shoulder-strap length buckles | Meets the shoulder requirement on **every** ride class with nothing to forget. Preferred for riders who mainly ride inverting coasters and drop towers, for park rental fleets, and for younger riders |
| **Convertible Center Strap** (anti-submarine module) | One strap fixed to the belt's front buckle, with **two modes**: **Anchor mode (3-Point Tie-Down):** short, clipped down to an RAS-3 center anchor on the seat pan, with nothing worn between the legs. **Wearable mode (crotch strap):** full length, passed between the legs and clipped to the belt's rear ring, racing-harness style. See the design rules below | Anchor mode on RAS-3 seats (preferred). Wearable mode on seats without a center anchor. One of the two is **required** on drop towers and dangling-leg seats |
| **Tether Kit** | Two independent side tethers, each 15–30 cm and adjustable. A permanent captive-pin or sewn connection at the belt end. **RAS latch tongue** at the anchor end, plus a **self-locking double-action snap hook** for wrap-strap rides (see trade study D). Inline energy absorber | Every ride |
| **Universal Wrap Strap** | Rated sling with sleeve, choke-wrapped around an approved seat-frame member | Legacy rides without RAS anchors |

## Ride rating matrix (pending dynamic testing, T-D2)
"+ Shoulder" means either the clip-on Shoulder Module or the one-piece Integrated Harness.

| Ride class | Hip Belt | + Shoulder | Convertible Center Strap |
|---|---|---|---|
| Flat rides, swings, sky swings | ✔ | — | Anchor mode recommended where available |
| Non-inverting coasters (including airtime hills) | ✔ | Recommended | Anchor mode recommended where available |
| Pendulums that don't fully invert | ✔ | Recommended | Anchor mode recommended where available |
| Inverting coasters, fully inverting pendulums | ✔ | **Required** | Anchor mode recommended where available |
| Drop towers, seats with dangling legs | ✔ | **Required** | **Required**: anchor mode on RAS-3 seats, wearable mode otherwise |
| Water rides where the vehicle can capsize or flood | **Not rated** (drowning risk, H27) | — | — |

The tag-based check (REQ-T3) lets an RAS anchor or an operator's reader confirm the right modules are fitted for that ride. On RAS seats with sensors, the center anchor can also report that it is clipped.

### Why the 3-Point Tie-Down works
- **The anti-submarine strap is anchored to the seat**, the way racing harnesses do it (the "sub strap" runs from the lap-belt buckle to the seat). A front-center tether pulls the front of the belt **down**, so the belt can't ride up onto the abdomen and the pelvis can't slide out under it. That directly addresses the top FMEA risk, belt migration (RPN 225).
- **With three short tethers, the belt can't move relative to the seat** in any direction: the side tethers hold it back and down, and the front tether holds it forward and down.
- **It's an easier sell:** the rider wears only the belt. The center tether clips on at the front, and nothing goes under the crotch.
- **It does not replace the Shoulder Module** on inverting rides. It controls the pelvis, not the upper body.

### Design rules for the Convertible Center Strap
**Both modes**
- The front end is permanently sewn to the belt's front buckle. The free end has **one connector (an RAS latch tongue)**, which fits both the RAS-3 center anchor and a matching latch receiver on the belt's rear.
- **Only one mode at a time, by design.** With a single free-end connector, the strap can't be clipped to the seat anchor and the rear ring together. That matters because in a combined setup, a rising rider would pull the strap up into the groin (H20).
- Strength meets REQ-L2 in both modes.

**Setting the length: two fixed positions, never free adjustment**
- A locking slider has two **sewn hard stops**: **A** (anchor length, short) and **W** (wearable length, long). The strap can't be set anywhere between them.
- **Mode indicator:** a colored band shows at the buckle (e.g., green for A, blue for W), so the operator can check the mode at a glance.
- In A mode, the spare tail tucks into a closed stow pocket on the belt. It can't hang loose or snag (REQ-H2).
- The tag check (REQ-T3) can be extended so an RAS-3 center anchor with a sensor confirms the strap is clipped to it.

**Anchor mode (3-Point Tie-Down)**
- The anchor sits on the seat pan **forward of the pelvis**, between the thighs, so the strap runs down and slightly forward from the buckle. It must **never pull up into the groin** (H20).
- Short and stiff at the A stop (≤ TBD cm), with no energy absorber, so the side tethers take the main ejection load.
- Must not clash with lap bars that have a center post or shin bar. RAS-3 defines a keep-out zone.

**Wearable mode (crotch strap)**
- At the W stop, the strap passes between the legs to the belt's rear ring, with a padded section where it crosses the crotch.
- Sized so it is snug when seated. A single fit range covers the size band of the belt (TBD).

**Slack control (now preferred, from the arrest model):** slack is the biggest driver of peak load. With zero slack the dynamic factor is about 1.0–1.3; with 5–10 cm it is about 2–3.4 (load-analysis §2a). **Self-retracting, inertia-locking tethers** (like a car seat-belt reel) are now the preferred side-tether design, because they take up slack automatically and speed up clipping in at three points. The fallback is a one-pull cinch. The reel must still meet the 30 kN MBS when locked; its lock-up distance counts toward slack. Detailed design is in [ras-latch.md](ras-latch.md) (connectors) and is still TBD for the reel.

## Trade studies
### A. Primary architecture
| Criterion | Weight | Waist belt (v0.1 "Belt") | Full harness + leg loops (v0.1 primary) | **Low hip belt + modules (v0.2)** |
|---|---|---|---|---|
| Arrest injury risk (REQ-L3) | 5 | 1 | 4 | 4 |
| Retention across ride classes | 5 | 1 | 5 | 4 |
| Consumer acceptance and comfort | 4 | 4 | 1 | 4 |
| Don and doff time | 2 | 5 | 2 | 4 |
| Restraint interference | 3 | 4 | 2 | 4 |
| **Weighted total** | | **47** | **59** | **80** |

→ **Low hip belt with modules.** A waist-position belt is ruled out entirely.

### A2. Clip-on Shoulder Module vs. Integrated Harness
| Criterion | Clip-on Shoulder Module | Integrated Harness |
|---|---|---|
| Can the rider forget or misfit the shoulder part? | Yes: a missing module is FMEA RPN 144 (H12), so it relies on labels, the operator check and the tag check | **No.** It is always present, so that failure mode is gone |
| Don and check time | Slower: extra clips, and the operator checks module fitment | Faster: one garment, one check |
| Flexibility | Remove it for flat rides and swings | Shoulder straps always worn; possibly warmer and bulkier on low-energy rides |
| Restraint interference (REQ-O4, H6) | Only when fitted | Always present under over-the-shoulder restraints and lap bars. **Every ride class needs the T-F5 interference check** |
| Sizing | Belt sizes plus one strap size range | Belt and torso length together: more sizes, or wider adjustment |
| Durability and inspection | Separate parts, inspected separately | One assembly; damage to the shoulder straps retires the whole unit |
| Rental fleets | More loose parts to manage | Simpler: one part per rider |

→ **Offer both.** The Integrated Harness is preferred for rental fleets, younger riders, and riders who mostly ride inverting rides or drop towers. The clip-on module suits riders who mix ride types.

**Design rules for the Integrated Harness**
- The shoulder straps are **not** the main load path. Ejection loads still go hip belt → side tethers. The arrest-model results and the 30 kN tether and anchor ratings apply unchanged.
- The sewn joints between belt and shoulder straps are rated to the Shoulder Module's own load case (inverted hang, upper-body restraint). They are tested in T-S1 and T-D2/T-D4 like the clip-on version.
- **Strappy construction, not a vest.** Torso fit comes from shoulder-strap length buckles. Do **not** use a vest panel with a height adjuster that moves the shoulder bands relative to the waist portion, and never add leg flaps or leg loops. This stays clear of Universal's US 11,975,679 claim 1 / EP 4 380 708 (vest + height adjuster + leg flaps) and the vest-shackle architecture of US 9,162,089. See [research/patentability-fto.md](../research/patentability-fto.md).
- The neck-zone rule (REQ-H1) applies: the sternum strap and shoulder straps must stay clear of the neck at every size.
- Its tag (REQ-T3) registers the unit as "Hip Belt + Shoulder", so the module check passes automatically on inverting rides.

### B. Shoulder-only harness: rejected as a standalone product
- When anchored low, the rider can slide down and forward out from under the straps (submarining).
- When the rider is lifted, the load goes through the shoulders toward the neck (H4).
- Kept only as an **add-on** to the Hip Belt.

### C. One tether vs. two
Two tethers, for redundancy (REQ-L5) and to keep the rider centered under lateral loads.

### D. Anchor-end connector
| Connector | Speed | Rider can't open it | Can't load sideways | Sensor-ready | Releases under load | Verdict |
|---|---|---|---|---|---|---|
| Triple-action carabiner | Slow | Good | **Poor** (gate and sideways loading) | Poor | **No** | Dropped as the primary connector |
| **Self-locking double-action snap hook**, captive eye (ANSI Z359.12 / EN 362) | Medium | Good | Good | Poor | No | **Wrap-strap rides** |
| **Keyed/tool-release latch** (seat-belt tongue or ISOFIX-style jaw onto an anchor bar) | **Fast** (push to lock) | **Excellent** (operator key or tool only) | **Excellent** | **Excellent** | Possible, if designed for it | **RAS anchors (primary)** |
| T-bar / keyhole slot | Fast | Good | Excellent | Good | Possible | Alternative for the RAS latch, evaluate |
| Ball-lock pin (PIP) | Slow | Good | Good | Good | No | Rejected (two hands, parts can be lost) |
| Racing rotary cam buckle | Fast | **Poor** (rider can twist it) | n/a | Fair | Yes | Rejected for anchors |
| 3-ring release | n/a | Excellent | n/a | Fair | **Yes**, at very low force | **Inside the operator release mechanism** |
| Magnet-guided mechanical buckle | Fast | Fair | Good | Good | No | Watch list; few are rated for life safety |

**Decision:**
- **RAS seats:** a keyed or tool-release **RAS latch**. The tether carries the tongue and the anchor carries the receiver. It locks with a push, cannot be loaded sideways, and has a clipped-in sensor built in.
- **Wrap-strap rides:** a self-locking double-action **snap hook** with a captive eye. The tongue-to-snap-hook adapter is a permanent sewn tether variant, never something the rider assembles.
- **Belt end:** a permanent connection, sewn or captive-pin. Riders never handle it.
- **Rescue:** every anchor-side release must **work under full load**, so a rider hanging in a stopped, inverted ride can be freed (REQ-O7). Candidates: a 3-ring-style release inside the RAS receiver, or a latch rated for release under load.
- **IP:** connector choice alone does not avoid US 11,975,679 ("keylocks" clipping into brackets). Keep the release mechanical or wired, to avoid US 12,134,366. See [research/patentability-fto.md](../research/patentability-fto.md).

## Next steps
- CAD and mock-ups of the hip belt shape (contoured to stay on the pelvis), the tether exit point and the anchor angle range.
- Fit trials on representative seats: lap-bar coaster, OTSR inverter, drop tower, swing seat.
- Sled-test matrix (T-D2): Hip Belt alone vs. each module combination, in each ride class.
