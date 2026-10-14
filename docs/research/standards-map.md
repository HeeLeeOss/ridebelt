# Standards Map (Phase 0)

> Get current editions from ASTM, CEN and ISO before relying on any clause. This map records **why** each standard matters. It does not quote their contents.
>
> "Current edition" was checked on 2026-10-14 against publisher and national-body listings (ASTM store, ANSI webstore, EVS/SIS/NSAI national stores, EUR-Lex). Standards change often, so re-check before citing in a certification file. Ride acceleration data and load cases are in [ride-acceleration-data.md](ride-acceleration-data.md).

## Amusement ride standards (the ride side)
| Standard | Current edition | Scope (exact title) | Relevance to RideBelt |
|---|---|---|---|
| ASTM F2291 | **F2291-26a** (active; superseded F2291-26, -25c, -25b, -25) ([ASTM](https://store.astm.org/f2291-26a.html)) | Standard Practice for Design of Amusement Rides and Devices | Section 5 (patron restraint, clearance envelope, containment; Annex A1) and Section 6 (acceleration limits; Appendix X1). Gives the **load cases** and restraint-class logic RAS must fit into. See "F2291 patron restraint notes" below |
| ASTM F1193 | **F1193-26** (active; F1193-25 now historical) ([ASTM](https://store.astm.org/f1193-25.html)) | Standard Practice for Quality, Manufacture, and Construction of Amusement Rides and Devices | Manufacturing quality for anchors built into seats |
| ASTM F770 | **F770-24** (active; revisions in progress: WK94128, WK95336 modification program) ([ASTM](https://store.astm.org/f0770-24.html)) | Standard Practice for Ownership, Operation, Maintenance, and Inspection of Amusement Rides and Devices | Operator procedures: checks, evacuation, and permission for rider-supplied equipment. A RAS retrofit would likely count as a modification under the proposed program |
| ASTM F1159 | **Withdrawn 2025** (last edition F1159-16e1; earlier F1159-11/-03a scope withdrawn 2020) ([ASTM](https://store.astm.org/f1159-16e01.html)) | Last title: Standard Practice for Design of Amusement Rides and Devices that are Outside the Purview of Other F24 Design Standards (Withdrawn 2025) | **Corrected:** this is not a current "legacy/general" design standard. It is withdrawn, so use F2291. Cite only for historical context (e.g., the old adult design weight; see ride-acceleration-data.md §5.2) |
| ASTM F24 committee | n/a | Amusement Rides and Devices (subcommittee F24.24 Design and Manufacture) | **Venue for proposing RAS** as a work item or annex. Open items to track: WK92171 (Class 4/5 restraint positioning and monitoring), the F2291 §7.1 / acceleration work items (impact events < 200 ms) |
| ASTM F2376 / F3493 | F2376 (water slide systems); F3493 (water slide rider acceleration test method). Editions not checked | Water slides | Only to document **why water slides are out of scope** |
| EN 13814-1 | **EN 13814-1:2019+A1:2024** (prEN 13814-1 revision in development) ([Genorma](https://genorma.com/en/standards/en-13814-1-2019-a1-2024)) | Safety of amusement rides and amusement devices — Part 1: Design and manufacture | EU equivalent of F2291. Informative **Annex J, Acceleration effects on passengers**. Excludes water slides |
| EN 13814-2 | **EN 13814-2:2019+A1:2024** ([EVS](https://www.evs.ee/en/evs-en-13814-2-2019-a1-2024-consolidated)) | Safety of amusement rides and amusement devices — Part 2: Operation, maintenance and use | EU equivalent of F770 |
| EN 13814-3 | **EN 13814-3:2019+A1:2024** (per EVS listing) | Safety of amusement rides and amusement devices — Part 3: Requirements for inspection during design, manufacture, operation and use | Inspection-body acceptance of RAS anchors on EU rides |
| ISO 17842-1 | **ISO 17842-1:2023** ([BSMD](https://bsmd.moic.gov.bh/store/standards/iso:pub:std:IS:73000/ISO%2017842-1:2023)) | Safety of amusement rides and amusement devices — Part 1: Design and manufacture | International harmonization (aligned with EN 13814) |
| ISO 17842-2 | **ISO 17842-2:2022** | Safety of amusement rides and amusement devices — Part 2: Operation and use | International harmonization |
| ISO 17842-3 | **ISO 17842-3:2022** (replaced the 2015 edition) ([ISO](https://www.iso.org/standard/73053.html)) | Safety of amusement rides and amusement devices — Part 3: Requirements for inspection during design, manufacture, operation and use | International harmonization; inspection under ISO/IEC 17020 |
| ISO/TS 17929 | **ISO/TS 17929:2014** (confirmed 2021; revision ISO/AWI 17929 registered Dec 2023, ISO/TC 254) ([SCC](https://scc-ccn.ca/standardsdb/standards/8158464)) | Biomechanical effects on amusement ride passengers | **Added.** Acceleration-duration envelopes (e.g., +Gz 6 g ≤ 1 s, 5 g ≤ 2 s; onset ≤ 15 g/s, per Pendrill & Eager 2020) and the combined-axis "egg graphs". Primary public basis for the load cases |

### F2291 patron restraint notes (relevant to a secondary restraint)
From secondary sources only; verify against the purchased F2291-26a:
- Restraints are assigned to **Class 1 to 5**, driven mainly by the **−Gz (out-of-seat) acceleration** the patron experiences. Higher −Gz means a higher class. The restraint-class chart is in Section 5 (older editions placed it at 6.3).
- **Class 5**, as quoted from F2291-20 by a student write-up and a blog table:
  - **Primary restraint:** one patron per restraint, automatic locking in a variable set of positions, external indication of restraint status for the operator, and **redundancy of the locking device**.
  - **Secondary restraint:** "Secondary restraints may be used in the absence of a locking redundancy." In the blog's table, a secondary restraint "should be independent of the primary restraint."
  - Sources: [mackenziegoldman.myportfolio.com](https://mackenziegoldman.myportfolio.com/ride-engineering-competition-double-ferris-wheel), [cavudw.com](https://cavudw.com/santas-sleigh/).
- A forum discussion reports a second belt added to meet the F2291-16 "secondary restraint in a Class 5 environment" requirement ([CoasterBuzz](https://coasterbuzz.com/Forums/PostLink/974006)). This is informal.
- Work item WK92171 proposes positioning and position-monitoring requirements for Class 4/5 restraints. If adopted, REQ-O4 (no interference with restraint sensing) becomes more important.
- **Implication for RAS:** F2291 already has the concept of an *independent* secondary restraint that substitutes for locking redundancy. RAS should be framed as that, in a load path independent of the primary restraint (REQ-A2). F2291 assumes the **manufacturer** designs and supplies the restraint, so rider-supplied equipment remains a gap (see below).
- F2291 acceleration limits address sustained accelerations (≥ 200 ms). Shorter impact events are outside the current limits, and a work item is open on this. RideBelt's arrest snatch load is such an event.

## Personal protective equipment standards (the wearable side)
| Standard | Current edition | Scope (exact title) | Relevance |
|---|---|---|---|
| EN 361 | **EN 361:2002** (revision prEN 361 rev abandoned 2017; harmonised under the PPE Regulation) ([iTeh](https://iteh.es/catalog/standards/cen/07c4e0e4-9f41-43f8-952c-c11939e8821e/en-361-2002), [genorma](https://genorma.com/en/standards/pren-361-rev-1)) | Personal protective equipment against falls from a height — Full body harnesses | Harness design and testing model |
| EN 813 | **EN 813:2024** (replaced EN 813:2008, withdrawn 2024-04-01; 2008 keeps presumption of conformity until the OJEU listing is updated) ([EVS](https://www.evs.ee/en/evs-en-813-2024)) | Personal fall protection equipment — Sit harnesses | Leg-loop and low-attachment model. **Corrected edition** |
| EN 12277 | **EN 12277:2015+A1:2018** ([SIS](https://www.sis.se/en/produkter/domestic-and-commercial-equipment-entertainment-sports/sports-equipment-and-facilities/outdoor-and-water-sports-equipment/ss-en-122772015a12018/)) | Mountaineering equipment — Harnesses — Safety requirements and test methods | Lighter-weight harness reference |
| EN 362 | **EN 362:2004** (harmonised; no revision found) ([EUR-Lex 2023/941](https://eur-lex.europa.eu/eli/dec_impl/2023/941)) | Personal protective equipment against falls from a height — Connectors | Connector classes, gate strength, and manual/automatic locking. **Corrected:** "triple-action" gates are a common product option, not a requirement of EN 362 or Z359.12. Both require deliberate multi-step opening for locking connectors (verify clause). RideBelt's double-action requirement (REQ-O2) is our own choice |
| ANSI Z359.12 | **ANSI/ASSP Z359.12-2019** ([ANSI blog](https://blog.ansi.org/?p=7109)) | Connecting Components for Personal Fall Arrest Systems | U.S. connector reference; source of the 16 kN (3,600 lbf) gate rating in REQ-O2 (verify clause) |
| EN 355 | **EN 355:2002** (harmonised; no newer edition) ([NSAI](https://shop.standards.ie/en-ie/standards/en-355-2002-345728_saig_cen_cen_790769/)) | Personal protective equipment against falls from a height — Energy absorbers | Energy-absorber test methods (RideBelt needs ride-specific limits) |
| ANSI Z359.13 | **ANSI/ASSP Z359.13-2013 (R2022)**, reaffirmed, not revised | Personal Energy Absorbers and Energy Absorbing Lanyards | U.S. absorber test methods |
| ANSI Z359.11 | **ANSI/ASSP Z359.11-2021** (referenced by Z359.1-2024 Fall Protection Code) ([ANSI blog](https://blog.ansi.org/ansi/ansi-assp-z359-1-2024-fall-protection-code/)) | Safety Requirements for Full Body Harnesses | U.S. harness reference |
| OSHA 1926.502(d) | Current CFR text | Fall protection systems criteria and practices | Precedent: body belts are not allowed for fall arrest |

## Process standards
| Standard | Current edition | Exact title | Use |
|---|---|---|---|
| ISO 12100 | **ISO 12100:2010** (no newer edition found; check iso.org for any revision project) | Safety of machinery — General principles for design — Risk assessment and risk reduction | Risk assessment method for the hazard analysis |
| IEC 60812 | **IEC 60812:2018** (Ed. 3.0; replaced the 2006 edition; EN IEC 60812:2018) ([IEC](https://webstore.iec.ch/publication/26359)) | Failure modes and effects analysis (FMEA and FMECA) | FMEA method |
| ISO 13849-1 / -2 | **ISO 13849-1:2023** (4th ed., replaced 2015); ISO 13849-2:2012 (edition not re-checked) | Safety of machinery — Safety-related parts of control systems — Part 1: General principles for design / Part 2: Validation | Only if the RAS "clipped-in" sensor feeds ride safety controls |

## Gaps (the opportunity)
- No current standard covers a **rider-supplied backup restraint** for amusement rides. F2291 Class 5 allows an *independent secondary restraint*, but only as part of the manufacturer's restraint system.
- No standard defines a **universal secondary anchor** on ride seats. RAS aims to fill this gap.
- F2291's acceleration limits do not cover impact events shorter than 200 ms (work item open). RideBelt's arrest loads need their own injury criteria (REQ-L3).
