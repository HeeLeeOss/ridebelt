# Reviewer Recruitment Plan: MVP-gate Safety Engineer and Advisory Reviewers

> Status: Draft · Task: `ridebelt-reviewer-001` · License: CC BY 4.0 · Prepared with AI assistance
>
> This plan fills the roles defined in [GOVERNANCE.md](../../GOVERNANCE.md). Under the intake-halt rule, **nothing is released and no person wears a prototype until a named, credentialed MVP-gate Safety Engineer has signed off.** Recruiting that person is the project's critical path.

## 1. Roles to fill
| Role (GOVERNANCE.md) | Blocking? | Number sought | Core qualification |
|---|---|---|---|
| MVP-gate Safety Engineer | **Yes** (release, human wear) | 2 (primary + second reviewer for release-under-load and rescue content) | Licensed Professional Engineer (or national equivalent) with amusement-ride or occupant-restraint/fall-protection experience |
| Standards & Test-Methods Reviewer | No (advisory) | 1 | Test-lab or standards-committee experience (ASTM F24, ANSI Z359, CEN TC 152 or similar) |
| Legal counsel | No (advisory) | 1 | Product liability, certification marks, patents/FTO |

## 2. Candidate pools
Organisations and public roles only. No private individuals are named. Approach each through its **public** channels: committee membership, published contact forms, member directories that allow it, and conference sessions.

