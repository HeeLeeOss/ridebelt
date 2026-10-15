# Adult Anthropometry Basis for Belt and Harness Sizing

> Status: research input (task `ridebelt-anthro-001`) · License: CC BY 4.0 · Prepared with AI assistance (Claude Code)
>
> These are **population statistics computed from open datasets**. They are inputs for the sizing work (`ridebelt-sizing-001`) and the design specs, not design requirements. Any sizing decision based on them stays DRAFT until the MVP gate (see [GOVERNANCE.md](../../GOVERNANCE.md)).

## 1. Sources and licences
| Dataset | What it is | Licence / status | Files used (SHA-256) |
|---|---|---|---|
| **NHANES 2021–2023** (CDC/NCHS) | Nationally representative US civilian survey; body measures exam (`BMX_L`) with demographics (`DEMO_L`) | US federal government work, public domain in the US ([17 U.S.C. §105](https://www.law.cornell.edu/uscode/text/17/105)). NCHS asks users not to attempt to identify participants | `BMX_L.xpt` `44440c416d9ad709e8b1708a5975378ab4d5b18edc39eb5015c2ae7186500170`, `DEMO_L.xpt` `ca4374a158b493b8b0163e1388da21d57a18d1b9cecff2aa4e2fa2bec494fe23` · [BMX_L documentation](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.htm), [DEMO_L documentation](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.htm) |
| **NHANES 2017–March 2020 pre-pandemic** (CDC/NCHS) | Same exam, earlier combined cycle (`P_BMX`, `P_DEMO`); used as a cross-check | As above | `P_BMX.xpt` `7038d0da3169420a4a3cbaec09ac586a701b38e1c7b925431b60e13ac24fed66`, `P_DEMO.xpt` `2e46c6c26bf77cd8989f64011ace12cbf42c0f3e03414eb59acc5328c8f87913` · [P_BMX documentation](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/P_BMX.htm) |
| **ANSUR II** (US Army, 2012 survey) | 4,082 men and 1,986 women, 93 directly measured dimensions, including seated, waist and crotch measures not in NHANES | US Army survey data, publicly released in 2017 via the [Penn State OPEN Design Lab](https://www.openlab.psu.edu/ansur2/). The host page states no licence. As a US government work it is treated as public domain in the US (17 U.S.C. §105); **confirm with the data host before redistributing the raw files** | `ANSUR_II_MALE_Public.csv` `0547aea0170e5293de519389981135e75803f02e6d40c77ace740decc0caac64`, `ANSUR_II_FEMALE_Public.csv` `ed7e800aa97a4d42f8286b988be2fe1883a2e789588169db959864b707d1757a` |

Raw data files are **not** copied into this repository. Download them from the links in [anthropometry/compute_percentiles.py](anthropometry/compute_percentiles.py), which reproduces every table below (`python compute_percentiles.py <data_dir>`).

**Method**
- NHANES: adults aged 18 and over. Percentiles use the MEC exam survey weights (`WTMEC2YR` for 2021–2023, `WTMECPRP` for 2017–2020) on the weighted cumulative distribution, following the [NHANES weighting guidance](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx). Weighted percentiles estimate the US civilian adult population. Variance (standard errors) was not computed.
- ANSUR II: unweighted percentiles of the full public sample. Body mass is converted from hectograms (the `weightkg` column) to kg, per the data host's note.

## 2. Results
### ANSUR II (US Army, 2012), unweighted

Units: mm; body mass in kg.

| Variable | Sex | n | P1 | P5 | P50 | P95 | P99 |
|---|---|---|---|---|---|---|---|
| Waist circumference (`waistcircumference`) | M | 4082 | 725 | 768 | 937 | 1131 | 1214 |
| Waist circumference (`waistcircumference`) | F | 1986 | 665 | 710 | 852 | 1040 | 1115 |
| Hip (buttock) circumference (`buttockcircumference`) | M | 4082 | 862 | 899 | 1017 | 1149 | 1218 |
| Hip (buttock) circumference (`buttockcircumference`) | F | 1986 | 867 | 901 | 1018 | 1156 | 1206 |
| Hip breadth, sitting (`hipbreadthsitting`) | M | 4082 | 317 | 333 | 378 | 431 | 462 |
| Hip breadth, sitting (`hipbreadthsitting`) | F | 1986 | 333 | 348 | 397 | 456 | 485 |
| Thigh circumference (proximal) (`thighcircumference`) | M | 4082 | 497 | 532 | 624 | 723 | 774 |
| Thigh circumference (proximal) (`thighcircumference`) | F | 1986 | 495 | 527 | 613 | 711 | 757 |
| Sitting height (`sittingheight`) | M | 4082 | 836 | 860 | 918 | 977 | 1001 |
| Sitting height (`sittingheight`) | F | 1986 | 784 | 803 | 857 | 912 | 932 |
| Waist back length (C7 to waist, back) (`waistbacklength`) | M | 4082 | 415 | 433 | 477 | 524 | 548 |
| Waist back length (C7 to waist, back) (`waistbacklength`) | F | 1986 | 365 | 384 | 424 | 470 | 494 |
| Waist front length, sitting (suprasternale to waist) (`waistfrontlengthsitting`) | M | 4082 | 324 | 342 | 386 | 438 | 459 |
| Waist front length, sitting (suprasternale to waist) (`waistfrontlengthsitting`) | F | 1986 | 304 | 317 | 355 | 396 | 413 |
| Crotch length, omphalion (front waist via crotch to back waist) (`crotchlengthomphalion`) | M | 4082 | 523 | 549 | 620 | 701 | 739 |
| Crotch length, omphalion (front waist via crotch to back waist) (`crotchlengthomphalion`) | F | 1986 | 527 | 553 | 619 | 692 | 723 |
| Biacromial (shoulder) breadth (`biacromialbreadth`) | M | 4082 | 371 | 384 | 415 | 447 | 463 |
| Biacromial (shoulder) breadth (`biacromialbreadth`) | F | 1986 | 322 | 335 | 365 | 396 | 406 |
| Body mass (`weightkg`) | M | 4082 | 57.8 | 64.4 | 84.6 | 110.7 | 124.2 |
| Body mass (`weightkg`) | F | 1986 | 46.7 | 51.3 | 66.8 | 87.1 | 97.5 |

### NHANES 2021-2023, adults 18+, survey-weighted (`WTMEC2YR`)

Units: cm; body mass in kg.

| Variable | Sex | n | P1 | P5 | P50 | P95 | P99 |
|---|---|---|---|---|---|---|---|
| Waist circumference (`BMXWAIST`) | M | 2738 | 70.4 | 77.4 | 100.5 | 133.2 | 149.2 |
| Waist circumference (`BMXWAIST`) | F | 3281 | 67.2 | 73.2 | 95.2 | 128.7 | 143.4 |
| Hip circumference (`BMXHIP`) | M | 2702 | 84.0 | 89.0 | 103.5 | 129.0 | 144.6 |
| Hip circumference (`BMXHIP`) | F | 3255 | 84.5 | 89.3 | 106.6 | 138.2 | 156.2 |
| Body mass (`BMXWT`) | M | 2825 | 52.4 | 60.4 | 86.3 | 131.5 | 155.8 |
| Body mass (`BMXWT`) | F | 3423 | 44.0 | 50.3 | 73.3 | 118.7 | 146.6 |
| Stature (`BMXHT`) | M | 2827 | 155.7 | 162.1 | 175.2 | 187.3 | 192.5 |
| Stature (`BMXHT`) | F | 3435 | 144.6 | 149.7 | 161.2 | 172.5 | 177.3 |

### NHANES 2017-March 2020 (pre-pandemic), adults 18+, survey-weighted (`WTMECPRP`)

Units: cm; body mass in kg.

| Variable | Sex | n | P1 | P5 | P50 | P95 | P99 |
|---|---|---|---|---|---|---|---|
| Waist circumference (`BMXWAIST`) | M | 4154 | 70.7 | 77.7 | 101.3 | 132.0 | 149.1 |
| Waist circumference (`BMXWAIST`) | F | 4295 | 67.5 | 72.4 | 96.4 | 128.7 | 146.4 |
| Hip circumference (`BMXHIP`) | M | 4152 | 84.7 | 89.5 | 103.6 | 127.6 | 144.4 |
| Hip circumference (`BMXHIP`) | F | 4311 | 83.7 | 88.4 | 106.9 | 139.2 | 157.3 |
| Body mass (`BMXWT`) | M | 4286 | 54.9 | 61.9 | 87.1 | 129.6 | 159.2 |
| Body mass (`BMXWT`) | F | 4525 | 44.5 | 49.8 | 73.5 | 120.3 | 155.9 |
| Stature (`BMXHT`) | M | 4281 | 157.4 | 163.1 | 175.0 | 187.3 | 193.1 |
| Stature (`BMXHT`) | F | 4523 | 144.9 | 149.9 | 161.2 | 172.4 | 177.7 |

## 3. What the numbers mean for RideBelt
| Design question | Relevant values | Observation |
|---|---|---|
| **Design rider mass** (REQ-L2 uses 140 kg, with 160 kg checked) | NHANES 2021–2023 P99 body mass: **155.8 kg (M), 146.6 kg (F)**; 2017–2020: 159.2 kg (M), 155.9 kg (F) | 140 kg is below the civilian P99 for both sexes. The **160 kg check case is roughly the civilian P99** and is the better basis if the rating is meant to cover 99% of adults. Flag for the requirements owner and engineer review (affects REQ-L2 and the arrest-model inputs) |
| **Hip Belt circumference range** (belt sits low on the pelvis, so hip circumference is the closest NHANES proxy) | NHANES P1–P99 hip circumference: **84.0–144.6 cm (M), 84.5–156.2 cm (F)** | The largest hips are in **women**, not men. REQ-F1's "5th-percentile female to 99th-percentile male" wording would miss the female P95–P99 range (about 138–156 cm). Suggest REQ-F1 cover the **99th percentile of both sexes** |
| Waist circumference (shoulder-module and harness fit; also a worst-case belt position check) | NHANES P1–P99: 70.4–149.2 cm (M), 67.2–143.4 cm (F) | A belt that fits from about 67 to 157 cm of girth needs **several sizes** with overlapping adjustment (for `sizing-001`) |
| Seated hip breadth (tether exit spacing; fit between seat sides and RAS side anchors) | ANSUR II P99: 462 mm (M), 485 mm (F) | Military-only data. Civilian large-body hip breadth is likely wider; no open civilian seated-breadth data was found in these sources |
| Thigh circumference (center strap and seat clearance) | ANSUR II P1–P99: 497–774 mm (M), 495–757 mm (F) | Military sample, likely an underestimate for civilians (see §4) |
| **Integrated Harness torso proxies** | ANSUR II waist back length (C7 to waist): 365–548 mm; waist front length, sitting (suprasternale to waist): 304–459 mm (P1 F to P99 M) | Front and back strap length ranges of about **15–18 cm** of adjustment across the population; candidate inputs for `design-002` and `design-003` |
| **Convertible Center Strap, W (wearable) length** | ANSUR II crotch length, omphalion (front waist via crotch to back waist): **523–739 mm** (P1–P99, both sexes) | Wearable-mode length needs about 22 cm of adjustment between the smallest and largest riders (input for `design-004`), before adding seated-posture and padding allowances |
| Sitting height (headroom; shoulder-strap routing under OTSRs) | ANSUR II P1–P99: 784–1001 mm | Military sample; NHANES does not measure sitting height |

## 4. Known population biases and limits
- **ANSUR II is a military sample.** Soldiers must meet fitness and body-composition standards, so ANSUR II **under-represents large and heavy bodies**. Compare the P99 hip circumference: 121 cm (F, ANSUR II) vs. 156 cm (F, NHANES). Treat ANSUR II upper percentiles as **lower bounds** for the civilian population. Its strength is the detailed seated, torso and crotch measurements that NHANES lacks.
- **ANSUR II ages and demographics** reflect Army personnel in 2010–2012 (mostly ages about 17–58, and a different demographic mix from the general population). Older riders and people with disabilities are under-represented.
- **NHANES measures fewer dimensions** (no seated breadths, torso lengths or thigh circumference in these cycles) and is **US-only**. Other countries' populations differ. For example, many East Asian populations are smaller on average, and the size range should be checked against local data before use outside the US.
- **NHANES hip and waist** are measured standing, at defined landmarks (see the BMX documentation). The Hip Belt sits low on a **seated** pelvis, where soft tissue redistributes, so seated girths may differ. Physical fit trials (T-F2, after the MVP gate) are still needed.
- **No standard errors** are reported here. Extreme percentiles (P1, P99) have the largest sampling uncertainty, especially in the smaller NHANES subgroups.
- **Children are out of scope here.** See `ridebelt-anthro-002`.

## 5. Suggested follow-ups (for the requirements owner, not changed here)
1. Revisit the **REQ-L2 design mass**: 140 kg vs. the civilian P99 of about 156–159 kg.
2. Reword **REQ-F1** to cover the 99th percentile of **both** sexes (largest hips are female).
3. Use these ranges in `sizing-001` (size chart), `design-001` to `design-004` (belt, harness, shoulder module, center strap) and `model-005` (mass range in the uncertainty study).
