# The Daily Line — NBA Opening Day Shadow Forecast (Frozen v0.1)

- **Date:** Tuesday 2026-10-20, 2026–27 regular-season opening slate.
- **Status:** first pregame research/shadow baseline; **UNCALIBRATED / NOT PRODUCTION**; no wager recommendation, PASS or claimed expected value.
- **As-of source cut:** 2026-10-20 18:23:00 UTC (11:23 Pacific), before Boston @ Detroit 19:00 UTC opening tip.
- **Simulation run/freeze:** 2026-10-20 18:26:29 UTC (11:26:29 Pacific).
- **Model version:** `nba-opening-possession-heuristic-0.1`; deterministic RNG seed `20261020`; 90,000 draws/game.
- **Archive hash (complete full input+output JSON):** SHA-256 `3899bb9697e50d0c69c341301881617e47efc98d560c1676545e3cdf16788333`
- **Model script hash:** SHA-256 `1df27f72bc924cc191702ffed1e25b3c145c2f16ae076456e5fdaf1966c89797`.
- **Source facts:** 2025–26 Basketball-Reference team and individual regular-season histories, RealGM team advanced stats, official NBA Oct. 20 1:45PM EDT injury bulletin, and newspaper-identified **projected** (not confirmed) starters.
- **Predictive isolation:** zero betting lines, consensus forecasts, third-party models or fantasy predictions used. No market fair comparisons, fees or closing prices have been performed.

## Pre-market frozen forecasts

All scores and totals are simulation expectations including approximate overtime adjustment when necessary. Player simulations in the full JSON are regulation-only.

| Away at Home | Away win % | Home win % | Fair away ML | Fair home ML | Projected regulation points | Fair home margin | Full-game total |
|---|---:|---:|---:|---:|---|---:|---:|
| BOS @ DET | 43.97% | 56.03% | +127 | -127 | BOS 109.83, DET 112.70 | DET +2.9 | 222.98 |
| PHI @ NYK | 40.41% | 59.59% | +147 | -147 | PHI 112.58, NYK 117.41 | NYK +4.8 | 230.43 |
| OKC @ SAS | 50.26% | 49.74% | -101 | +101 | OKC 113.10, SAS 112.92 | SAS -0.2 | 226.45 |

80% simulated intervals on **total**: BOS-DET 196–251; PHI-NYK 203–259; OKC-SAS 199–254. These are **model-draw intervals**, not calibrated uncertainty or verified confidence bounds.

### Player outcomes (joint minutes/attempts/assists/rebounds simulation; expected per game)

| Match | Player | Expected PTS | REB | AST | 3PM |
|---|---|---:|---:|---:|---:|
| BOS-DET | Jayson Tatum | 24.0 | 9.7 | 4.9 | 3.2 |
| BOS-DET | Paul George | 17.3 | 5.0 | 3.2 | 2.6 |
| BOS-DET | Cade Cunningham | 24.5 | 5.7 | 11.4 | 2.1 |
| BOS-DET | Jalen Duren | 20.0 | 11.5 | 2.5 | 0.0 |
| PHI-NYK | Tyrese Maxey | 21.7 | 4.0 | 5.3 | 2.5 |
| PHI-NYK | Jaylen Brown | 23.1 | 6.8 | 4.1 | 1.7 |
| PHI-NYK | LeBron James | 15.7 | 5.9 | 5.7 | 1.1 |
| PHI-NYK | Joel Embiid | 19.8 | 7.1 | 3.0 | 1.1 |
| PHI-NYK | Jalen Brunson | 27.1 | 3.3 | 7.7 | 2.6 |
| PHI-NYK | Karl-Anthony Towns | 22.1 | 12.7 | 3.6 | 1.6 |
| OKC-SAS | Shai Gilgeous-Alexander | 29.1 | 4.4 | 6.4 | 1.7 |
| OKC-SAS | Chet Holmgren | 17.4 | 9.8 | 1.8 | 1.4 |
| OKC-SAS | Stephon Castle | 17.9 | 5.8 | 7.6 | 1.4 |
| OKC-SAS | Victor Wembanyama | 25.8 | 12.2 | 3.1 | 2.1 |

### Model assumptions and methodological warning

- Historical 2025–26 team base: BOS OffRtg120.8 DefRtg112.7 Pace94.8; DET117.9/109.7/99.3; PHI115.4/115.5/99.4; NYK119.8/113.3/96.8; OKC118.9/107.7/99.3; SAS119.6/111.3/99.9.
- Historical factual team four factors (team eFG, turnovers, offensive boards, FT/FGA, 3PA/FGA and opponent defensive counterparts) drive event-level shooting/turnover/FT/rebounding opportunity distributions.
- In-house **heuristic**, not statistically trained or validated: opponent-adjusted expected offense = adjusted off-rating × opponent adjusted defensive rating / 115.7; shared possessions from blended 2025–26 paces; full margin home-court adjustment +2.4 points; with-star season subset rates partially pooled using GP/(GP+30); offseason roster offsets assumed by analyst and recorded in the full JSON; player minutes, roles, attempts, binomial conversion and shared game shooting variations used for player distributions.
- Major roster change: Boston Jaylen Brown out, Paul George and Mitchell Robinson in; Philadelphia Jaylen Brown and LeBron James in, Paul George out; Detroit John Collins for Tobias Harris, who is now at SAS but listed OUT. Historical ratings are not assumed transferable without adjustments.
- These adjustments are uncertain, not causal learned coefficients. Training/backtesting, optimizer, shooting location, play types, defended shot distance, WOWY/lineup stint samples, assists opportunities, rebound chances, provider tracking, injury scenarios, official confirmed lineups, out-of-sample variance calibration, and player prop OT settlement are **not fully collected or implemented**. A true “full model” is **not** claimed.
- Neither opening-day regular-season game results nor market prices were known or accessed by the simulator as of source cut. Closing lines and outcomes must be appended later **without changing** this frozen snapshot.
- **Gate:** SHADOW / WATCH-RESEARCH only; no PASS, buy threshold or EV without permitted model readiness, verified price/contract terms and an independently frozen forecast.
- Modeling caveat: shared possessions/shooting and team rebounds/assists are simulated together, but exact possession-by-possession event accounting and prop OT are not yet consistent/validated.

## Source links

- [Basketball Reference: league 2025-26](https://www.basketball-reference.com/leagues/NBA_2026.html)
- [BOS](https://www.basketball-reference.com/teams/BOS/2026.html), [DET](https://www.basketball-reference.com/teams/DET/2026.html), [PHI](https://www.basketball-reference.com/teams/PHI/2026.html), [NYK](https://www.basketball-reference.com/teams/NYK/2026.html), [OKC](https://www.basketball-reference.com/teams/OKC/2026.html), [SAS](https://www.basketball-reference.com/teams/SAS/2026.html)
- [NBA injury report, Oct. 20, 2026 at 1:45PM EDT](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-20_01_45PM.pdf)
- [Spurs/Thunder starters projected](https://www.expressnews.com/sports/spurs/article/san-antonio-spurs-okc-thunder-how-to-watch-22482941.php)
- [2026–27 opening-day preview](https://www.brewhoop.com/general/77668/nba-opening-day-celtics-knicks-thunder)

**Immutable restatement policy:** preserve this v0.1 alongside later factual news, revised model, market-only checks and postgame results. **Do not replace it.**
