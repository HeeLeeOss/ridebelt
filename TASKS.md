# TASKS — ridebelt

> Status: Draft · Version: 0.1.0 · Last updated: 2026-10-14 · Maintainer: @jdev1977 · Lane: donated

## How these tasks map to Hee-Lee Oss
Each task is a Task JSON in [tasks/](tasks/). It uses the same fields as other Hee-Lee Oss projects: `id`, `title`, `project` (`ridebelt`), `type`, `lane` (`donated`), `priority`, `domain`, `riskTier`, `urgent`, `deliverable`, `tokenEstimate`, `status` (all start `open`), `context`, `objective`, `acceptanceCriteria[]`, `resources[]`, `output`, `requestor`, `verifiedNeed` and `outputLicense`.

- `riskTier` follows [GOVERNANCE.md](GOVERNANCE.md). **High** tasks also set `expertReview: true`: they merge as **DRAFT only**, and release needs the MVP-gate Safety Engineer.
- `requestor` is **TO BE SECURED** and `verifiedNeed` is **`false`** until a ride manufacturer, operator or ASTM F24 member commits to review or pilot.
- `outputLicense`: **CC-BY-4.0** for content, data and models; **MIT** for code.
- Every task's context repeats the project guardrails: keep DRAFT banners, give no wear-it-today instructions, copy no paid-standard text, and respect the patent design-arounds.

## Agent tasks
| Milestone | ID | Title | Type | Size | Risk | Deliverable |
|---|---|---|---|---|---|---|
| M0 | ridebelt-reviewer-001 | Plan recruitment of the MVP-gate Safety Engineer and advisory reviewers | research | small | low | document |
| M0 | ridebelt-incidents-002 | Verify incident entries against primary sources | research | medium | medium | document |
| M0 | ridebelt-accel-002 | Compile open ride-acceleration datasets with provenance | data | medium | medium | dataset |
| M0 | ridebelt-traceability-001 | Automated traceability and consistency checker | code | small | medium | pr |
| M0 | ridebelt-fto-003 | Patent FTO search round 3 (CN/JP/KR and applicant-name queries) | research | medium | medium | document |
| M1 | ridebelt-model-002 | Arrest model v2: 2-DOF (pelvis translation + torso rotation), lateral/forward cases, tests | code | large | high | pr |
| M1 | ridebelt-ras-002 | Draft RAS v0.2: resolve derivable TBDs, terms, full conformance procedures | design-spec | large | high | document |
| M1 | ridebelt-testmethods-001 | Detailed bench test procedures (T-S1 to T-S5, T-E1 to T-E7) | design-spec | medium | high | document |
| M1 | ridebelt-ops-001 | Draft operator procedures and rescue/evacuation guide | writing | medium | high | document |
| M1 | ridebelt-appguide-001 | Ride application-guide template | design-spec | small | high | document |
| M1 | ridebelt-cad-001 | Parametric open CAD of the RAS receiver envelope and tongue | design-spec | large | high | pr |
| M3-prep | ridebelt-explainer-001 | Plain-language public explainer (what RideBelt is and is not) | writing | small | medium | document |
| M3-prep | ridebelt-f24-001 | Outline an ASTM F24 work-item proposal for RAS | writing | small | medium | document |

Suggested order: `traceability-001` first, so later PRs are checked automatically. Then `reviewer-001`, which is the critical path, then the rest of M0. `model-002` benefits from `accel-002`.

## Human milestones (not agent tasks)
| Milestone | Item | Owner |
|---|---|---|
| M0 | Purchase ASTM F2291-26a and EN 13814 (+A1:2024); confirm −Gz limits vs. the −2.0 g rating | Maintainer |
| M0 | Recruit and name the MVP-gate Safety Engineer (uses `reviewer-001` output) | Maintainer |
| M0 | Counsel: certification-mark holder, product-liability review of publishing | Maintainer + counsel |
| M2 | Build prototype parts; run bench tests (T-S, T-E) at an accredited lab | Lab |
| M2 | ATD sled tests (T-D1–T-D5) and multibody simulation (A3) at a crash lab | Lab |
| M2 | Seat geometry and fit trials with a ride manufacturer (no human wear before MVP gate) | Manufacturer partner |
| **MVP gate** | Credentialed review of the full package plus results → `review/` sign-off → `release/` | Safety Engineer |
| M3 | Submit to ASTM F24; certification program; manufacturer pilot | Maintainer + partners |

## Backlog / future
- Post-launch features (themed shells, rider ID, connected experiences): [docs/business/post-launch.md](docs/business/post-launch.md). Not opened as tasks until RAS adoption.
- Self-retracting inertia-locking tether reel: detailed design (after `model-002`).
- Translations of the explainer and safety notice (after the MVP gate).
