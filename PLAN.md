# PLAN — ridebelt

> Status: Draft · Version: 0.1.0 · Last updated: 2026-10-14 · Maintainer: @jdev1977 · Lane: donated · License: CC BY 4.0 (content), MIT (code)
>
> ⚠️ Safety-critical project. All design content is **DRAFT and not for use** until the MVP review gate. See [SAFETY-NOTICE.md](SAFETY-NOTICE.md).

## Executive summary
Riders keep dying or being badly hurt when an amusement ride's restraint fails, isn't locked, or doesn't fit them. RideBelt is an **open design for an optional, rider-worn backup restraint**: a low hip belt with short, self-retracting tethers that latch into a **free, open anchor standard (RAS)** built into ride seats. It also includes a wrap strap for older rides. The project publishes the research, requirements, safety analysis, load models, anchor standard and test methods openly. The goal is that ride manufacturers, parks, standards bodies (ASTM F24) and gear makers can adopt it, once a credentialed engineer has reviewed it and it has been tested.

## Problem & beneficiaries
- **Problem:** see [docs/research/incidents.md](docs/research/incidents.md), which covers 26 incidents from 10 countries. Restraints that were never locked or checked, riders who didn't fit the restraint, and mechanical restraint failures account for most ejections. In about 35% of the reviewed cases a seat-anchored backup would plausibly have helped, and in another 35% partly.
- **Beneficiaries:** amusement-ride riders, especially riders outside the restraint's design range (large or small bodies, limb differences) and children; park operators; ride manufacturers; ride inspectors and standards committees.
- **Requestor:** TO BE SECURED (target: a ride manufacturer, park operator or ASTM F24 member who commits to review and pilot).

## Goals and non-goals
**Goals**
1. An open, reviewed **RAS anchor standard**: placement, strength, latch interface, release under load, clipped-in sensing, and conformance tests.
2. An open **wearable design**: Hip Belt, clip-on Shoulder Module, one-piece Integrated Harness (belt and shoulders sewn together), Convertible Center Strap, self-retracting tethers, Wrap Strap.
3. Open **analysis and test methods**: arrest model, load cases, bench and dynamic test procedures.
4. Pass the **MVP review gate**, then propose RAS to **ASTM F24**.

**Non-goals**
- Selling products, filing patents, or charging for the standard.
- Replacing or modifying any ride's primary restraint.
- Protecting against structural failures or collisions (out of scope, and stated openly).
- Rider-side use before certification. The project gives **no** guidance for wearing anything on rides today.

## Success metrics (outcomes)
- MVP gate passed: credentialed sign-off recorded in `review/`.
- RAS v1.0 published; at least one manufacturer or operator review on record.
- RAS submitted to ASTM F24 as a work item or annex.
- At least one third-party lab builds and tests to the published test methods.

## Scope
In scope: everything under [docs/](docs/). Out of scope for now: physical manufacturing, the certification-mark program (needs legal counsel), and the post-launch features in [docs/business/post-launch.md](docs/business/post-launch.md), which stay a future vision until RAS is adopted.

## Solution approach & architecture
| Area | Document |
|---|---|
| Requirements (numbered, testable) | [docs/requirements.md](docs/requirements.md) |
| Hazard analysis & FMEA | [docs/safety/](docs/safety/) |
| Concepts, modules, connector trade study | [docs/design/concepts.md](docs/design/concepts.md) |
| Latch, release & sensor | [docs/design/ras-latch.md](docs/design/ras-latch.md) |
| Anchor standard | [docs/standard/RAS-v0.1.md](docs/standard/RAS-v0.1.md) |
| Load cases & arrest model | [docs/analysis/](docs/analysis/), [docs/research/ride-acceleration-data.md](docs/research/ride-acceleration-data.md) |
| Test plan & traceability | [docs/testing/test-plan.md](docs/testing/test-plan.md) |

