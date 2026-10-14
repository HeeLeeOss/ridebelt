# Post-Launch Plan: Theming, Rider ID & Connected Experiences v0.1

**Goal:** turn RideBelt from a safety accessory into something riders *want* to wear: themed, personal and connected. The cool factor drives adoption, adoption drives RAS uptake, and RAS uptake drives safety.

> **Ground rule:** nothing in this plan may touch the certified load path. Theming and electronics live on a **separate, non-structural layer**, and adding them must not require re-certifying the harness.

---

## 1. Architecture: certified core + experience layer
| Layer | Contents | Who can change it |
|---|---|---|
| **Certified core** | Webbing, stitching, buckles, attachment point, tethers, connectors, absorbers | RideBelt only. Fixed design, third-party certified |
| **Experience shell** | Themed covers, padding, patches, character elements, colorways | Licensed parks and brands within the **Theming Rules** (§2) |
| **Tag module** | Passive RFID/NFC tag (always present), optional active module | RideBelt hardware. Data integration is open to parks via an API |

The shell attaches to the core through defined attachment zones (sleeve-over pads, hook-and-loop panels, patch pockets). It never wraps buckles, connectors, inspection windows or labels.

## 2. Theming & customization
### Product tiers
| Tier | Example | Channel |
|---|---|---|
| **Park-branded** | Park logo and colorways, ride-specific editions ("I rode X" patch) | Park retail, rental at ride entrance |
| **Character/IP-licensed** | Character shoulder pads, franchise colorways | Park retail via IP holder license |
| **Bespoke** | Name embroidery, custom colors, pattern uploads | Online configurator, made to order |
| **Collectibles** | Swappable patches and pins per ride, season or event | Earned in the park (see §4) or purchased |

### Theming Rules (become part of the brand license)
- **TR-1** No changes to certified core parts, no extra holes and no stitching into load webbing.
- **TR-2** Shell elements must not reach the neck zone (REQ-H1) and must break away at ≤ TBD N (REQ-H2).
- **TR-3** No rigid or protruding decorations (ears, horns, wings) that could become projectiles, snag, or enter the ride clearance envelope (H11, REQ-O5). Soft, low-profile or flat-printed elements only.
- **TR-4** Buckles, connectors, inspection windows, labels and the absorber deployment indicator stay visible and uncovered.
- **TR-5** Shell materials meet the same flammability, skin-contact and washability requirements as the core.
- **TR-6** Every themed SKU passes a fit check and restraint-interference check (T-F5) before release.

## 3. Rider ID: RFID/NFC tag module
### Baseline: passive tag in every unit (no battery)
A sealed passive UHF RFID or NFC tag is built into the core. It is required because it **serves safety first**:
- **Authenticity:** RAS anchors and operator handhelds can reject counterfeit gear (FMEA H9).
- **Life tracking:** the gear's serial number links to its manufacture date, inspection history and any arrest event. Expired or retired gear is flagged at the ride entrance (REQ-D3).
- **Module check:** the anchor or an operator reader can confirm the modules the ride requires are fitted, e.g., the Shoulder Module on an inverting ride (REQ-H4). Modules carry their own tags.
- **Clipped-in confirmation:** RAS latch-mode anchors with readers confirm *which* certified unit is clipped into *which* seat. This strengthens the optional interlock (RAS §5.3).

The tag holds **only a random ID**. Personal data stays server-side, linked only if the rider opts in.

### Optional: active "Plus" module (battery)
Clip-in pod for riders who want enhanced experiences: LEDs, haptics, BLE, accelerometer.
- **Detachable**, stowed in a closed pocket, and **removed for high-energy rides** unless the ride's application guide allows it (projectile and battery risk).
- Battery: small, certified (UN 38.3 / IEC 62133), sealed IP67 for water rides, and never part of the load path.
- No RF emissions that could interfere with ride control systems. EMC testing (e.g., FCC Part 15 / EN 301 489) plus a manufacturer EMC sign-off for each ride.

