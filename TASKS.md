# TASKS — ridebelt

> Status: Draft · Version: 0.2.0 · Last updated: 2026-10-15 · Maintainer: @jdev1977 · Lane: donated

## How these tasks map to Hee-Lee Oss
Each task is a Task JSON in [tasks/](tasks/). It uses the same fields as other Hee-Lee Oss projects: `id`, `title`, `project` (`ridebelt`), `type`, `lane` (`donated`), `priority`, `domain`, `riskTier`, `urgent`, `deliverable`, `tokenEstimate`, `status` (all start `open`), `context`, `objective`, `acceptanceCriteria[]`, `resources[]`, `output`, `requestor`, `verifiedNeed` and `outputLicense`.

- `riskTier` follows [GOVERNANCE.md](GOVERNANCE.md). **High** tasks merge as **DRAFT only**, and release needs the MVP-gate Safety Engineer (stated in each task's context and acceptance criteria).
- `requestor` is **TO BE SECURED** and `verifiedNeed` is **`false`** until a ride manufacturer, operator or ASTM F24 member commits to review or pilot.
- `outputLicense`: **CC-BY-4.0** for content, data and models; **MIT** for code.
- Every task's context repeats the project guardrails: keep DRAFT banners, give no wear-it-today instructions, copy no paid-standard text, and respect the patent design-arounds.

## Agent tasks
65 tasks: M0 foundation and evidence (24), M1 draft design package (28), M3-prep communication, adoption and translations (13). By risk tier: low 5, medium 32, high 28 (high = merged as DRAFT only; release needs the MVP-gate Safety Engineer).

| Milestone | ID | Title | Type | Size | Risk | Deliverable | Depends on |
|---|---|---|---|---|---|---|---|
| M0 | ridebelt-reviewer-001 | Plan recruitment of the MVP-gate Safety Engineer and advisory reviewers | research | small | low | document | — |
| M0 | ridebelt-incidents-002 | Verify US incident entries against primary sources | research | medium | medium | document | — |
| M0 | ridebelt-incidents-003 | Verify non-US incident entries against primary sources | research | medium | medium | document | incidents-002 |
| M0 | ridebelt-incidents-004 | Extend the incident review with 2015–2026 ejection and fall cases | research | medium | medium | document | incidents-002 |
| M0 | ridebelt-foia-001 | Public-records request templates for ride incident reports | writing | small | low | document | — |
| M0 | ridebelt-accel-002 | Compile open ride-acceleration datasets with provenance | data | medium | medium | dataset | — |
| M0 | ridebelt-accel-003 | Literature review of published ride acceleration measurements | research | medium | medium | document | — |
| M0 | ridebelt-accel-004 | Open measurement protocol for ride accelerations (bystander/seat-mounted data logging) | writing | small | medium | document | accel-002 |
| M0 | ridebelt-anthro-001 | Adult anthropometry basis for belt and harness sizing | data | medium | medium | document | — |
| M0 | ridebelt-anthro-002 | Child and youth anthropometry for minimum-rider rules | data | small | medium | document | — |
| M0 | ridebelt-biomech-001 | Literature review: pelvic and abdominal loading tolerance under belt restraint | research | medium | medium | document | — |
| M0 | ridebelt-biomech-002 | Literature review: inverted and suspended-occupant tolerance | research | small | medium | document | — |
| M0 | ridebelt-regulatory-001 | Jurisdiction map: rules on amusement rides and rider-supplied equipment | research | medium | medium | document | — |
| M0 | ridebelt-materials-001 | Webbing and stitching materials survey | research | medium | medium | document | — |
| M0 | ridebelt-hardware-001 | Market survey: rated connectors, key-release buckles and absorbers | research | medium | medium | document | — |
| M0 | ridebelt-retractor-001 | Technology survey: inertia-locking retractors and self-retracting lifelines | research | small | medium | document | — |
| M0 | ridebelt-fto-003 | Patent FTO search round 3 (CN/JP/KR and applicant-name queries) | research | medium | medium | document | — |
| M0 | ridebelt-fto-004 | FTO check: Integrated Harness and Shoulder Module vs. harness patents | research | small | medium | document | — |
| M0 | ridebelt-traceability-001 | Automated traceability and consistency checker | code | small | medium | pr | — |
| M0 | ridebelt-ci-001 | Link checker and markdown lint in CI | code | small | low | pr | traceability-001 |
| M0 | ridebelt-docs-001 | Glossary of RideBelt terms | writing | small | low | document | — |
| M0 | ridebelt-docs-002 | CONTRIBUTING guide for RideBelt | writing | small | low | document | — |
| M0 | ridebelt-requirements-002 | TBD register: every open value with data source and owner | writing | small | medium | document | — |
| M0 | ridebelt-requirements-003 | Raise the design rider mass toward 160 kg (REQ-L2) and size to the 99th percentile of both sexes (REQ-F1) | design-spec | medium | high | pr | anthro-001 (merged) |
| M1 | ridebelt-hazard-002 | Hazard analysis and FMEA update for the Integrated Harness and recent findings | design-spec | medium | high | document | — |
| M1 | ridebelt-model-002 | Arrest model v2: 2-DOF pelvis translation + torso rotation | code | large | high | pr | — |
| M1 | ridebelt-model-003 | Arrest model: lateral and forward load cases | code | medium | high | pr | model-002 |
| M1 | ridebelt-model-004 | Arrest model: run measured acceleration pulses | code | small | high | pr | accel-002 |
| M1 | ridebelt-model-005 | Arrest model: uncertainty and sensitivity analysis | code | medium | high | pr | — |
| M1 | ridebelt-ras-002 | Draft RAS v0.2: requirements text in standards style | design-spec | large | high | document | — |
| M1 | ridebelt-ras-003 | RAS conformance test procedures (RAS-CT0 to RAS-CT7) | design-spec | medium | high | document | ras-002 |
| M1 | ridebelt-ras-004 | RAS marking, labelling and installation-record spec | design-spec | small | high | document | — |
| M1 | ridebelt-testmethods-001 | Bench test procedures: static strength (T-S1 to T-S5) | design-spec | medium | high | document | — |
| M1 | ridebelt-testmethods-002 | Test procedures: environmental and durability (T-E1 to T-E7) | design-spec | medium | high | document | — |
| M1 | ridebelt-testmethods-003 | Test protocols: dynamic drop and sled tests (T-D1 to T-D5) | design-spec | large | high | document | — |
| M1 | ridebelt-testmethods-004 | Test protocols: fit and operation (T-F1 to T-F9), post-MVP human trials | design-spec | medium | high | document | — |
| M1 | ridebelt-design-001 | Hip Belt detailed design spec | design-spec | medium | high | document | anthro-001, materials-001 |
| M1 | ridebelt-design-002 | Integrated Harness detailed design spec | design-spec | medium | high | document | design-001, fto-004 |
| M1 | ridebelt-design-003 | Clip-on Shoulder Module detailed design spec | design-spec | small | high | document | design-001 |
| M1 | ridebelt-design-004 | Convertible Center Strap detailed design spec | design-spec | small | high | document | design-001 |
| M1 | ridebelt-design-005 | Self-retracting tether reel concept spec | design-spec | medium | high | document | retractor-001 |
| M1 | ridebelt-design-006 | Universal Wrap Strap spec and approved-member rules | design-spec | small | high | document | — |
| M1 | ridebelt-sizing-001 | Sizing system for Hip Belt and Integrated Harness | design-spec | small | high | document | anthro-001 |
| M1 | ridebelt-ops-001 | Draft operator procedures (pre-dispatch checks and refusal criteria) | writing | medium | high | document | — |
| M1 | ridebelt-ops-002 | Draft rescue and evacuation guide (inverted stop, release under load) | writing | medium | high | document | — |
| M1 | ridebelt-appguide-001 | Ride application-guide template with a fictional worked example | design-spec | small | high | document | — |
| M1 | ridebelt-labels-001 | Draft product labelling and instructions-for-use | writing | medium | high | document | — |
| M1 | ridebelt-inspection-001 | Gear inspection and retirement criteria | writing | small | high | document | — |
| M1 | ridebelt-cad-001 | Parametric open CAD: RAS tongue | design-spec | medium | high | pr | — |
| M1 | ridebelt-cad-002 | Parametric open CAD: RAS receiver envelope and interface | design-spec | large | high | pr | cad-001 |
| M1 | ridebelt-cad-003 | Seat geometry and anchor-zone model (RAS-2 and RAS-3) | design-spec | medium | high | pr | — |
| M1 | ridebelt-diagram-001 | System overview diagrams (SVG) | design-spec | small | medium | document | — |
| M3-prep | ridebelt-explainer-001 | Plain-language public explainer (what RideBelt is and is not) | writing | small | medium | document | — |
| M3-prep | ridebelt-faq-001 | FAQ for riders, parks and manufacturers | writing | small | medium | document | — |
| M3-prep | ridebelt-outreach-001 | Manufacturer and operator briefing pack | writing | small | medium | document | — |
| M3-prep | ridebelt-outreach-002 | Insurer and regulator briefing | writing | small | medium | document | — |
| M3-prep | ridebelt-f24-001 | Outline an ASTM F24 work-item proposal for RAS | writing | small | medium | document | — |
| M3-prep | ridebelt-certmark-001 | Research: certification-mark program models | research | small | medium | document | — |
| M3-prep | ridebelt-liability-001 | Research: liability considerations for publishing open safety designs | research | small | medium | document | — |
| M3-prep | ridebelt-translate-notice-es | Translate the Safety Notice into Spanish | writing | small | medium | translation | — |
| M3-prep | ridebelt-translate-notice-fr | Translate the Safety Notice into French | writing | small | medium | translation | — |
| M3-prep | ridebelt-translate-notice-de | Translate the Safety Notice into German | writing | small | medium | translation | — |
| M3-prep | ridebelt-translate-notice-ja | Translate the Safety Notice into Japanese | writing | small | medium | translation | — |
| M3-prep | ridebelt-translate-notice-zh | Translate the Safety Notice into Simplified Chinese | writing | small | medium | translation | — |
| M3-prep | ridebelt-translate-notice-pt | Translate the Safety Notice into Portuguese | writing | small | medium | translation | — |

**Suggested start:** `traceability-001` (checks every later PR), `reviewer-001` (critical path), then the M0 research tasks, which feed the M1 design specs. Dependencies are also stated in each task's context.

**Good first deeds:** `docs-001`, `foia-001`, `explainer-001`, `faq-001` and the `translate-notice-*` tasks (small, low or medium risk).

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
