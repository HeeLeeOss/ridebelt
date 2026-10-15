# Webbing and Stitching Materials Survey

> Status: research input (task `ridebelt-materials-001`) · License: CC BY 4.0 · Prepared with AI assistance (Claude Code)
>
> This is a literature and datasheet survey. Candidates are named **for prototype evaluation only**. Material choices are set in the DRAFT design specs (`ridebelt-design-001` and later) and are not released until the MVP gate ([GOVERNANCE.md](../../GOVERNANCE.md)). Values are typical published figures for **fibres or yarns**, not for finished webbing. Webbing strength depends on weave, width, finish and stitching, and must come from the webbing maker's test data plus our own tests (T-S1, T-E1, T-E2).

## 1. What RideBelt needs from webbing
| Need | Requirement | Why it matters for material choice |
|---|---|---|
| High strength in the load path | REQ-L2: MBS ≥ 30 kN per tether path (5 × 6 kN) | Tethers, belt and sewn joints must reach this with margin after ageing |
| **Low stretch** | REQ-L4: slack ≤ 2 cm and total excursion ≤ 10 cm | The arrest model shows rider excursion and peak load rise with slack and compliance ([load-analysis.md](../analysis/load-analysis.md)). Stretchy webbing adds excursion |
| UV, water, sweat and chlorine durability | REQ-D1: ≥ 80% strength retained after UV, washing and wet or chlorinated exposure | Gear is worn outdoors and gets wet in rain or sweat. Capsizable water rides are excluded (REQ-H6), but splash exposure remains |
| Abrasion and edge resistance | T-S4 edge abrasion; FMEA "tether cut or abraded" | Contact with seat edges and buckles |
| Inspectability and service life | REQ-D3, `ridebelt-inspection-001` | Colour change is **not** a reliable indicator of strength loss (UIAA, below) |

### A ready-made performance benchmark: FMVSS 209 seat-belt webbing
The US standard for vehicle seat-belt webbing (49 CFR 571.209, S4.2) sets requirements that map closely onto RideBelt's. They are a useful **minimum** benchmark for a candidate webbing ([49 CFR 571.209, Cornell LII](https://www.law.cornell.edu/cfr/text/49/571.209)):

| FMVSS 209 webbing requirement | Value | RideBelt comparison |
|---|---|---|
| Breaking strength, Type 1 (pelvic) belt | ≥ 26,689 N | Close to, but **below**, RideBelt's 30 kN MBS target |
| Elongation, Type 1 | ≤ 20% at 11,120 N | A useful ceiling; RideBelt's excursion limit favours lower stretch |
| Resistance to abrasion | ≥ 75% of required breaking strength after abrasion | Compare REQ-D1 (≥ 80%) |
| Resistance to light (carbon-arc exposure) | ≥ 60% of pre-exposure strength | **Weaker than REQ-D1 (≥ 80%)**, so RideBelt needs better UV performance than seat-belt webbing guarantees, or a lower de-rated design strength |
| Resistance to micro-organisms | ≥ 85% of pre-exposure strength | Relevant to sweat and wet storage |

## 2. Fibre and yarn properties
Tenacity conversions use 1 g/den = 8.83 cN/tex.