## 4. Connected experiences
| Feature | How | Notes |
|---|---|---|
| **Ride log & stats** | Anchor or entrance reader logs each ride. The Plus module logs G-forces and airtime | "Rode 14 coasters, max 4.2 G" sharing cards |
| **Scorekeeping & quests** | Points for rides, park-wide scavenger hunts, seasonal challenges, credit counting | Rewards: digital badges, physical collectible patches (§2) |
| **Interactive rides** | Tag ID feeds score systems on interactive dark rides and shooting rides | Integrate with the park's existing ride-game systems |
| **Auto ride photos & video** | Seat-level tag read ties on-ride photos to the rider's account | Works with existing park photo vendors |
| **Virtual queue / Lightning-lane** | Tap at the entrance | Partner with the park's ticketing system (MagicBand-style) |
| **Ride effects** | Plus module LEDs or haptics synced to ride moments | Low-energy rides only, or when the application guide allows |
| **Payments** | Link to the park wallet | Park-side; RideBelt only supplies the ID token |
| **Group & family** | Families group their IDs together; reunion help at guest services (parent opt-in) | **No live location tracking of minors by default** (§5) |

### Platform
- **RideBelt ID Service:** registry of gear serials, safety life-cycle data, and the opt-in rider profile.
- **Park Integration API:** parks build their own experiences on top. RideBelt provides identity and safety status, the park owns its guest experience.
- **Rider app:** registration, stats, badges, gear inspection reminders, recall notices.

## 5. Privacy & data rules
Rider tracking, especially of children, is a major legal and trust risk. These rules are non-negotiable design constraints:
- **P-1 Safety data and experience data are separate.** Gear life-cycle data never needs personal identity. Experience features are **opt-in**.
- **P-2 Children:** verifiable parental consent under COPPA (U.S.) and GDPR-K. Child profiles default to minimal data and no location history.
- **P-3 No biometrics** (face or gait). This avoids BIPA, GDPR special-category data and similar regimes.
- **P-4 Data minimization:** zone-level reads (ride entrance, seat), not continuous GPS. Retention limits TBD. Riders can delete their data.
- **P-5 Clone resistance:** tags use cryptographic authentication (e.g., NTAG 424 DNA class), and raw IDs can't be used to track a person outside the park.
- **P-6** Privacy impact assessment and a security review before launch, with an annual audit.

## 6. Business model
| Revenue stream | Notes |
|---|---|
| Themed and bespoke gear sales | Highest margin. Character IP under license royalty |
| Park rental fleet | Rental at ride entrances. Needs hygiene process (washable shell, sanitized core), automatic retirement by tag data |
| Collectible patches & badges | Recurring, earned or purchased |
| Plus module + experience subscription | Ride stats, quests, video, cross-park passport |
| Park integration licensing | Per-reader or per-active-rider fee for the Park Integration API |
| Data insights to parks | Aggregated, anonymized ride throughput and adoption only. **Never sell personal data** |

**Cross-park passport:** one RideBelt works at any RAS park. Ride logs and badges across parks create a network effect and pull more parks into RAS.

## 7. Rollout
| Stage | Scope |
|---|---|
| L1 (launch) | Core gear with passive tag. Safety uses only (authenticity, life cycle) |
| L2 | Park-branded shells and colorways, rider app with ride log, collectible patches |
| L3 | Character IP partnerships, bespoke configurator, interactive-ride scoring integration |
| L4 | Plus module (rides allowed by application guides only), cross-park passport, photo and video integration |

## 8. Safety & certification checks for this plan
- Shell, tag and Plus module added to the hazard analysis (H13–H16) and the requirements (REQ-T*).
- Each new shell design and the Plus module go through T-F5 (restraint interference), T-F7 (entanglement) and EMC testing before release.
- Marketing follows the stakeholder messaging rules: the fun is the hook, but the gear is still a **backup restraint**, used only with park approval.
