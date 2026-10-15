# Sizing System: Hip Belt and Integrated Harness (v0.1)

> 🚧 **DRAFT: not reviewed by a qualified engineer; not for use.** Not released until the MVP review gate. See [SAFETY-NOTICE](../../SAFETY-NOTICE.md).

Task `ridebelt-sizing-001` · License: CC BY 4.0 (text), MIT ([sizing/size_chart.py](sizing/size_chart.py)) · Prepared with AI assistance (Claude Code)

## 1. Requirement and basis
- **REQ-F1** (as updated by `ridebelt-requirements-003`): sizes shall fit the **1st to 99th percentile of both sexes** for hip and waist girth, thigh girth and torso length. (This task's original text said "5th-percentile female to 99th-percentile male". The current REQ-F1 is stricter and is used here.)
- **REQ-F3:** a fit check shall be possible in under 10 s.
- **Data:** [research/anthropometry-adult.md](../research/anthropometry-adult.md). Belt girth uses **NHANES 2021–2023** hip circumference (US civilians, survey-weighted), because the Hip Belt sits low on the pelvis. Harness torso lengths use **ANSUR II**, since NHANES has no torso-length measures.
- **Every percentage below is reproducible** with `python docs/design/sizing/size_chart.py <data_dir>`, using the data files listed in the anthropometry document.

### Assumptions (for engineer review)
| ID | Assumption | Value | Why it matters |
|---|---|---|---|
| SZ-A1 | Clothing allowance added to measured hip circumference | 4 cm | The belt is worn over clothing; heavier clothing shifts riders up a size |
| SZ-A2 | Adjustment range of one belt size | 20 cm | A semi-rigid, contoured belt can't keep its shape (REQ-L6, REQ-F4) over a much wider range; to be confirmed in prototype fit work |
| SZ-A3 | **Overlap between adjacent sizes** | **≥ 4 cm** (the stated margin) | A rider near a size boundary fits both sizes and isn't forced to the end of an adjuster |
| SZ-A4 | Shoulder-strap path = front torso length (sitting) + back torso length + shoulder arc | arc 10 cm | Estimates the strap length the Integrated Harness must reach |
| SZ-A5 | Standing girths approximate seated girths at belt height | — | NHANES measures standing; seated soft-tissue spread may need extra range (to be measured in T-F2, after the MVP gate) |

## 2. Hip Belt size chart (proposed)
Five sizes, each with 20 cm of adjustment and 4 cm of overlap with its neighbours, spanning **82–166 cm** of fit girth (hip circumference plus clothing).

### Coverage (NHANES 2021–2023, adults 18+, survey-weighted)

| Size | Adjustment range (cm, over clothing) | Fits (all adults) | Fits (men) | Fits (women) |
|---|---|---|---|---|
| XS | 82–102 | 25.3% | 27.3% | 23.3% |
| S | 98–118 | 61.6% | 68.2% | 55.3% |
| M | 114–134 | 26.6% | 22.7% | 30.4% |
| L | 130–150 | 9.0% | 5.2% | 12.6% |
| XL | 146–166 | 2.4% | 1.6% | 3.1% |
| **All sizes** | 82–166 | 99.6% | 99.9% | 99.4% |
| Below smallest | < 82 | 0.1% | 0.0% | 0.1% |
| Above largest | > 166 | 0.3% | 0.1% | 0.5% |

Fit girth = NHANES hip circumference + 4 cm clothing allowance; n = 5957; weighted P1/P5/P50/P95/P99 = 88.3 / 93.2 / 109.0 / 139.0 / 155.2 cm. Sizes overlap, so a rider near a boundary fits two sizes and the per-size shares sum to more than the total.

**Result:** the five sizes fit **99.6% of US adults** (99.9% of men, 99.4% of women), which meets REQ-F1's 1st-to-99th-percentile target for both sexes. The rider P1 (88.3 cm) and P99 (155.2 cm) fit girths both sit well inside the 82–166 cm span. About 0.5% of women and 0.1% of men are above the largest size. Covering them would need an XXL (about 162–182 cm), which this draft leaves as an open question.

**Notes**
- **Most riders are S or M:** S fits about 62% and M about 27% of adults. Rental fleets should stock in roughly that proportion; the per-size shares above give a starting mix.
- Sizes are **the same for both sexes**: the belt is fitted by girth, not by sex.
- Each size's tether attachment points and position marker (REQ-F4) must stay in the correct place at both ends of its adjustment range. That is a reason not to widen SZ-A2 without prototype evidence.

## 3. Integrated Harness sizing
The Integrated Harness uses the **same five belt sizes** for its hip belt, plus **one shoulder-strap range** for every size.

### Shoulder-strap path length

| Sex | n | P1 | P5 | P50 | P95 | P99 | Inside strap range |
|---|---|---|---|---|---|---|---|
| M | 4082 | 85.2 | 88.5 | 96.3 | 105.1 | 109.5 | 100.0% |
| F | 1986 | 77.9 | 81.0 | 87.9 | 95.9 | 99.6 | 99.9% |

Strap path = waist front length (sitting) + waist back length + 10 cm shoulder arc (ANSUR II, cm). Strap adjustment range 76–116 cm. ANSUR II is a military sample, so upper percentiles are lower bounds for civilians.

**Proposal:** shoulder-strap path adjustment **76–116 cm** (40 cm in total), provided by **two adjusters per strap of about 20 cm each**, one at the front and one at the back. This fits 100% of ANSUR II men and 99.9% of ANSUR II women, from the female P1 (77.9 cm) to the male P99 (109.5 cm) with about 6 cm to spare.

**Caveats**
- ANSUR II under-represents large bodies, and a large abdomen or chest lengthens the strap path. The civilian upper end may exceed 116 cm. **Open item:** confirm with civilian torso data or fit trials, and consider a "long strap" variant if needed.
- One strap range for every belt size keeps fleet stock simple, but it means a short rider with a large girth (or the reverse) is fitted correctly. A separate strap size per belt size would leave such riders out.
- The design rules in [concepts.md](concepts.md) still apply: torso fit comes from **strap-length buckles, not a vest height adjuster**, and there are no leg flaps or loops (FTO design-around). The neck-zone clearance (REQ-H1) must hold at both ends of the strap range, for the smallest and largest riders. That check belongs to `ridebelt-design-002`.

## 4. Fit-check method (REQ-F3, under 10 s)
This is a **design specification for built-in fit-check features**. It is not instructions for use: nobody may wear RideBelt before the MVP gate. The time budget below is an estimate to validate in T-F3, after the MVP gate.

| Step | Built-in feature | What the operator or wearer confirms | Time budget |
|---|---|---|---|
| 1 | **Size-range window** on each belt adjuster: a coloured band visible only while the adjuster is inside its rated range | The adjuster isn't at or beyond either end of its range (otherwise use the next size) | ≈ 2 s |
| 2 | **Position marker** at the pelvic bones (REQ-F4) | The belt sits low on the pelvis, not at the waist | ≈ 3 s |
| 3 | **Snugness gauge tab**: a stiff, flat tab of defined thickness (about two fingers, value TBD) sewn to the belt's inner edge | The tab must *not* slide between belt and body. This turns the "two-finger rule" into a repeatable, objective check | ≈ 3 s |
| 4 | **Size and module label** (and tag, REQ-T3) at the buckle; on the Integrated Harness, a sternum-strap marker band | The right product and modules for the ride class (REQ-H4); the sternum strap is in its marked band | ≈ 2 s |
| | | **Total** | **≈ 10 s (target < 10 s)** |

If steps 1 to 3 can be confirmed in a single look from the platform, the check could fall well under 10 s. That is a question for the T-F3 protocol (`ridebelt-testmethods-004`).

## 5. Open questions
1. Is a 20 cm range (SZ-A2) achievable for a contoured, semi-rigid belt? Prototype fit work is needed (mannequins before the MVP gate; people only after it).
2. Should there be an **XXL** for the 0.3–0.5% above 166 cm?
3. Is the 4 cm clothing allowance (SZ-A1) enough for winter clothing at outdoor parks?
4. Civilian torso-length data for the large-body end of the harness strap range.
5. Youth sizing is **out of scope**. See [research/anthropometry-youth.md](../research/anthropometry-youth.md): many children have waists below the XS range. That is input to REQ-F2, not a youth size.

## 6. Traceability
| Requirement | How this document addresses it | Verified by |
|---|---|---|
| REQ-F1 | Five belt sizes fit 99.6% of adults; one strap range fits 99.9–100% of the ANSUR II torso range | T-F2 (post-MVP fit trials) |
| REQ-F3 | Four-step built-in fit check, ≈ 10 s budget | T-F3 |
| REQ-F4 | Position marker included in the fit check | T-F3 |