| Property | Polyester (PET), high tenacity | Nylon 6,6, high tenacity | UHMWPE (e.g., Dyneema/Spectra) | Para-aramid (e.g., Kevlar) |
|---|---|---|---|---|
| Tenacity | up to **84 cN/tex** ([Swicofil PET HT](https://www.swicofil.com/commerce/products/polyester/165/hightenacity)) | up to **82 cN/tex** ([Swicofil PA6.6 HT](https://www.swicofil.com/commerce/products/polyamide66/238/hightenacity)) | **28.0–38.0 g/den ≈ 247–336 cN/tex** ([Fiber-Line UHMWPE datasheet](https://www.avient.com/sites/default/files/2021-06/fl.us-.datasheet-uhmwpe.pdf)) | **23.0 g/den ≈ 203 cN/tex** ([Fiber-Line para-aramid datasheet](https://www.fiber-line.com/uploads/pdf%20US/fl.us.datasheet-kevlar-para-aramid.pdf)) |
| Elongation at break | **13–24%** (Swicofil PET HT) | **17.5–48%** (Swicofil PA6.6 HT) | **3.1–3.6%** (Fiber-Line) | **3.5%** standard modulus (Fiber-Line) |
| Moisture regain / water uptake | "Typically < 1%" by weight ([National Webbing technical guide](https://www.nationalwebbing.com/nylon-webbing-articles/nylon-webbing/technical-guide-webbing-materials-312.html)) | "Can be several %" (National Webbing) | < 0.1% (Fiber-Line) | 5.0% at 55% RH (Fiber-Line) |
| Wet strength | No material wet-strength loss reported in these sources | About **10–15% loss** reported for wet nylon web slings, recovered on drying ([Unirope chemical-resistance guide](https://www.unirope.com/?p=12102)); a 2017 BYU undergraduate study tested tubular nylon webbing in wet and cold conditions, noting that makers' ratings are dry-tested ([BYU JUR](https://scholarsarchive.byu.edu/jur/vol2017/iss1/37); results not checked here, as only the abstract was read). Quantitative evidence is thin | Negligible water uptake (Fiber-Line) | Absorbs up to 5% moisture (Fiber-Line) |
| Heat | — | — | **Melts at about 147 °C**, low for a load-bearing textile (Fiber-Line). Friction heat in a sliding or knotted joint is a known failure route | No melting; **decomposes at 425–480 °C** (Fiber-Line) |
| Creep | — | — | **1.7–5.0% at 40–58% of break load**, "susceptible to creep" (Fiber-Line) | < 0.03% (Fiber-Line) |
| UV | **Best of the group:** least affected in the UIAA canyoning-harness ageing study ([UIAA safety alert](https://www.theuiaa.org/uiaa-safety-alert-canyoning-harnesses/)). In WSTDA outdoor tests (reported by Unirope) loss levelled off at **about 30%** after the first 12 months ([Unirope](https://unirope.com/sling/exposure-to-sun-and-uv-light/)) | **Steady loss**: WSTDA tests found loss continuing over 36 months, reaching **50–60%** for some samples (Unirope). In the UIAA study some polyamide straps fell **from 30 kN to 3 kN after 2,000 h** of ageing | Fiber-Line calls the fibre "UV stable", **but** Dyneema/polyamide straps were the *most* affected in the UIAA study (**20 kN → 1 kN** in the worst cases) | "Suffers from UV degradation, which causes strength loss and discoloration" (Fiber-Line) |
| Chlorine / bleach | No quantitative public data found | No quantitative public data found | No quantitative public data found | Degrades in some acids and bases; sodium hydroxide named (Fiber-Line) |
| Relative cost | Cost index 0.90–1.05 vs nylon 1.00 (National Webbing) | 1.00 (National Webbing reference) | **Much higher [estimate]**, specialist fibre | **Much higher [estimate]**, specialist fibre |

**Gaps:** no source found gives quantitative **chlorine** effects for any of these webbings. That has to come from T-E2 testing. Abrasion data in public sources is qualitative only; National Webbing doesn't quantify it, and Fiber-Line rates it in symbols.

### Reading the UV evidence carefully
- The UIAA results come from accelerated ageing (up to 2,000 h at up to 70 °C) on canyoning-harness straps, not ride gear. They show that **a fibre's UV reputation does not guarantee a finished strap's UV performance**: finishes, blends and constructions matter.
- The UIAA also notes that **colour change did not reliably indicate strength loss**. Inspection criteria (`ridebelt-inspection-001`) shouldn't rely on fading alone, and service-life limits (REQ-D3) are needed.

## 3. Stitching and sewn joints
### Joint efficiency
- **Joint efficiency** is the strength of a sewn joint divided by the strength of the unsewn material. NASA's parachute work defines a *standard* efficiency that subtracts one standard deviation of the joint test results. Across 92 CPAS seam and joint tests, mean efficiency exceeded standard efficiency by **1–10% (average 4%)** ([Mollmann, "Strength Variation of Parachute Joints", NASA NTRS 20170003951](https://ntrs.nasa.gov/api/citations/20170003951/downloads/20170003951.pdf)). RideBelt should use the **standard (minus one SD) efficiency** in its design factor, and test enough samples to estimate the SD (T-S1).
- The same paper notes that actual material is often stronger than its minimum rating, "often by as much as 20%". Efficiencies must therefore be calculated against **tested control samples from the same lot**, not catalogue minimums, or they will be misleading.

### Stitch patterns
| Pattern | What the sources say | Source |
|---|---|---|
| **W and diamond patterns** | Among the most efficient patterns for load-bearing webbing in Sailrite's lab tests | [Sailrite: How to Sew Webbing Loops](https://www.sailrite.com/How-to-Sew-Webbing-Loops) |
| **Bar tacks** | Also performed well in Sailrite's tests, attributed to the amount of stitching. They are the standard industrial method for high-load joints, and hand sewing can't match commercial bar-tacking | Sailrite; [Practical Sailor](https://www.practical-sailor.com/sails-rigging-deckgear/is-hand-stitched-nylon-webbing-strong-enough/) |
| **W-W vs. box-X** | The FAA Parachute Rigger Handbook says a W-W pattern is stronger than a box-X; stitch pattern, stitch length and re-sewing all affect strength | [FAA Parachute Rigger Handbook (via avstop)](http://avstop.com/ac/prh/chapter2_20.html) |
| **Straight rows** | For hand-sewn joints, closely spaced straight rows gave the strongest joins, and the pattern mattered little except at the ends | Practical Sailor |

**No reliable published efficiency percentages** were found for bar-tack vs. W-box joints in webbing like RideBelt's. Vendor pages quote figures without sources, and they aren't used here. RideBelt's joint efficiencies must be **measured** on the chosen webbing, thread and pattern (T-S1), using the NASA standard-efficiency method.

### Thread
- Use thread of the **same fibre family or one more UV-stable than the webbing** (e.g., polyester webbing with polyester thread), so the stitching doesn't age faster than the webbing it holds. This is reasoned from the UV evidence above **[assumption to verify in T-E1]**.
- Use **contrasting thread colour** at load-bearing joints so worn or broken stitching is visible during inspection (FMEA "bar-tack failure" mitigation).

## 4. Candidates for prototype evaluation
| Role | Candidate for evaluation | Rationale | Watch-outs to test |
|---|---|---|---|
| **Tethers and belt load path** | **High-tenacity polyester webbing**, seat-belt grade or better | Best UV retention of the group; very low water uptake; moderate stretch (lower than nylon); FMVSS 209 webbing is an established, widely produced benchmark | Must exceed FMVSS 209's 60% light-retention level to meet REQ-D1 (≥ 80%); confirm 30 kN tether MBS and elongation in T-S1 |
| Alternative load path | Nylon 6,6 webbing | Strong, tough, energy-absorbing | Higher stretch (adds excursion, REQ-L4); steady UV loss over years; wet-strength loss reported. **Not preferred** for outdoor ride use |
| Possible low-stretch element (e.g., inside a sleeve) | UHMWPE webbing or tape | Very high strength and very low stretch could reduce excursion | **Low melting point (about 147 °C)**, creep, poor UV result for blended straps in the UIAA study, knot sensitivity. Use only fully protected, never knotted, with a separate creep check |
| Not recommended for exposed parts | Para-aramid | Very strong, low stretch, heat resistant | UV degradation; moisture uptake. Only inside a UV-blocking cover, if at all |
| **Thread** | Bonded polyester, contrasting colour | Matches polyester webbing's UV behaviour; visible for inspection | Verify joint efficiency and UV retention in T-S1 and T-E1 |
| **Sewn joints** | Machine bar-tack or W-pattern, chosen by test | Patterns the sources rate most efficient | Measure standard (minus one SD) efficiency on the actual webbing and thread |

## 5. Suppliers and publishers of specifications
| Source | What it publishes | Notes |
|---|---|---|
| [Swicofil](https://www.swicofil.com/commerce/products/polyester/165/hightenacity) | Yarn tenacity, elongation and shrinkage ranges for PET and PA6.6 high-tenacity yarns | Yarn, not webbing |
| [Fiber-Line (Avient)](https://www.avient.com/sites/default/files/2021-06/fl.us-.datasheet-uhmwpe.pdf) | Datasheets for UHMWPE and para-aramid processed fibres | Processor datasheets; brand-specific (Dyneema, Kevlar) values should be confirmed with the fibre producers |
| [National Webbing Products](https://www.nationalwebbing.com/nylon-webbing-articles/nylon-webbing/technical-guide-webbing-materials-312.html) | Qualitative webbing comparison and a relative cost index | Vendor guide; no tensile values |
| FMVSS 209 webbing makers | Seat-belt webbing certified to [49 CFR 571.209](https://www.law.cornell.edu/cfr/text/49/571.209) | The closest regulated product; request their test reports |

Purchase decisions belong to `ridebelt-hardware-001` (hardware survey) and the design specs. This survey names no preferred vendor.

## 6. Limitations
- Fibre and yarn values are **not webbing values**. Weave, width, finish and joints change them.
- UV evidence comes from slings and canyoning straps under particular exposures. Ride-gear exposure (outdoor storage, daily sun) must be tested (T-E1).
- Wet-strength evidence for nylon is thin (one vendor figure; the BYU paper's results weren't read), and no chlorine data was found.
- Vendor pages are used only where stated, and their figures are typical, not guaranteed.

## Sources
- 49 CFR 571.209 (FMVSS 209), Cornell LII: https://www.law.cornell.edu/cfr/text/49/571.209
- Swicofil, Polyester PET high tenacity: https://www.swicofil.com/commerce/products/polyester/165/hightenacity
- Swicofil, Polyamide 6.6 high tenacity: https://www.swicofil.com/commerce/products/polyamide66/238/hightenacity
- Fiber-Line, UHMWPE datasheet (hosted by Avient): https://www.avient.com/sites/default/files/2021-06/fl.us-.datasheet-uhmwpe.pdf
- Fiber-Line, para-aramid datasheet: https://www.fiber-line.com/uploads/pdf%20US/fl.us.datasheet-kevlar-para-aramid.pdf
- National Webbing Products, Technical Guide to Webbing Materials: https://www.nationalwebbing.com/nylon-webbing-articles/nylon-webbing/technical-guide-webbing-materials-312.html
- UIAA Safety Alert: Canyoning Harnesses: https://www.theuiaa.org/uiaa-safety-alert-canyoning-harnesses/
- Unirope, Exposure to Sun and UV-Light (WSTDA results): https://unirope.com/sling/exposure-to-sun-and-uv-light/
- Unirope, chemical resistance of slings: https://www.unirope.com/?p=12102
- BYU Journal of Undergraduate Research (2017), nylon webbing study: https://scholarsarchive.byu.edu/jur/vol2017/iss1/37
- Mollmann, C., "Strength Variation of Parachute Joints", NASA NTRS 20170003951: https://ntrs.nasa.gov/api/citations/20170003951/downloads/20170003951.pdf
- Sailrite, How to Sew Webbing Loops: https://www.sailrite.com/How-to-Sew-Webbing-Loops
- Practical Sailor, Is Hand-stitched Nylon Webbing Strong Enough?: https://www.practical-sailor.com/sails-rigging-deckgear/is-hand-stitched-nylon-webbing-strong-enough/
- FAA Parachute Rigger Handbook, chapter 2 (via avstop): http://avstop.com/ac/prh/chapter2_20.html
