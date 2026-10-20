# NBA Opening Day — independent shadow v0.2 (frozen, exploratory)
**Date:** 2026-10-20; **model:** `nba-open-reconciled-zones-v0.2-experimental`; **run:** 2026-10-20 18:53:12 UTC (11:53:12 PDT). **Input observation cut:** 18:50 UTC. **First scheduled tip:** 19:00 UTC. **Seed:** 20261022; **simulation draws:** 72,000 per game.

**State:** initial before-tipoff v0.2 research forecast. **Uncalibrated and SHADOW only. No PASS, no EV, no sportsbook/market quotes/consensus or external forecasts used.** Original [v0.1](2026-10-20-opening-day-shadow-v0.1.md) remains immutable. The full reproducible v0.2 source, tests, original v0.1 input/output files and CSV exports were created as a dated downloadable research bundle in the project conversation; this GitHub record indexes the first v0.2 forecast without importing outcomes.

## Independent premarket simulation (full game with heuristic OT)

| Game | v0.1 home win % | v0.2 home win % | v0.2 away win % | v0.2 projected away / home points | v0.2 home fair American | Full-game total | Home expected margin | Full-game total 80% *simulation* interval |
|---|---:|---:|---:|---|---:|---:|---:|---|
| BOS @ DET | 56.03 | **56.9236** | 43.0764 | 110.16 / 113.39 | -132 | 223.55 | +3.23 | 197–251 |
| PHI @ NYK | 59.59 | **65.8792** | 34.1208 | 110.08 / 118.00 | -193 | 228.09 | +7.92 | 201–256 |
| OKC @ SAS | 49.74 | **48.6153** | 51.3847 | 113.88 / 113.14 | +106 | 227.02 | -0.75 | 200–254 |

**NOTE:** fair American prices are calculated *from* frozen model probability; they are **not real market quotations**. Simulation intervals are **not calibrated confidence intervals**.

### Selected player expected regulation statistics (same joint simulations)

| Game | Player | PTS | REB | AST | STL | BLK | custom fantasy |
|---|---|---:|---:|---:|---:|---:|---:|
| BOS–DET | Jayson Tatum | 23.57 | 9.62 | 4.67 | 1.06 | 0.19 | 43.51 |
| BOS–DET | Cade Cunningham | 23.86 | 5.89 | 9.08 | 1.11 | 0.51 | 46.08 |
| BOS–DET | Jalen Duren | 18.28 | 11.94 | 1.95 | 0.67 | 0.55 | 37.38 |
| PHI–NYK | Tyrese Maxey | 20.32 | 4.40 | 4.41 | 1.56 | 0.60 | 36.73 |
| PHI–NYK | Jaylen Brown | 20.74 | 7.47 | 3.46 | 0.83 | 0.30 | 35.35 |
| PHI–NYK | Joel Embiid | 17.69 | 7.76 | 2.47 | 0.47 | 0.84 | 32.41 |
| PHI–NYK | Jalen Brunson | 25.25 | 3.63 | 6.10 | 0.65 | 0.06 | 38.63 |
| PHI–NYK | Karl-Anthony Towns | 20.27 | 13.92 | 2.88 | 0.78 | 0.33 | 42.11 |
| OKC–SAS | Shai Gilgeous-Alexander | 28.16 | 4.50 | 5.54 | 1.13 | 0.67 | 45.20 |
| OKC–SAS | Victor Wembanyama | 23.09 | 13.35 | 2.51 | 0.81 | 2.58 | 50.71 |

Custom fantasy research scoring = 1×PTS+1.2×REB+1.5×AST+3×STL+3×BLK−1×TO, **not** a declared platform settlement. Player simulations regulation-only, so not comparable to full-game player prop markets until OT handling is corrected.

## What v0.2 actually adds

1. Independent 2025-26 team efficiency/four-factor and player shooting inputs, no outside predictions; original v0.1 speculative and unverified with/without cohort splits **removed** rather than treated as real.
2. Per-game player-minute draws **exactly summing to 240** for each team in regulation. Named players individually capped at 43; residual **Other** is a GROUP of bench players.
3. Nine verifiable 2025-26 **regular-season** shooting-by-distance player profiles (four two-point zones), plus Boston opponent defensive-zone data; otherwise documented 2P-only or overall opponent eFG fallback.
4. Shared possession count, draws for shot/FT attempts and conversions, team/player points summing exactly, assists allocated from made FGs, turnovers allocated to players, steals bounded by opponent turnovers, rebounds bounded by simulated missed-shot chances, blocks bounded by opponent missed 2P opportunities.
5. Player steals, blocks, turnovers, fouls and fantasy point *distributions*, PRA, alternate counts and double-doubles. Season-specific historical player inputs when verified; missing players' defensive rates explicitly labeled **generic priors**.
6. Conditional example for Joel Embiid at 24 rather than projected 29 minutes. It is a **hypothetical** minutes scenario, not a sourced restriction or probability weighting. Separate conditional forecast recorded.
7. Structural assertions and five Python regression checks **passed**: original v0.1 SHA-256 unchanged, input/provenance validation, exact possession/rotation/event accounting, output-probability identities, conditional scenario structure. Separate scoring harness created; only toy smoke-test evaluations run, **no retrospective calibration claimed**.

## Hard limitations and source quality

- **Missing:** actual historical five-man lineup possession history, validated WOWY changes, true potential assists/optical touches/rebound chances, accurate opponent shot-zone defense for all teams, defensive coverage classifications, longitudinal leak-free retrospective replay and statistically calibrated probabilities.
- Lineup minutes and role shares remain **analyst assumptions**. Early-season roster/rotation adjustments remain uncertain; do not interpret NBA 2025-26 aggregate as 2026-27 current roster talent.
- Foul trouble is capped at six but does not actually reduce player minutes in simulated future possessions. OT extends team score only, **not player distributions**.
- A model correction can shift PHI–NYK probabilities by several points; this is model uncertainty, not proven skill improvement. Retain all predictions for future fair scoring.
- As of forecast no actual outcomes, sportsbook prices, no-vig probabilities, fee-adjusted EV, market gates or CLV have been analyzed.

## Evidence and reproducibility hashes

- frozen original v0.1 JSON SHA-256: `3899bb9697e50d0c69c341301881617e47efc98d560c1676545e3cdf16788333` (unchanged)
- v0.2 Python model SHA-256: `cf26a82ec4e1354c8bef75a412580b03e5a15b0fa1bb6f6fd369b4cb1ada8381`
- v0.2 output JSON SHA-256: `442064840131b732cc15c80e7a4f6e38b81af7657b0ba8c45478c38142355674`

Raw historical source references: [2025-26 league stats](https://www.basketball-reference.com/leagues/NBA_2026.html), [2025-26 season player shooting](https://www.basketball-reference.com/leagues/NBA_2026_shooting.html), [BOS](https://www.basketball-reference.com/teams/BOS/2026.html), [DET](https://www.basketball-reference.com/teams/DET/2026.html), [PHI](https://www.basketball-reference.com/teams/PHI/2026.html), [NYK](https://www.basketball-reference.com/teams/NYK/2026.html), [OKC](https://www.basketball-reference.com/teams/OKC/2026.html), [SAS](https://www.basketball-reference.com/teams/SAS/2026.html), [NBA injury report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-20_01_45PM.pdf). Source statistics were used for manual/private shadow research, **not represented as cleared for commercial redistribution**.

### Frozen-prediction preservation

The next official outcome review must preserve this original run as-is and write a separate grading entry. Do **not** mutate the independent probabilities to reflect lines, market reactions or completed game stats. No PASS was issued.