# Governance — ridebelt Reviewers & Gates

## Overview
RideBelt is **safety-critical**. Mistakes could hurt people, so governance separates **drafting** (open to anyone, including donated AI capacity) from **release** (only after credentialed engineering review). Reviewing in two stages keeps work moving without ever releasing unreviewed safety content.

## Content states
| State | Where | Meaning | Who can approve |
|---|---|---|---|
| **DRAFT** | `docs/` (every safety doc carries the 🚧 DRAFT banner) | Work in progress. **Not for use.** | Maintainer (merge) |
| **RELEASED** | `release/` (created at the MVP gate) | Reviewed and signed off; may be relied on within its stated scope | **MVP-gate Safety Engineer only** |

**Rules**
1. A DRAFT banner may be removed **only** when a sign-off record for that document exists in `review/`.
2. No content is moved to `release/` without a signed record in `review/`.
3. **No person wears any RideBelt prototype**, even statically, before the MVP gate is passed.
4. Nothing in this repo may give instructions for wearing or attaching anything to a ride today.

## Risk tiers for tasks
| Tier | Examples | Review before merge |
|---|---|---|
| **low** | Recruitment plans, explainers, repo maintenance | Maintainer |
| **medium** | Incident verification, acceleration datasets, patent searches, traceability tooling, standards mapping | Maintainer checks sources and citations |
| **high** | Anything that sets numbers, geometry or procedures someone could rely on: requirements, RAS text, latch design, test methods, ops and rescue procedures, models | Maintainer merges as **DRAFT only**. **Release needs the MVP-gate Safety Engineer** (`expertReview: true`) |

This applies the Hee-Lee Oss rule that safety work needs credentialed sign-off: for RideBelt, **release** is the step that needs it, and DRAFT merges are explicitly labeled "not for use".

## Required roles
### 1. Maintainer: @jdev1977 (filled)
Triage, merges DRAFT content, keeps banners and traceability intact, buys the paid standards (F2291-26a, EN 13814).

### 2. MVP-gate Safety Engineer (**TO BE SECURED**, blocking for release)
- **Qualification:** a licensed Professional Engineer (or national equivalent) with amusement-ride or restraint-system experience. Preferred: ASTM F24 participation, NAARSO/AIMS background, or fall-protection or occupant-restraint engineering.
- **Independence:** no financial interest in RideBelt and no conflict with any ride manufacturer under review.
- **Scope at the MVP gate:** `safety/`, `requirements.md`, `analysis/`, the RAS draft, the latch design, and bench and ATD results.
- **Rotation:** at least 2 engineers preferred; a second engineer reviews the first's sign-off for anything about release under load or rescue.

### 3. Standards & Test-Methods Reviewer (TO BE SECURED, advisory)
Test-lab or standards-committee experience. Reviews test procedures for repeatability.

### 4. Legal counsel (TO BE SECURED, advisory)
Product-liability exposure, the certification mark, and FTO before any manufacture.

## Intake-halt rule
- **No named Safety Engineer → nothing is released and no human wear.** Drafting continues.
- **No maintainer available → no merges.**

## Sign-off record format (`review/<gate>-<doc>-<date>.md`)
Reviewer name, credential and licence number, scope, documents and versions (commit SHA), findings, conditions, and the decision (approve / approve with conditions / reject). Signed by the reviewer.

## Conflict resolution
The Safety Engineer's technical decision on safety content is final. Disagreements are recorded in `review/` with reasons.

## Licensing of contributions
Contributions are CC BY 4.0 (content) or MIT (code), with a DCO sign-off on each commit. AI assistance is disclosed in each PR, as Hee-Lee Oss requires.
