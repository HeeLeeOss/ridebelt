# Contributing to RideBelt

Thank you for helping. RideBelt is a **safety-critical** open project, so contributing works a little differently from most repositories. Please read this page, the [Safety Notice](SAFETY-NOTICE.md) and [GOVERNANCE.md](GOVERNANCE.md) before opening a pull request.

Content you contribute is licensed **CC BY 4.0** ([LICENSE](LICENSE)). Code is licensed **MIT** ([LICENSE-CODE](LICENSE-CODE)).

## 1. Picking up work
- **Through Hee-Lee Oss (recommended):** run `hee-lee-oss browse`, choose a `ridebelt-*` task, then `hee-lee-oss pull --task-file <task> --repo HeeLeeOss/ridebelt`. Your workspace gets the task's `TASK.md` and `CONTEXT.md`; read both fully.
- **Directly:** pick an open task from [TASKS.md](TASKS.md) (the JSON is in [tasks/](tasks/)), or open an issue describing what you'd like to do.
- Check the task's **"Depends on"** column in TASKS.md. If a dependency isn't merged yet, do it first or say in your PR which outputs you assumed.
- One task per pull request. Keep the change to what the task asks for.

## 2. Project guardrails (non-negotiable)
1. **DRAFT stays DRAFT.** Never remove or weaken the 🚧 DRAFT banner on a safety document. Only a credentialed sign-off record in `review/` can do that (see GOVERNANCE.md, "Content states").
2. **No instructions for use today.** Nothing may tell anyone how to wear, build, or attach anything to an amusement ride before the MVP gate is passed.
3. **No copied standards text.** ASTM, EN and ISO standards are paid documents. Cite them by number, edition and title, and summarise in your own words.
4. **Cite everything.** Every factual claim needs a working source link. Label estimates as estimates and assumptions as `ASSUMPTION`.
5. **No private individuals.** Don't name incident victims or private people. Name organisations and public roles only.
6. **Respect the patent design-arounds** in [docs/research/patentability-fto.md](docs/research/patentability-fto.md): mechanical or wired release only (never wireless), no vest-style height adjusters or leg flaps or leg loops on harness designs, and no spring-plate anchor sensor. Being open source doesn't license anyone to other companies' patents.
7. **Stay in scope.** No drive-by refactors, reformatting, or dependency changes.

If a task would break any of these, **stop and say so in an issue**. Not opening a PR is a good outcome.

## 3. Risk tiers and review
Every task has a `riskTier` (see GOVERNANCE.md, "Risk tiers for tasks"):

| Tier | Typical work | What review means |
|---|---|---|
| low | Explainers, glossary, repo housekeeping | Maintainer review |
| medium | Research, datasets, patent searches, tooling | Maintainer checks sources and citations |
| high | Requirements, the RAS standard, design specs, test methods, operations and rescue procedures, models | Merged **as DRAFT only**; **release** needs the MVP-gate Safety Engineer |

A merge is not an approval for use. Nothing is RELEASED until a credentialed engineer signs it off.

## 4. Citation and writing style
- Link sources inline, e.g. `([source](https://…))`, or add a **Sources** list at the end.
- For papers, give authors, year, title and DOI or URL. For patents, give the number with a Google Patents or Espacenet link.
- Keep the existing document structure and ID schemes: `REQ-*` requirements, `H*` hazards, `T-*` and `RAS-CT*` tests.
- When you add or change a requirement, hazard or test, update the cross-references: the requirement's verification column, the test plan's traceability table, and the hazard or FMEA rows.
- Plain, direct English. Use tables for comparisons and values.

## 5. Checks you must run
```bash
python tools/check_traceability.py
```
This checker runs in CI on every PR. It verifies that:
- every requirement is in the traceability table;
- every referenced test ID exists;
- hazards cite real requirements;
- every FMEA row with severity 9 or more has a mitigation and a test;
- every safety document keeps its DRAFT banner.

Code contributions must also pass their own tests (e.g., `pytest`) and use only the dependencies the task allows.

## 6. DCO sign-off
Every commit must carry a **Developer Certificate of Origin** sign-off, confirming you have the right to submit the work under the project's licences ([developercertificate.org](https://developercertificate.org/)):

```bash
git commit -s -m "Your message"
```

This adds `Signed-off-by: Your Name <your-email>` to the commit. To keep your personal email private, use your GitHub no-reply address (`ID+username@users.noreply.github.com`, shown in your GitHub email settings) for `user.email` in this repository. `hee-lee-oss submit` adds the sign-off for you.

## 7. Disclosing AI assistance
Hee-Lee Oss contributions are often prepared with AI coding agents. **Say so in the PR description**, and name the agent (e.g., "Prepared with AI assistance (Claude Code)"). `hee-lee-oss submit` adds this disclosure automatically, so don't remove it. Whether a person or an agent wrote it, the same guardrails, citations and review apply.

## 8. Pull request checklist
Copy this into your PR description and tick each item:

- [ ] Linked the task ID (e.g., `ridebelt-anthro-001`) or issue
- [ ] Met every acceptance criterion in the task
- [ ] DRAFT banners intact on every safety document I touched
- [ ] No instructions for wearing or attaching anything to a ride
- [ ] No text copied from paid standards; standards cited by number and title
- [ ] Every factual claim cited with a working link; estimates and assumptions labelled
- [ ] No private individuals or incident victims named
- [ ] Patent design-arounds respected (patentability-fto.md)
- [ ] Cross-references updated, and `python tools/check_traceability.py` passes
- [ ] Commits signed off (`git commit -s`)
- [ ] AI assistance disclosed (if used)
- [ ] Change limited to the task's scope

## 9. Review flow
1. CI runs the traceability checker.
2. The maintainer reviews: scope, sources, guardrails and the risk tier's requirements.
3. **Low and medium:** merged when the review passes.
4. **High:** merged as DRAFT. It is reviewed again at the MVP gate by the credentialed Safety Engineer before release (GOVERNANCE.md).
5. After merge, the task is marked done (`hee-lee-oss complete`) so it isn't served again.

## Questions
Open an issue in [HeeLeeOss/ridebelt](https://github.com/HeeLeeOss/ridebelt/issues). For questions about the platform itself, see the [Hee-Lee Oss docs](https://github.com/HeeLeeOss/hee-lee-oss-downloads).
