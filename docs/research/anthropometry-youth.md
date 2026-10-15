# Child and Youth Anthropometry for Minimum-Rider Rules (Ages 6–17)

> Status: research input (task `ridebelt-anthro-002`) · License: CC BY 4.0 · Prepared with AI assistance (Claude Code)
>
> **This is input data for REQ-F2 (minimum rider height and mass). It is not a recommendation that children use RideBelt.** RideBelt is DRAFT and not for use by anyone (see the [Safety Notice](../../SAFETY-NOTICE.md)). Whether, and from what size, any child could ever use a backup restraint is a decision for the credentialed engineering review at the MVP gate and for ride manufacturers and regulators.

## 1. Source and method
| Item | Detail |
|---|---|
| Data | **NHANES 2021–2023** (`BMX_L`, `DEMO_L`), cross-checked against **NHANES 2017–March 2020** (`P_BMX`, `P_DEMO`). Both are from CDC/NCHS: US federal government data, public domain in the US ([17 U.S.C. §105](https://www.law.cornell.edu/uscode/text/17/105)) |
| Variables | `RIDAGEYR` age; `RIAGENDR` sex; `BMXHT` standing height (stature); `BMXWT` weight; `BMXWAIST` waist circumference; `BMXHIP` hip circumference; `BMXLEG` upper leg length. See the [BMX_L documentation](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.htm) and [P_BMX documentation](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/P_BMX.htm) |
| Population | Ages 6–17 at screening, both sexes; 1,731 children in 2021–2023 |
| Weighting | MEC exam weights (`WTMEC2YR`, `WTMECPRP`) per the [NHANES weighting guidance](https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx). Percentiles come from the weighted cumulative distribution; no standard errors were computed. Cells with fewer than 30 children show "n<30" |
| Ride height limits | 42, 48 and 54 in. (106.7, 121.9 and 137.2 cm): common posted minimums for family rides, larger coasters and the most intense rides respectively. They are used here only as reference bands |
| Reproduce | [anthropometry/compute_youth.py](anthropometry/compute_youth.py) (uses the same data files as the adult analysis in [anthropometry-adult.md](anthropometry-adult.md); raw files are not committed) |

**Coverage limits in NHANES:** hip circumference is recorded only from **age 12**, and upper leg length only from **age 8**. NHANES has **no seated or torso-length measures** for children, so stature is the only torso proxy here. The CDC growth-chart percentile files would add smoothed stature and weight curves, but the CDC site refused automated download during this work. They can be added later from the [CDC growth chart data files page](https://www.cdc.gov/growthcharts/cdc-data-files.htm).

## 2. Results
### Share of children reaching each height limit, by age — NHANES 2021–2023

Weighted percentage of children at each age whose measured stature is at or above the limit.

| Age | n | ≥ 42 in | ≥ 48 in | ≥ 54 in |
|---|---|---|---|---|
| 6 | 120 | 99% | 35% | 0% |
| 7 | 145 | 100% | 73% | 4% |
| 8 | 162 | 100% | 96% | 23% |
| 9 | 147 | 100% | 100% | 51% |
| 10 | 149 | 100% | 100% | 80% |
| 11 | 141 | 100% | 100% | 95% |
| 12 | 155 | 100% | 100% | 99% |
| 13 | 148 | 100% | 100% | 100% |
| 14 | 134 | 100% | 100% | 99% |
| 15 | 144 | 100% | 100% | 100% |
| 16 | 148 | 100% | 100% | 100% |
| 17 | 129 | 100% | 100% | 100% |

### By ride height band (ages 6–17, both sexes) — NHANES 2021–2023

| Height band | Measure | n | P5 | P50 | P95 |
|---|---|---|---|---|---|
| < 42 in (< 106.7 cm) | Age, years | 1 | n<30 | n<30 | n<30 |
| < 42 in (< 106.7 cm) | Body mass, kg | 1 | n<30 | n<30 | n<30 |
| < 42 in (< 106.7 cm) | Waist circumference, cm | 1 | n<30 | n<30 | n<30 |
| < 42 in (< 106.7 cm) | Hip circumference, cm (ages 12+ only) | 0 | n<30 | n<30 | n<30 |
| 42–47.9 in (106.7–121.9 cm) | Age, years | 123 | 6 | 6 | 8 |
| 42–47.9 in (106.7–121.9 cm) | Body mass, kg | 123 | 17.3 | 21.5 | 32.3 |
| 42–47.9 in (106.7–121.9 cm) | Waist circumference, cm | 119 | 49.0 | 54.7 | 70.5 |
| 42–47.9 in (106.7–121.9 cm) | Hip circumference, cm (ages 12+ only) | 0 | n<30 | n<30 | n<30 |
| 48–53.9 in (121.9–137.2 cm) | Age, years | 373 | 6 | 8 | 10 |
| 48–53.9 in (121.9–137.2 cm) | Body mass, kg | 373 | 22.8 | 28.6 | 42.3 |
| 48–53.9 in (121.9–137.2 cm) | Waist circumference, cm | 367 | 52.4 | 59.7 | 79.2 |
| 48–53.9 in (121.9–137.2 cm) | Hip circumference, cm (ages 12+ only) | 3 | n<30 | n<30 | n<30 |
| ≥ 54 in (≥ 137.2 cm) | Age, years | 1225 | 9 | 13 | 17 |
| ≥ 54 in (≥ 137.2 cm) | Body mass, kg | 1224 | 33.0 | 55.6 | 99.1 |
| ≥ 54 in (≥ 137.2 cm) | Waist circumference, cm | 1188 | 59.8 | 75.2 | 109.4 |
| ≥ 54 in (≥ 137.2 cm) | Hip circumference, cm (ages 12+ only) | 816 | 78.9 | 93.8 | 120.8 |

### By ride height band (ages 6–17, both sexes) — NHANES 2017–March 2020 (cross-check)

| Height band | Measure | n | P5 | P50 | P95 |
|---|---|---|---|---|---|
| < 42 in (< 106.7 cm) | Age, years | 3 | n<30 | n<30 | n<30 |
| < 42 in (< 106.7 cm) | Body mass, kg | 3 | n<30 | n<30 | n<30 |
| < 42 in (< 106.7 cm) | Waist circumference, cm | 2 | n<30 | n<30 | n<30 |
| < 42 in (< 106.7 cm) | Hip circumference, cm (ages 12+ only) | 0 | n<30 | n<30 | n<30 |
| 42–47.9 in (106.7–121.9 cm) | Age, years | 280 | 6 | 6 | 8 |
| 42–47.9 in (106.7–121.9 cm) | Body mass, kg | 280 | 17.4 | 21.8 | 29.9 |
| 42–47.9 in (106.7–121.9 cm) | Waist circumference, cm | 267 | 48.2 | 55.0 | 67.0 |
| 42–47.9 in (106.7–121.9 cm) | Hip circumference, cm (ages 12+ only) | 0 | n<30 | n<30 | n<30 |
| 48–53.9 in (121.9–137.2 cm) | Age, years | 722 | 6 | 8 | 10 |
| 48–53.9 in (121.9–137.2 cm) | Body mass, kg | 721 | 22.3 | 28.4 | 42.7 |
| 48–53.9 in (121.9–137.2 cm) | Waist circumference, cm | 680 | 52.0 | 59.6 | 80.7 |
| 48–53.9 in (121.9–137.2 cm) | Hip circumference, cm (ages 12+ only) | 3 | n<30 | n<30 | n<30 |
| ≥ 54 in (≥ 137.2 cm) | Age, years | 2191 | 9 | 13 | 17 |
| ≥ 54 in (≥ 137.2 cm) | Body mass, kg | 2189 | 33.2 | 56.8 | 96.9 |
| ≥ 54 in (≥ 137.2 cm) | Waist circumference, cm | 2127 | 59.5 | 75.9 | 108.7 |
| ≥ 54 in (≥ 137.2 cm) | Hip circumference, cm (ages 12+ only) | 1394 | 77.3 | 94.7 | 119.8 |

### By age group and sex — NHANES 2021–2023

| Measure | Age | Sex | n | P5 | P50 | P95 |
|---|---|---|---|---|---|---|
| Stature, cm | 6–8 | M | 201 | 113.1 | 127.4 | 140.3 |
| Stature, cm | 6–8 | F | 226 | 113.9 | 126.8 | 142.1 |
| Stature, cm | 9–11 | M | 230 | 127.5 | 143.5 | 158.0 |
| Stature, cm | 9–11 | F | 207 | 131.7 | 146.2 | 163.0 |
| Stature, cm | 12–14 | M | 211 | 149.3 | 165.3 | 180.0 |
| Stature, cm | 12–14 | F | 226 | 144.6 | 158.1 | 167.8 |
| Stature, cm | 15–17 | M | 210 | 162.5 | 174.2 | 187.7 |
| Stature, cm | 15–17 | F | 211 | 150.9 | 160.5 | 171.7 |
| Body mass, kg | 6–8 | M | 202 | 19.4 | 26.8 | 41.9 |
| Body mass, kg | 6–8 | F | 226 | 18.5 | 26.3 | 44.4 |
| Body mass, kg | 9–11 | M | 230 | 25.7 | 38.1 | 72.3 |
| Body mass, kg | 9–11 | F | 207 | 28.2 | 41.4 | 71.8 |
| Body mass, kg | 12–14 | M | 213 | 38.3 | 57.3 | 103.4 |
| Body mass, kg | 12–14 | F | 225 | 38.5 | 53.7 | 95.5 |
| Body mass, kg | 15–17 | M | 210 | 49.2 | 70.8 | 112.4 |
| Body mass, kg | 15–17 | F | 211 | 45.0 | 59.3 | 103.9 |
| Waist circumference, cm | 6–8 | M | 194 | 50.8 | 57.5 | 75.8 |
| Waist circumference, cm | 6–8 | F | 222 | 50.3 | 58.4 | 82.4 |
| Waist circumference, cm | 9–11 | M | 228 | 54.1 | 66.1 | 100.2 |
| Waist circumference, cm | 9–11 | F | 205 | 55.6 | 68.7 | 92.4 |
| Waist circumference, cm | 12–14 | M | 204 | 62.2 | 73.6 | 114.2 |
| Waist circumference, cm | 12–14 | F | 211 | 62.8 | 75.0 | 104.2 |
| Waist circumference, cm | 15–17 | M | 206 | 65.5 | 80.2 | 117.3 |
| Waist circumference, cm | 15–17 | F | 205 | 65.0 | 78.3 | 109.7 |
| Hip circumference, cm (ages 12+ only) | 12–14 | M | 201 | 74.8 | 90.0 | 120.8 |
| Hip circumference, cm (ages 12+ only) | 12–14 | F | 211 | 79.0 | 92.1 | 116.3 |
| Hip circumference, cm (ages 12+ only) | 15–17 | M | 203 | 82.0 | 96.8 | 123.0 |
| Hip circumference, cm (ages 12+ only) | 15–17 | F | 204 | 84.9 | 96.2 | 123.8 |
| Upper leg length, cm (ages 8+ only) | 6–8 | M | 81 | 26.8 | 30.0 | 34.3 |
| Upper leg length, cm (ages 8+ only) | 6–8 | F | 78 | 26.7 | 30.8 | 34.4 |
| Upper leg length, cm (ages 8+ only) | 9–11 | M | 225 | 29.5 | 34.0 | 39.8 |
| Upper leg length, cm (ages 8+ only) | 9–11 | F | 201 | 29.7 | 34.6 | 39.2 |
| Upper leg length, cm (ages 8+ only) | 12–14 | M | 200 | 34.7 | 40.0 | 44.5 |
| Upper leg length, cm (ages 8+ only) | 12–14 | F | 213 | 33.1 | 37.1 | 41.5 |
| Upper leg length, cm (ages 8+ only) | 15–17 | M | 202 | 38.0 | 41.9 | 46.9 |
| Upper leg length, cm (ages 8+ only) | 15–17 | F | 203 | 34.4 | 37.7 | 42.2 |

## 3. How the height limits map to body size
| Ride height limit | Who reaches it (NHANES 2021–2023) | Body size of children in the band just above the limit |
|---|---|---|
| **42 in** | Almost every child aged 6 and over (99% at age 6) | 42–47.9 in band: median about 21.5 kg; waist P5–P95 about 49–71 cm (ages 6–8 dominate; the band also contains under-6s, who are outside this dataset's 6–17 scope) |
| **48 in** | About 35% at age 6, 73% at 7, 96% at 8, essentially all from 9 | 48–53.9 in band: median about 28.6 kg (P5–P95 about 23–42 kg); waist P5–P95 about 52–79 cm; ages mostly 6–10 |
| **54 in** | About 23% at age 8, 51% at 9, 80% at 10, 95% at 11, essentially all from 12 | ≥ 54 in band: body mass P5–P95 about 33–99 kg; waist about 60–109 cm; hip (ages 12+) about 79–121 cm |

The 2017–2020 cross-check gives very similar band values: P50 body mass within 1.2 kg and P50 waist within 0.7 cm in every band.

## 4. Observations for REQ-F2 (inputs only)
- **Girth vs. adult sizing:** the smallest adult belt size implied by [anthropometry-adult.md](anthropometry-adult.md) is about 67 cm waist (adult female P1). Many children in the 48–53.9 in band have **waists below 60 cm** (median about 60 cm, P5 about 52 cm). Adult sizes would not fit much of this group, so any youth use would need separate sizes and its own analysis.
- **Mass vs. the load model:** children are far lighter than the 140–160 kg design rider (median about 29 kg in the 48–53.9 in band). Lighter riders lower tether loads, but **injury tolerance in children differs from adults**. The adult biomechanics inputs (`ridebelt-biomech-001`) can't be applied to children without specific evidence.
- **Shape changes with age:** for younger children, pelvis shape and the hip-to-waist relationship differ from adults. A low hip belt relies on the adult pelvic shape to stay down (REQ-L6), which may not hold for small children. This needs engineering review and dynamic testing with child ATDs before any youth rating is considered.
- **Body-size spread within a height band is wide** (P95 mass is roughly 1.5–3× P5), so a height limit alone does not bound belt girth or mass.
- **Incident relevance:** children appear often in the incident review ([incidents.md](incidents.md)). That makes this question important, but it does not by itself justify youth use.

## 5. Limitations
- US-only data; other populations differ.
- Standing girths, not seated; no torso, seated or thigh measures for children.
- Ride height bands start at age 6 in this dataset, so the "< 42 in" and lower part of the "42–47.9 in" bands are under-represented (most children under 42 in are younger than 6).
- No standard errors; small cells (n<30) are suppressed.

## Sources
- NHANES 2021–2023 Body Measures (`BMX_L`): https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.htm
- NHANES 2021–2023 Demographics (`DEMO_L`): https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.htm
- NHANES 2017–March 2020 Body Measures (`P_BMX`): https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/P_BMX.htm
- NHANES weighting tutorial: https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx
- 17 U.S.C. §105 (US government works): https://www.law.cornell.edu/uscode/text/17/105