| # | Pool | Why it fits | Best for | Public link |
|---|---|---|---|---|
| 1 | **ASTM Committee F24 on Amusement Rides and Devices** | The standards body for ride design (F2291) and operation (F770). Members include ride engineers, inspectors, operators, manufacturers, consumer advocates and government officials, and the committee meets twice a year. RAS is meant to be proposed here after the MVP gate | Safety Engineer; Standards Reviewer | [astm.org/committee-f24](https://www.astm.org/committee-f24) |
| 2 | **NAARSO** (National Association of Amusement Ride Safety Officials) | Trains and certifies amusement ride inspectors in North America; its network includes engineers who know restraint failures in the field | Safety Engineer (referrals); field-practice review | [naarso.com](https://www.naarso.com) |
| 3 | **AIMS International** (Amusement Industry Manufacturers & Suppliers) | Runs ride safety training and certification for maintenance and operations, and connects manufacturers' engineering staff | Safety Engineer (referrals); manufacturer perspective | [aimsintl.org](https://www.aimsintl.org) |
| 4 | **IAAPA** (International Association of Amusement Parks and Attractions) | Global industry association for parks and attractions, with safety programs and committees | Referrals; operator review; later "requestor" for the project | [iaapa.org](https://www.iaapa.org) |
| 5 | **Third-party ride certification bodies**, e.g. TÜV SÜD's amusement ride services | Accredited engineers who inspect, test and certify rides to EN 13814; potential independent reviewers and the eventual certification route | Safety Engineer; Standards & Test-Methods Reviewer | [tuvsud.com — amusement rides & theme parks](https://www.tuvsud.com/en-us/amusement-rides-theme-parks) |
| 6 | **ADIPS** (UK Amusement Devices Inspection Procedures Scheme) | UK scheme for amusement device inspection, which registers approved inspection bodies; a route to UK/EU inspection engineers | Safety Engineer (EU/UK perspective) | [adips.co.uk](https://adips.co.uk/) |
| 7 | **ISEA** (International Safety Equipment Association), fall protection group | ANSI-accredited standards developer whose fall-protection manufacturers work on ANSI Z359; relevant to harness, connector and energy-absorber engineering | Standards & Test-Methods Reviewer; connector/absorber review | [safetyequipment.org](https://safetyequipment.org) |
| 8 | **ASSP** (American Society of Safety Professionals) | Professional society with fall-protection practice specialists and the secretariat for ANSI Z359 standards (verify current status on ASSP's site) | Safety Engineer (fall-protection side); Standards Reviewer | [assp.org](https://www.assp.org) |
| 9 | **SAE International** | Occupant-restraint, seat-belt and crash-test (ATD) engineering community; relevant to belt loading, submarining and sled tests | Biomechanics / dynamic-test review | [sae.org](https://www.sae.org) |
| 10 | **State PE licensing boards via NCEES** | Not a recruiting pool in itself, but the way to **verify** that a candidate's Professional Engineer licence is current before sign-off | Credential verification | [ncees.org/licensure](https://ncees.org/licensure/) |

Suggested order: start with pools 1, 2 and 5 (closest to ride restraints), use 7–9 for the restraint and fall-protection engineering side, and use 10 to verify licences.

## 3. Selection criteria
**Must have**
1. Current Professional Engineer licence (or national equivalent: Chartered Engineer, Ingenieur with recognised registration), verified through the issuing board (pool 10).
2. Documented experience in at least one of: amusement-ride design or inspection, occupant-restraint systems, fall-protection equipment.
3. Independence as set out in §5.
4. Willingness to sign a public, named sign-off record in `review/` (GOVERNANCE.md format).

**Strongly preferred**
- ASTM F24, ANSI Z359, CEN/TC 152 or ISO/TC 254 committee participation.
- Experience with ATD sled testing or dynamic restraint testing.
- Both a US and an EU/UK perspective across the two Safety Engineer seats.

## 4. Outreach message template
> **Subject:** Request for independent engineering review — open backup-restraint standard for amusement rides (RideBelt)
>
> Hello,
>
> I maintain **RideBelt**, an open, non-commercial project on the Hee-Lee Oss platform ([github.com/HeeLeeOss/ridebelt](https://github.com/HeeLeeOss/ridebelt)). It is developing an **optional backup restraint** for amusement-ride riders and a **free, open seat anchor standard (RAS)** that ride manufacturers could build into seats. Everything is published under CC BY 4.0, and we intend to propose RAS to ASTM F24.
>
> All the safety content is currently **DRAFT and marked not for use**. Our governance requires an **independent, credentialed engineer** to review the package before anything is released or any prototype is worn. That is the role we are hoping you, or someone you could recommend, could fill.
>
> **Scope of review (the "MVP gate"):** hazard analysis and FMEA, requirements, load analysis (including an open arrest model), the draft RAS standard, the anchor latch design, and the bench and sled-test results once available.
>
> **Time estimate:** roughly **40–80 hours** over several months, mostly at the MVP gate, plus optional early comments on the hazard analysis. *(This is an estimate. It depends on the size of the test package.)*
>
> **Independence:** we ask reviewers to have no financial interest in RideBelt and no conflict with any manufacturer whose ride is used as a test case. A short conflict-of-interest checklist is attached.
>
> **Compensation:** the project is open and currently unfunded, so we are first asking for **volunteer or pro-bono** review. If that isn't possible, we would seek a grant or sponsorship to pay an honorarium, on terms that keep the review independent (see the project's GOVERNANCE.md). We're glad to discuss.
>
> **Recognition:** your sign-off would be a named record in the repository, and you would be credited in RAS releases and any ASTM submission, if you wish.
>
> If you are interested, or can suggest a colleague or organisation, please reply or open an issue on the repository. Thank you for considering it.
>
> — RideBelt maintainer (@jdev1977)

## 5. Conflict-of-interest checklist
This follows GOVERNANCE.md role 2 (independence, no financial interest, no conflict with a manufacturer under review). Each candidate answers before appointment, and the answers are kept with the sign-off record in `review/`.

| # | Question | Disqualifying if "yes"? |
|---|---|---|
| 1 | Do you hold any financial interest in RideBelt, its gear makers, or any future certification-mark holder? | **Yes** |
| 2 | Would you or your employer profit directly from RAS adoption (e.g., selling RAS hardware or certification) beyond normal professional fees? | **Yes**, unless disclosed and accepted by the maintainer and the second reviewer |
| 3 | Are you employed by, or under contract to, a ride manufacturer or operator whose ride, seat or data is used in the package under review? | **Yes** for that review; may review other content |
| 4 | Do you hold or have you filed patents on rider-worn restraints or ride anchor systems (see docs/research/patentability-fto.md)? | Disclose; disqualifying for FTO-related content |
| 5 | Are you involved in pending litigation about an incident listed in docs/research/incidents.md? | **Yes** for content citing that incident |
| 6 | Did you author or substantially contribute to the content you are being asked to review? | **Yes** (no self-review) |
| 7 | Is your PE (or equivalent) licence current, and can it be verified publicly? | Disqualifying if **no** |
| 8 | Will you sign a named, public sign-off record in `review/`? | Disqualifying if **no** |

Rotation (from GOVERNANCE.md): at least two Safety Engineers are preferred, and the second reviews the first's sign-off for anything about release under load or rescue.

## 6. Process and timeline (estimates)
| Step | Action | Target |
|---|---|---|
| 1 | Maintainer posts a "Call for independent reviewers" issue in the repo, linking this plan | Week 1 |
| 2 | Outreach via pools 1, 2 and 5 (public contact routes, committee meetings) | Weeks 1–4 |
| 3 | Outreach via pools 7–9 for the restraint and fall-protection specialists | Weeks 2–6 |
| 4 | Screen candidates against §3 and §5; verify licences (pool 10) | Within 2 weeks of each reply |
| 5 | Record appointments in GOVERNANCE.md (role, credential, rotation note) and update PLAN.md "Review sign-off" | On appointment |
| 6 | Optional early review of the hazard analysis and FMEA (reduces rework) | After appointment |

If no Safety Engineer is appointed by the time the M2 bench evidence is ready, the intake-halt rule applies: drafting continues, but nothing is released.

## 7. Sources
- ASTM Committee F24 page (scope, membership, meetings): https://www.astm.org/committee-f24
- TÜV SÜD amusement ride services (inspection, testing, certification; EN 13814): https://www.tuvsud.com/en-us/amusement-rides-theme-parks
- ADIPS scheme site: https://adips.co.uk/
- ISEA Fall Protection Group and ANSI-accredited standards development: https://safetyequipment.org/?p=393
- NAARSO: https://www.naarso.com · AIMS International: https://www.aimsintl.org · ASSP: https://www.assp.org · SAE International: https://www.sae.org · NCEES licensure: https://ncees.org/licensure/
