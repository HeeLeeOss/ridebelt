# Open-Standard Adoption Model v0.2 (Phase 7)

> **Decision (2026-10-14): Path A, fully open.** RideBelt is published openly as a Hee-Lee Oss project. Designs and documents are CC BY 4.0, code is MIT, and **no patents will be filed**. The publication itself acts as a **defensive publication**: it becomes prior art, so nobody (including us) can later patent these ideas and block others from using them.

## Goal
Get as many rides as possible to adopt the RideBelt Anchor Standard (RAS), and as many riders as possible to have access to certified backup gear. Adoption matters more than revenue.

## Model
| Who | Cost to use RAS | What they get |
|---|---|---|
| Ride manufacturers (new builds) | **Free**: open standard, CC BY 4.0 | Spec, interface geometry, conformance test procedures |
| Park operators (retrofits) | **Free** | Spec, ride application guide template, operator and rescue procedures |
| Gear makers (belts, tethers) | **Free** to build to the spec | Spec and test methods. Using the **"RAS-certified" mark** needs independent third-party testing (see below) |

## What open licensing does *not* cover: the certification mark
CC BY 4.0 grants copyright permissions only. It **does not grant trademark rights** (license §2(b)(2)). That keeps a quality backstop:
- **"RideBelt" and "RAS-certified"** can be held as a **certification mark**, by a neutral body or a nonprofit set up for it, so that only gear that passes third-party testing can carry it.
- This matters for safety. Anyone may build to an open spec, but riders and parks need a way to tell tested gear from knock-offs (hazard H9).
- Certification fees (charged by test labs, and possibly a small program fee) fund the program. They are not a toll on the standard.

## Path to a real standard
1. Publish RAS openly (this repo), clearly marked DRAFT until the MVP gate.
2. After the MVP gate, propose RAS to **ASTM F24** as a work item or annex (F2291 already recognizes an *independent secondary restraint* for Class 5).
3. Encourage insurers to offer premium credits for RAS-equipped rides.

## Consequences of choosing open
- **No exclusivity.** Anyone, including big operators and manufacturers, may implement RAS and build compatible gear. That is the intent.
- **Defensive publication:** once public, the published features become prior art against later third-party patents. **Publish complete detail** (drawings, dimensions, variants), because prior art protects only what it actually discloses.
- **Existing third-party patents still apply.** Open publication does not grant anyone a license to *other people's* patents. Builders must still respect the active patents listed in [research/patentability-fto.md](../research/patentability-fto.md) (especially Universal's US 11,975,679 and EP 4 380 708, and the wireless-lock US 12,134,366). The design-arounds noted there stay in force.

## Still needed (legal counsel)
- Trademark or certification-mark search and filing for "RideBelt" and "RAS", and who holds it (a nonprofit is preferred)
- Product-liability exposure for publishing safety designs: the disclaimers in [SAFETY-NOTICE.md](../../SAFETY-NOTICE.md) and the CC BY "as is" terms, reviewed by counsel
- Certification program rules: lab accreditation, revocation and recalls
