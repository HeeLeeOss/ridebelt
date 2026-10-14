# FMEA v0.1 (Phase 2, IEC 60812 method)

> 🚧 **DRAFT: not reviewed by a qualified engineer; not for use.** Not released until the MVP review gate. See [SAFETY-NOTICE](../../SAFETY-NOTICE.md).


S = severity, O = occurrence, D = detection (each 1–10). RPN = S × O × D. **Any S ≥ 9 needs a design mitigation and a verifying test, whatever the RPN.** Ratings are initial engineering estimates to revisit after testing.

| Component | Failure mode | Effect | S | O | D | RPN | Mitigation | Test |
|---|---|---|---|---|---|---|---|---|
| Hip Belt | Worn too high, or migrates onto the abdomen | Abdominal or spinal injury; submarining | 9 | 5 | 5 | **225** | Contoured belt, position guide, downward tether angle, operator visual check | T-D2, T-D3, T-F3 |
| Required module | Missing for the ride class | Partial retention on inverting or drop rides | 9 | 4 | 4 | 144 | Ride rating labels, tag-based module check, operator check | T-E5, ops guide |
| Harness webbing | Tensile rupture | Loss of retention | 10 | 2 | 4 | 80 | 5:1 SF, inspection, retirement | T-S1, T-E1 |
| Harness stitching | Bar-tack failure | Loss of retention | 10 | 3 | 5 | 150 | Stitch-pattern qualification, contrasting thread for inspection | T-S1 |
| Buckle | Slip under load | Free travel grows, rider moves | 9 | 3 | 4 | 108 | Auto-locking buckles, slip test | T-S2 |
| Tether | Cut or abrasion on a sharp edge | Rupture | 10 | 3 | 5 | 150 | Abrasion sleeve, edge rules in RAS | T-S4 |
| Energy absorber | Deploys at too low a load | Extra free travel | 8 | 2 | 3 | 48 | Deployment threshold spec, visual indicator | T-D2, T-E4 |
| Connector | Opens in use (snap-hook gate, or RAS latch) | Disconnection | 10 | 2 | 5 | 100 | Key/tool-release RAS latch; double-action snap hook; two tethers | T-S3 |
| RAS latch | False latch (partly inserted) | Tether not actually held | 10 | 3 | 4 | 120 | Positive-latch geometry, sensor, indicator | RAS-CT7 |
| Connector | Cross-loaded on the gate | Strength reduced by about 70% | 10 | 4 | 6 | **240** | Captive-pin connectors at the harness end, RAS anchor geometry stops cross-loading | T-S3, RAS-CT2 |
| Wrap strap | Slides off the member | Disconnection | 10 | 3 | 5 | 150 | Choke-wrap design, minimum and maximum member diameter, end-stop rule | T-S5 |
| Wrap strap | Anchored to the wrong member | No protection | 10 | 5 | 7 | **350** | Ride-specific application guides, operator approval, RAS preferred | Ops guide |
| RAS anchor | Mounting fastener failure | Disconnection | 10 | 2 | 4 | 80 | Redundant fasteners, torque marking, inspection schedule | RAS-CT1 |
| RAS sensor | False "clipped" signal | Missed interlock | 6 | 3 | 5 | 90 | Two-channel sensing, self-test | RAS-CT4 |

## Top priorities
1. **Wrong anchoring member (RPN 350).** This is the main argument for pushing RAS adoption over wrap straps.
2. **Cross-loaded connector (RPN 240).** Fix this by geometry, not by instructions.
3. **Hip Belt position (RPN 225).** The leg-loop-free design depends on the belt staying low. Fix this with belt shape and anchor angle, not just with fit instructions.
