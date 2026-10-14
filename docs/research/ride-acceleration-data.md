# Ride Acceleration Data (Phase 1 research, v0.1)

> Status: desk research, compiled 2026-10-14. Feeds analysis A1 in [../analysis/load-analysis.md](../analysis/load-analysis.md) and the TBDs in REQ-L1/REQ-L2 of [../requirements.md](../requirements.md).
>
> **All design load cases in §4 are PRELIMINARY ESTIMATES pending review by a qualified ride engineer** and pending purchase of ASTM F2291 (current edition F2291-26a) and EN 13814-1 / ISO/TS 17929. The paid standards contain the actual envelopes; this document does not reproduce them.
>
> Labels used below: **[measured]** = instrumented data in a published source; **[design/claimed]** = manufacturer, operator or press figure, not independently measured; **[theory]** = calculated in a published source; **[derived]** = our own arithmetic on cited inputs; **[estimate]** = engineering judgement, no source.

## 1. Sign convention

Ride standards (ASTM F2291, EN 13814, ISO/TS 17929) express accelerations as **what the rider feels**, in a body-fixed frame: z along the spine toward the head, x chest-forward, y lateral ([Pendrill & Eager 2020](https://opus.lib.uts.edu.au/rest/bitstreams/634b7dc5-a637-4e34-89c1-264e3db88056/retrieve)). Sitting still = +1 Gz. Accelerometers measure (a − g)/|g| in the moving frame, not acceleration itself ([Pendrill & Modig 2018](https://iopscience.iop.org/article/10.1088/1361-6552/aac3cb)).

- **+Gz** presses the rider into the seat (valleys, braking on drop towers).
- **−Gz** lifts the rider out of the seat. This is the **ejection direction**: with the primary restraint gone, the RideBelt tethers must supply a force of about m × |Gz| × g.
- 0 Gz = weightless (free fall, "floater" airtime). A rider in a free-falling seat is not pushed out; the seat and rider fall together.
- Inverted and stationary = −1 Gz **sustained** (a stopped or slow inverted vehicle). This is the governing case for REQ-H5 and REQ-O7.

## 2. What is publicly known about the standards envelopes

### 2.1 ASTM F2291 (current edition F2291-26a)
- Section 5 is "Patron Restraint, Clearance Envelope, and Containment Design Criteria" (with Annex A1). Section 6 is "Acceleration Limits", with Appendix X1 also titled "Acceleration Limits" ([ASTM store, F2291-25c and F2291-26a pages](https://store.astm.org/f2291-26a.html)).
- F2291 gives limits for each orthogonal axis and for combined magnitudes of orthogonal accelerations (cited in [US patent 10086297](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10086297), referring to F2291-14).
- The limits cover **sustained** accelerations (≥ 200 ms), which are mainly limited by cardiovascular response. Events shorter than 200 ms are treated as "impact events" limited by neuromuscular response and are **not addressed** by the current limits. An open ASTM work item is extending this ([search summary of ASTM work items WK97865/WK91645](https://store.astm.org/workitem-wk91645)). For RideBelt this matters: the snatch load at tether take-up (REQ-L4 free travel) is an impact event outside the F2291 envelope, so it needs separate injury criteria (REQ-L3).
- Restraint classes 1 to 5 are selected mainly from the **−Gz (out-of-seat) acceleration**. See §2.4 and [standards-map.md](standards-map.md).
- **Not found publicly:** the numerical −Gz, ±Gx, ±Gy envelope values versus duration. Do not use any figure for these until the standard is purchased.

### 2.2 ISO/TS 17929:2014 "Biomechanical effects on amusement ride passengers" (and EN 13814-1 Annex J)
Pendrill & Eager (2020) summarize the ISO/TS:
- Recommended maximum **+Gz: 6 g for no more than 1 s, 5 g for no more than 2 s**. Lower levels may last longer: the paper calls 6 s the "recommended limit" for its 4 g periods ([Pendrill & Eager 2020](https://opus.lib.uts.edu.au/rest/bitstreams/634b7dc5-a637-4e34-89c1-264e3db88056/retrieve)).
- Each exposure must stay under a trapezoidal envelope with **maximum onset rate (jerk) 15 g/s** and a trailing-edge drop of **at least 0.8 g/s**.
- Limits in the other axes are given as "egg graphs" (combined-axis envelopes). Values were not reproduced in public sources.
- "This exceeds the maximum G force of 6 g allowed by amusement park standards." Child rides are typically 0.5–2 g, family rides 0–3 g, and thrill rides 4 g or more with negative g, "where the body lifts from the seat, and must be held in place by the restraint system" (same source).
- ISO/TS 17929:2014 was confirmed in 2021, and a revision (ISO/AWI 17929, ISO/TC 254) was registered in December 2023 ([SCC](https://scc-ccn.ca/standardsdb/standards/8158464), [Genorma](https://genorma.com/en/standards/iso-awi-17929)).
- EN 13814-1 contains an informative **Annex J, "Acceleration effects on passengers"** ([SAI Global listing](https://infostore.saiglobal.com/en-us/Standards/16-30328759-DC-0-287605_SAIG_BSI_BSI_665931/)). A secondary source, citing the 2019 version, gives a 6 g maximum measured at a reference point 60 cm above the seat, plus brake deceleration limits of 0.7 g (emergency) and 0.5 g (normal) ([Acta Technica Jaurinensis 2024](https://epa.hu/02500/02537/00060/pdf/EPA02537_atj_2024_2_65-74.pdf)). **Unverified** against the standard; these brake values are probably specific to certain ride types.

### 2.3 Water slides
Water slides fall outside EN 13814. In the U.S., limits are in ASTM F2376 and the human-subject test method is ASTM F3493 (developed as WK72594) ([Interpark](https://interpark.co.uk/news/astm-develops-proposed-standard-test-method-for-waterslides/)). No published measured values were found.

### 2.4 F2291 restraint classes (secondary sources only)
- There are five classes. The main selector is **−Gz**, the force lifting the rider out of the seat ([cavudw.com](https://cavudw.com/santas-sleigh/)). One example treats −Gz beyond −0.2 g as Class 5 territory. That is the blog author's reading, not the standard's text.
- A Class 5 table quoted on the same blog, matching a student write-up citing [F2291-20](https://mackenziegoldman.myportfolio.com/ride-engineering-competition-double-ferris-wheel):
  - **Primary restraint:** one patron per restraint, variable latching position, automatic locking, external indication of locked status, and **redundancy of the locking device**.
  - **Secondary restraint:** permitted in place of locking redundancy. The blog's table says: "Not required. Secondary restraint should be independent of the primary restraint."
- An ASTM work item (WK92171) is adding restraint-positioning and position-monitoring language for Class 4 and Class 5 ([ASTM](https://astm.org/membership-participation/technical-committees/workitems/workitem-wk92171)).
- **Relevance:** F2291 already recognizes an *independent secondary restraint* as a way to meet Class 5 redundancy. RideBelt plus RAS fits this concept, but it would be rider-supplied rather than manufacturer-supplied. Verify against the purchased standard.

## 3. Published data by ride class

Peak values are as stated in the source. "–" means no credible public number was found.

### 3.1 Non-inverting coasters (airtime hills, ejector airtime)
| Quantity | Value | Basis | Source |
|---|---|---|---|
| Peak +Gz (valley) | ≈ 4 g (Balder, wooden) | measured (motion tracker) | [Pendrill, Balder page](https://physics.gu.se/LISEBERG/eng/beowulf.html) |
| Peak +Gz (valley after dive) | nearly 4 g (Valkyria dive coaster) | measured | [Pendrill & Eager 2020](https://opus.lib.uts.edu.au/rest/bitstreams/634b7dc5-a637-4e34-89c1-264e3db88056/retrieve) |
| Peak +Gz, "high-G" coasters | > 5 g (3 coasters, incl. Face/Off, Rock 'n' Roller Coaster, Speed) | measured | [Smith & Meaney 2002, J. Neurotrauma 19(10)](https://www.engineering.upenn.edu/~molneuro/pdfs/SmithMeaney2002_RollerCoasters.pdf) |
| Peak −Gz (airtime) | −1.3 g (Intamin design figures for airtime hills, Walibi Belgium) | design/claimed | [Coaster101](https://www.coaster101.com/?p=39575) |
| Peak −Gz | −1.2 g (Icon, Blackpool, park claim relayed second-hand) | design/claimed, unverified | [CoasterForce forum](https://forums.coasterforce.com/threads/airtime.36395/) |
| Peak −Gz | ≈ −0.9 g (Hyperion; smoothed rider-carried sensor) | measured, informal | [CoasterForce forum](https://forums.coasterforce.com/threads/airtime.36395/) |
| Peak −Gz, valley entry | "slightly negative" (Valkyria) | measured | Pendrill & Eager 2020 |
| Airtime episodes | 10 negative-g episodes per ride (Balder) | measured | Pendrill, Balder page |
| Airtime duration | 6.5 s continuous (Superman: Escape from Krypton, former Guinness record); 27.2 s total per ride (Steel Vengeance) | claimed record | [Wikipedia: Air time (rides)](https://en.wikipedia.org/wiki/Air_time_(rides)) |
| Lateral Gy | 1.2–4.2 g peak "side-to-side" (3 high-G coasters, incl. launched) | measured | Smith & Meaney 2002 |
| Longitudinal Gx | 1.65–5.4 g peak "fore/aft" (same 3 coasters) | measured | Smith & Meaney 2002 |
| Jerk | ≈ 7 g/s into a valley (limit 15 g/s) | measured | Pendrill & Eager 2020 |
| Typical high-G duration | "brief accelerations (<3 s)" | review | Smith & Meaney 2002 |

Notes: ejector airtime is a sharp positive-to-negative transition. Forum analysis notes that peak values depend heavily on sensor filtering and mounting, and smoothing hides short spikes. Peak −Gz of ejector moments therefore probably exceeds the smoothed values above. Our working assumption is pops of about 0.2–1 s **[estimate]**.

### 3.2 Inverting coasters
| Quantity | Value | Basis | Source |
|---|---|---|---|
| Peak +Gz | "close to 4 g" loop entry/exit (Kanonen); "close to 4.5 g" bottom of Norwegian loop (Speed Monster) | measured (3-axis) | [Pendrill, launched coasters](https://physics.gu.se/LISEBERG/eng/launch.html) |
| Gz at top of loop | "essentially weightless" (≈ 0 g) | measured | same |
| −Gz in inversions | Not quantified publicly. Physical bound: a slow or stopped inverted vehicle gives −1 Gz sustained | physics | §1 |
| Gy, Gx | see 3.1 (Smith & Meaney data include Face/Off, an inverting boomerang-type ride) | measured | Smith & Meaney 2002 |
| Coaster general range | "current upper range of peak G forces 4–6 G's" | review | Smith & Meaney 2002 |

### 3.3 Launched coasters
| Quantity | Value | Basis | Source |
|---|---|---|---|
| Launch +Gx (into seatback) | 1.7 g (Formula Rossa, 0–240 km/h) | design/claimed (park) | [Ferrari World figure via search; Wikipedia lists a conflicting 4.8 g "G-force"](https://en.wikipedia.org/wiki/Formula_Rossa) |
| Launch +Gx average | ≈ 1.67 g (Kingda Ka: 0–206 km/h in 3.5 s → 57.2 m/s ÷ 3.5 s = 16.3 m/s²) | derived | [Wikipedia: Kingda Ka](https://en.wikipedia.org/wiki/Kingda_Ka) (ride removed 2024) |
| Launch profile | horizontal force drops during the launch (Kanonen, Speed Monster) | measured | Pendrill, launched coasters |
| Peak +Gz | ≈ 4–4.5 g in loops | measured | Pendrill, launched coasters |
| Fore/aft peak | up to 5.4 g in the Smith & Meaney set (includes launched Rock 'n' Roller Coaster and Speed – The Ride) | measured | Smith & Meaney 2002 |
| −Gz on top-hat crest | "airtime" (no public figure) | – | – |
| Braking −Gx (rider thrown forward) | not given numerically; Speed Monster enters final brakes at 18 m/s | measured (graph only) | Pendrill, launched coasters |

### 3.4 Drop towers (free fall and braking)
| Quantity | Value | Basis | Source |
|---|---|---|---|
| Free-fall phase | ≈ 0 g reading (gravity drop) | measured (teaching data) | [USC Midway Physics handout](https://apple.sc.edu/study/colleges_schools/artsandsciences/physics_and_astronomy/documents/midway-physics-2023-electronic-measurements-1.pdf) |
| Free-fall duration | "just over three seconds" (AtmosFear, 146 m above sea level, ≈ 70 mph) | claimed | [Nordstjernan](https://www.nordstjernan.com/news/nordic/2313/) |
| Pushed-down drop (faster than g) | Turbo Drop "lets the rider fall with 2 g", i.e. about −1 Gz relative to the seat **[derived]**; another source says push-down types can reach "up to three times g" | teaching article / claimed | [Mårtensson-Pendrill & Axelsson, "Science at the Amusement Park"](https://openjournals.library.sydney.edu.au/CAL/article/view/6134/6784); [Science in School](https://www.scienceinschool.org/wp-content/uploads/2014/11/issue20_amusement.pdf); [Burt & Pendrill 2020, Gyldne Tårn](https://iopscience.iop.org/article/10.1088/1361-6552/ab9872) (graph only) |
| Braking +Gz | max ≈ 4 g (AtmosFear) | claimed | Nordstjernan |
| Braking +Gz | ≈ 5 g, permanent magnetic brakes (Fabbri Scary Drop) | manufacturer marketing | [Fabbri](https://www.fabbrigroup.com/thrill-rides/scary-drop/) |
| Braking design target | < 5 g, peak ≥ 0.5 s after brake onset (eddy-current brake patent) | design | [US 6062350](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6062350) |
| Launch (shot) tower | ≈ 3.5 g at launch, then ≈ 1.5 s weightless, then 2.5 g, 2.0 g rebounds (Space Shot) | measured | [Mårtensson-Pendrill & Axelsson, "Science at the Amusement Park"](https://openjournals.library.sydney.edu.au/CAL/article/view/6134/6784) |
| Gx, Gy | small in normal operation (vertical-only motion) | – | – |

### 3.5 Pendulum rides (Giant Frisbee, Gyro Swing)
| Quantity | Value | Basis | Source |
|---|---|---|---|
| Peak +Gz (bottom of swing) | ≈ 4 g (Loke Gyro Swing, L = 24 m, 120°) | theory, "essentially consistent" with measured accelerometer data | [Pendrill & Modig 2018, Phys. Educ. 53 045017](https://iopscience.iop.org/article/10.1088/1361-6552/aac3cb) |
| −Gz (turning points, 120°) | N = −mg/2, i.e. −0.5 g "acting on the rider's shoulders" | theory | same |
| Coriolis contribution | up to ≈ 0.48 g at the lowest point (depends on seat position) | theory | same |
| Swing period | ≈ 13.2 s at 120° (9.8 s small-angle) | theory | same |
| Giant Frisbee (Huss, Nanjing) | +4.5 g, airtime −0.5 g, ≈ 110 km/h, 120° each side | manufacturer press | [EAP Magazin](https://www.eap-magazin.de/Article/New-Giant-Frisbee-Swinging-through-OCT-Happy-Valley-Nanjing.html) |
| Delirium (Kings Island Giant Frisbee) | up to 4.5 g | claimed | [Theme Park Archive](https://www.themeparkarchive.com/parks/kings-island/delirium) |

Duration of the −0.5 g phase near each turning point: about 1–2 s per half-cycle, repeated over the ride **[estimate, from the 13.2 s period]**.

### 3.6 Swing rides / Star Flyers
| Quantity | Value | Basis | Source |
|---|---|---|---|
| Horizontal (centripetal) | ≈ 1.3 g (Himmelskibet Star Flyer, 80 m, chain 8 m, swing angle ≈ 52°) | measured (accelerometer graph) | [Liseberg physics, Himmelskibet](https://physics.gu.se/LISEBERG/tivoli/himmelskibet/index.html) |
| Resultant along chain (seat +Gz) | ≈ √(1² + 1.3²) ≈ 1.64 g | derived | – |
| −Gz | none expected in normal operation: the seat aligns with the resultant | physics | [Liseberg Wave Swinger page](https://physics.gu.se/LISEBERG/eng/SLANGGUNGAN.html) |
| Vertical | only during start/stop of vertical travel (2.2 m/s lift) | measured | Himmelskibet page |

### 3.7 Spinning flat rides
| Quantity | Value | Basis | Source |
|---|---|---|---|
| Peak +Gz | 3 g (HUSS Enterprise) | database figure | [Wikipedia: Enterprise (ride)](https://en.wikipedia.org/wiki/Enterprise_(ride)) |
| Peak | up to 4 g (Take Off) | rider-reported | [DOD3](https://thedod3.com/5-lesser-known-huss-rides/) |
| −Gz | rides that invert or hold riders inverted (Top Spin type): up to −1 Gz sustained **[physics]**; no published measurements found | – | – |
| Gy | on spinning-gondola rides, centripetal loads act laterally for the rider; not quantified publicly | – | – |

### 3.8 Water slides
No published measured peak values were found. Limits are in ASTM F2376 and measurement uses ASTM F3493 (human subjects). One model of a vertical looped slide gives 2–3 × body weight **[theory]** ([Academia.edu paper](https://www.academia.edu/167332436/Mathematical_Modelling_of_Vertical_Looped_Water_Slide_Using_Matlab)). **RideBelt is not applicable:** slides have no seats or anchors, and tethering a rider in water creates entrapment and drowning hazards.

### 3.9 Daily-life comparison (for context only)
Allen et al. (1994, *Spine* 19:1285) measured brief everyday peaks: sneeze 2.9 g, cough 3.5 g, hop off a step 8.1 g, and plopping into a chair 10.1 g, with a 10.4 g single event reported elsewhere ([IAAPA "Understanding G-forces"](https://www.vekoma.com/public/files/understanding_g-forces_iaapa.pdf)). These are short impact spikes and should not be used as ride design values.

## 4. Preliminary design load cases, ejection direction (PRELIMINARY: pending engineer review)

Method: take the largest credible published or claimed −Gz for the class and round up to give at least about 1.5× margin **[estimate]**. Then check the sustained inverted case (−1 Gz) wherever the vehicle can stop upside down. These are **static-equivalent accelerations**. The dynamic factor for the restraint-failure snatch (REQ-L4 free travel) is applied separately per [load-analysis.md](../analysis/load-analysis.md) §1.

| Ride class | Highest −Gz found (basis) | Typical duration | Suggested design −Gz (estimate) | Other axes to check (estimate) | Sustained inverted case |
|---|---|---|---|---|---|
| Non-inverting coaster (airtime, ejector) | −1.3 g (design/claimed) | 0.2–1 s pops; floater sections up to several seconds | **−2.0 g** for ≤ 3 s | ±Gy 2.0 g; −Gx (forward on brakes) 1.5 g | no |
| Inverting coaster | ≈ 0 g at loop top (measured); −1 g if stopped inverted (physics) | inversions a few seconds; a stop can last minutes or longer | **−2.0 g** dynamic **and** −1.0 g sustained (REQ-H5 duration TBD) | ±Gy 2.0 g; ±Gx 2.0 g | **yes** |
| Launched coaster | top-hat airtime (unquantified); launch +Gx 1.7 g (into seat) | launch 2–5 s | **−2.0 g** | −Gx (braking/rollback, forward toward the lap bar) **2.0 g**; ±Gy 2.0 g | if the layout inverts |
| Drop tower, gravity drop | ≈ 0 g (no out-of-seat push) | free fall ≈ 3 s | **−1.0 g** (allows for brake chatter, rebound and launch-tower tops) | **+Gz 5 g braking** checks submarining and the center strap (REQ-H4, REQ-L8) | no |
| Drop tower, push-down / shot tower | ≈ −1 g (2 g down-push, derived); "up to 3 g" claim would be −2 g | 1–3 s | **−2.0 g** | +Gz 5 g braking or launch | no |
| Pendulum (≤ 120° swing) | −0.5 g (theory and manufacturer) | ≈ 1–2 s per turning point, cyclic (≈ 10–20 cycles per ride) | **−1.0 g**, cyclic (fatigue and abrasion at the RAS latch) | Coriolis/lateral 0.5 g → design ±Gy 1.0 g; +Gz 4.5 g | only for 360° pendulum types: treat as an inverting coaster |
| Swing ride / Star Flyer | none in normal operation | – | **−0.5 g** (gusts, stop transients) | resultant 1.64 g along the chain; outward Gy 1.5 g if the seat does not align | no |
| Spinning flat ride | unquantified; −1 g if it holds riders inverted | seconds to tens of seconds | **−1.5 g**, and −1.0 g sustained where inversion is possible | ±Gy 3 g (gondola spin) | type-dependent |
| Water slide | n/a | – | **Not applicable**; exclude from RideBelt rating | – | – |

Envelope suggestion for the first prototype rating **[estimate]**: design to **−2.0 Gz** plus **−1.0 Gz sustained inverted**, ±2 g lateral, and 2 g forward. That covers every class above except +Gz submarining checks. It matches the 2 g placeholder in load-analysis.md, so no change is needed there yet.

Example static load [derived]: m = 140 kg (see §5) × 2.0 g × 9.81 = **2.75 kN** total, shared by two tethers. Per REQ-L5 each tether alone must carry it.

Open items before these numbers can be used:
1. Buy F2291-26a and read the Section 6 −Gz, Gx and Gy envelopes and the restraint-class figure (Section 5). Replace the "highest found" column with the standard's limits: the ride itself is designed up to the standard's limit, not to published examples.
2. Buy ISO/TS 17929 (or EN 13814-1 Annex J) for the egg-graph combined limits.
3. Instrument rides ourselves (3-axis logger at 200 Hz or more, unfiltered, seat-mounted, plus chest-mounted). Phone apps such as phyphox and Ride Forces work for screening, but they smooth data and can drop samples ([phyphox forum](https://phyphox.org/forums/showthread.php?tid=1612)).
4. Treat short (< 200 ms) snatch and impact loads separately. F2291 does not cover them.

## 5. Rider mass assumptions

### 5.1 Population data
CDC/NCHS, *Anthropometric Reference Data for Children and Adults: United States, 2015–2018*, Vital Health Stat 3(46), Jan 2021, Table 5. These are measured NHANES weights, without shoes and in light examination clothing ([CDC Stacks 100478](https://stacks.cdc.gov/view/cdc/100478); [PDF](https://www.cdc.gov/nchs/data/series/sr_03/sr03-046-508.pdf)).

| Group (men, 2015–2018) | Mean | 50th | 90th | 95th |
|---|---|---|---|---|
| All men 20+ | 90.6 kg | 87.4 kg | 119.4 kg | **130.3 kg** (287.2 lb) |
| Heaviest age band, 30–39 | 94.4 kg | 89.7 kg | 123.8 kg | **139.9 kg** (308.5 lb) |
| Heaviest subgroup reported, non-Hispanic white men 20–39 | 91.6 kg | 86.7 kg | 122.7 kg | 137.3 kg |
| Women 20+ (Table 3) | 77.5 kg | 73.1 kg | 105.3 kg | 119.6 kg |

**The report has no 99th percentile** (its highest is the 95th). Any 99th-percentile figure would be an extrapolation and must be labelled as an estimate. Assuming a normal-like upper tail from the 90th and 95th points, the 99th percentile for men 20+ is roughly 150–160 kg **[estimate]**.

### 5.2 Ride weight limits (examples)
- Orlando FreeFall (Funtime drop tower): the manufacturer's manual gave a **130 kg (286 lb)** maximum ([ClickOrlando 2022](https://www.clickorlando.com/news/local/2022/03/29/new-records-show-orlando-freefall-has-weight-limit-as-state-continues-to-investigate-teens-death/)).
- DelGrosso Park: Rock Star **300 lb (136 kg) per seat**, Yo-Yo 216 lb (98 kg) per seat, Crazy Mouse 500 lb per vehicle ([DelGrosso](https://www.mydelgrossopark.com/amusement-park-rides/rock-star/)).
- Many major parks use **restraint fit** rather than a posted weight (e.g., Universal's Forbidden Journey has no maximum weight; the restraint must close) ([AJC](https://www.ajc.com/travel/how-big-too-big-some-theme-park-riders-fear-the-walk-shame/YN7JDzapFtPgi4cRAdjIPJ/)). Signage is not required unless the manufacturer's manual says so ([Fox 35](https://fox35orlando.com/news/state-senator-looking-to-take-action-to-make-amusement-rides-more-safe)).
- A forum post quotes the withdrawn F1159 as using a 170 lb adult design weight or 12 lb per inch of hip width, whichever is greater ([CoasterBuzz](https://coasterbuzz.com/Forums/PostLink/398020)). This is **unverified**.

### 5.3 Recommendation (preliminary)
- **Design rider mass m = 140 kg** for REQ-L2. This is the 95th percentile of the heaviest U.S. male age band (139.9 kg) and covers the all-ages 95th (130.3 kg) plus about 4 kg of clothing and harness **[estimate]**. It also exceeds the posted ride limits found (130–136 kg).
- **Upper rated user mass on the label: 140 kg.** Riders above this are outside the rating, even if the ride admits them by restraint fit.
- REQ-F1 asks for sizing to the 99th-percentile male. Sizing (girth) and mass rating are separate. If marketing wants the mass rating to reach about the 99th percentile, use **m = 160 kg [estimate]**, which raises loads by 14%.
- This replaces the 136 kg placeholder in load-analysis.md §1, after engineer review.

## 6. Sources not yet obtained (to buy or request)
- ASTM F2291-26a (Sections 5 and 6, Annex A1, Appendix X1).
- ISO/TS 17929:2014; EN 13814-1:2019+A1:2024 Annex J.
- Smith & Meaney 2002: per-ride traces (the paper gives only ranges).
- Pendrill & Rödjegård 2005 (Balder) and Burt & Pendrill 2020 (Gyldne Tårn): raw accelerometer files. Contact the authors.
- ASTM F2376 / F3493 (water slides), only if the scope ever changes.