Key numbers (preliminary): 140 kg design rider; −2.0 g ejection rating plus −1.0 g sustained; 6 kN design load per tether → 30 kN MBS; slack ≤ 2 cm; 4 kN energy absorber; tethers at 45–75°; release under a 2 kN load.

## Data, licensing & compliance
- Content: CC BY 4.0 ([LICENSE](LICENSE)). Code: MIT ([LICENSE-CODE](LICENSE-CODE)). **No patents will be filed**, and publication serves as defensive publication ([docs/business/licensing-model.md](docs/business/licensing-model.md)).
- Third-party patents still apply. Contributors must respect the design-arounds in [docs/research/patentability-fto.md](docs/research/patentability-fto.md): no wireless lock or unlock, no leg-flap or vest-plus-leg-restraint harness, no spring-plate anchor sensor.
- Standards: never copy text from paid standards (ASTM, EN, ISO). Cite clause numbers and summarize only.
- Sources: every factual claim cites a source. Incident entries carry a verification status.

## Quality, review & risk gates
See [GOVERNANCE.md](GOVERNANCE.md). In brief: low and medium tasks are reviewed by the maintainer. High-risk (safety-critical) tasks merge **only as DRAFT** content with the banner intact. **No content is RELEASED, and no person wears any prototype, until a credentialed engineer signs off at the MVP gate.**

## Roadmap & milestones
| Milestone | Content | Exit criteria |
|---|---|---|
| **M0 — Foundation** | Repo, governance, reviewer recruitment, evidence base (incidents, acceleration data) | MVP-gate engineer identified; incident and acceleration datasets verified |
| **M1 — Draft design package** | Arrest model v2, RAS v0.2, test methods, ops and rescue guide, application-guide template, CAD | All safety docs complete as DRAFT; traceability check passes |
| **M2 — Bench evidence** *(human/lab)* | Prototype parts, bench tests, sled tests with ATD | Results recorded under `docs/testing/` |
| **MVP gate** | Credentialed review of the whole package plus results | Sign-off in `review/`; content moves to RELEASED |
| **M3 — Adoption** | ASTM F24 proposal, manufacturer pilot, certification program | Work item accepted; pilot agreed |

## Work breakdown
See [TASKS.md](TASKS.md) and [tasks/](tasks/).

## Governance, roles & stakeholders
[GOVERNANCE.md](GOVERNANCE.md) · stakeholders: [docs/business/stakeholders.md](docs/business/stakeholders.md).

## Dependencies & integrations
ASTM F2291-26a and EN 13814 (paid standards, to be bought by the maintainer); an ATD sled-test lab; a ride manufacturer for seat geometry.

## Risks & mitigations
| Risk | Mitigation |
|---|---|
| Someone builds and uses unreviewed designs | Safety notice, DRAFT banners on every safety doc, no "how to wear it today" content, MVP gate |
| AI-generated engineering errors | All safety content DRAFT until credentialed review; model assumptions flagged; traceability checks |
| No credentialed reviewer found | Recruitment task M0; intake-halt rule (nothing released without one) |
| Third-party patent conflict | FTO design-arounds; counsel review before any manufacture |
| Product liability for publishing | CC BY "as is" terms, safety notice, counsel review (open item) |

## Security & privacy
The core project handles no personal data. The rider-ID ideas in post-launch are out of scope until adoption, and would then need a privacy impact assessment.

## Sustainability & maintenance
Open standard, maintained here until it is accepted by ASTM F24. After that, the standard is maintained by the committee, and this repo keeps the reference designs and test methods.

## Open questions
1. Who will serve as the credentialed MVP-gate reviewer?
2. Who should hold the "RAS-certified" certification mark (a new nonprofit, or an existing standards or testing body)?
3. Are F2291-26a's −Gz limits above our −2.0 g rating for any ride class?

## References
[docs/research/](docs/research/) (incidents, standards, acceleration data, patent and FTO review).

## Review sign-off
| Gate | Reviewer | Date | Record |
|---|---|---|---|
| MVP gate | TO BE SECURED | — | `review/` |
