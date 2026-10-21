# The Daily Line | NBA Full Slate Shadow Audit | 2026-10-21

**Original pregame v0.2.1 freeze:** 2026-10-21 **21:22:11 UTC / 2:22:11 PM PDT**, first tip **4:00 PM PDT**. Facts cutoff **20:45 UTC / 1:45 PM PDT** official NBA injury bulletin, with some season histories observed before that. **60,000 simulated draws/game**, deterministic seed `20261021`, 11 games/22 teams, 129 named player output rows. No actual game outcomes, external projections, betting markets, implied odds or closing lines were consumed. Reuses the former v0.2 event simulation core, with 2025–26 roster-linked inputs and new v0.2.1 assumptions. **NOT TRAINED OR CALIBRATED; NO PASS**.

**Integrity:** Full original prediction JSON SHA-256 `5f684c3a9557c8e8af081ab7595f482cc6a4abac6df832daa3e1e938014fae8c`. This archive is append-only; scenario research was computed in a separate file and does not alter original probabilities.

## 1. Independent win probabilities, scores, fair odds

| Away @ Home | Predicted winner | Model P(win) | Expected away–home points | Expected total | Expected home margin | Model fair American (winner) | Gate |
|---|---|---:|---|---:|---:|---:|---|
| MIL@WAS | **Wizards** | 65.0% | 112.1–119.6 | 231.7 | +7.5 | -185 | WATCH-research |
| ATL@ORL | **Magic** | 51.4% | 114.4–115.1 | 229.4 | +0.7 | -106 | WATCH-research |
| CHA@BKN | **Hornets** | 59.7% | 114.0–109.3 | 223.3 | -4.6 | -148 | WATCH-research |
| CHI@TOR | **Raptors** | 73.8% | 109.9–122.2 | 232.2 | +12.3 | -282 | WATCH-research |
| MIN@MIA | **Heat** | 63.3% | 115.5–122.1 | 237.6 | +6.6 | -172 | WATCH-research |
| IND@NOP | **Pelicans** | 55.6% | 115.6–118.3 | 233.9 | +2.7 | -125 | WATCH-research |
| UTA@MEM | **Jazz** | 53.0% | 119.8–118.3 | 238.0 | -1.5 | -113 | WATCH-research |
| DAL@HOU | **Rockets** | 68.3% | 108.8–118.0 | 226.8 | +9.2 | -216 | WATCH-research |
| PHX@POR | **Trail Blazers** | 53.3% | 111.7–113.3 | 225.0 | +1.6 | -114 | WATCH-research |
| GSW@LAL | **Lakers** | 65.2% | 109.2–116.7 | 225.9 | +7.6 | -187 | WATCH-research |
| SAC@LAC | **Clippers** | 59.5% | 110.0–114.5 | 224.5 | +4.5 | -147 | WATCH-research |

Home margin = projected HOME points minus AWAY points. Positive favors home. Quoted American odds are **fair odds mathematically implied by our independent p**, not purchasable sportsbook/exchange prices or approved price thresholds.

## 2. Uncertainty

| Matchup | 10–90% total interval (simulation) | Model home P(win) | ±4 OffRtg point/team assumption sensitivity (home P) |
|---|---|---:|---:|
| MIL@WAS | 205–259 | 65.0% | 52.5%–76.3% |
| ATL@ORL | 202–257 | 51.4% | 39.9%–63.9% |
| CHA@BKN | 196–251 | 40.3% | 29.1%–52.3% |
| CHI@TOR | 205–260 | 73.8% | 62.4%–82.0% |
| MIN@MIA | 210–265 | 63.3% | 50.9%–73.7% |
| IND@NOP | 207–261 | 55.6% | 42.6%–67.7% |
| UTA@MEM | 211–266 | 47.0% | 34.4%–60.2% |
| DAL@HOU | 200–254 | 68.3% | 56.7%–77.5% |
| PHX@POR | 198–252 | 53.3% | 41.2%–64.6% |
| GSW@LAL | 199–253 | 65.2% | 52.9%–75.3% |
| SAC@LAC | 198–252 | 59.5% | 47.2%–71.8% |

**Warning:** 10–90% simulation quantiles are NOT calibrated uncertainty or a confidence interval. Sensitivity varies each side’s heuristic offensive adjustment by opposing ±4 points per 100 possessions; this is a scenario stress test, not an estimated credible probability range.

## 3. Key player projections (REGULATION only)

| Match | Player | Min | PTS | REB | AST | 3PM | Stl | Blk |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| MIL@WAS | Trae Young | 33.0 | 22.2 | 2.6 | 8.4 | 3.4 | 1.1 | 0.3 |
| MIL@WAS | Anthony Davis | 32.0 | 19.2 | 11.5 | 2.3 | 0.9 | 0.7 | 0.5 |
| ATL@ORL | Jalen Johnson | 35.0 | 20.1 | 11.6 | 6.2 | 1.2 | 0.7 | 0.2 |
| ATL@ORL | Paolo Banchero | 35.0 | 20.7 | 8.8 | 4.4 | 2.4 | 0.7 | 0.2 |
| CHA@BKN | Brandon Miller | 35.0 | 23.0 | 6.5 | 3.5 | 3.2 | 1.0 | 0.2 |
| CHA@BKN | Michael Porter Jr. | 34.0 | 23.0 | 7.2 | 2.8 | 3.5 | 0.9 | 0.2 |
| CHI@TOR | Josh Giddey | 34.0 | 15.8 | 9.0 | 7.5 | 2.5 | 0.9 | 0.2 |
| CHI@TOR | Kawhi Leonard | 34.0 | 27.1 | 7.3 | 3.3 | 3.8 | 0.9 | 0.2 |
| MIN@MIA | LaMelo Ball | 34.0 | 21.1 | 6.7 | 7.8 | 3.0 | 1.1 | 0.2 |
| MIN@MIA | Anthony Edwards | 36.0 | 25.7 | 5.6 | 3.4 | 3.6 | 0.9 | 0.2 |
| MIN@MIA | Giannis Antetokounmpo | 33.0 | 30.3 | 12.6 | 6.2 | 1.5 | 1.0 | 0.6 |
| IND@NOP | Tyrese Haliburton | 34.0 | 17.6 | 3.9 | 7.5 | 2.7 | 0.9 | 0.2 |
| IND@NOP | Pascal Siakam | 34.0 | 23.6 | 7.5 | 3.1 | 2.6 | 0.8 | 0.2 |
| IND@NOP | Trey Murphy III | 35.0 | 20.9 | 6.2 | 3.8 | 3.4 | 0.9 | 0.2 |
| IND@NOP | Zion Williamson | 32.0 | 22.1 | 6.8 | 3.5 | 0.9 | 0.8 | 0.2 |
| UTA@MEM | Keyonte George | 34.0 | 21.2 | 4.5 | 7.3 | 3.2 | 0.9 | 0.2 |
| UTA@MEM | Lauri Markkanen | 34.0 | 24.0 | 8.0 | 2.4 | 2.6 | 0.7 | 0.2 |
| UTA@MEM | Zach Edey | 31.0 | 14.3 | 13.0 | 1.3 | 0.5 | 0.8 | 0.6 |
| DAL@HOU | Kyrie Irving | 33.0 | 19.7 | 4.5 | 4.2 | 3.1 | 0.8 | 0.2 |
| DAL@HOU | Cooper Flagg | 35.0 | 19.6 | 7.1 | 4.8 | 2.2 | 0.8 | 0.2 |
| DAL@HOU | Kevin Durant | 35.0 | 26.2 | 6.4 | 4.0 | 3.0 | 0.8 | 0.2 |
| DAL@HOU | Alperen Sengun | 34.0 | 19.4 | 11.0 | 5.5 | 0.6 | 0.8 | 0.5 |
| PHX@POR | Devin Booker | 35.0 | 23.9 | 5.2 | 5.6 | 3.4 | 1.0 | 0.2 |
| PHX@POR | Deni Avdija† | 34.0 | 21.7 | 7.7 | 4.6 | 2.2 | 0.7 | 0.2 |
| GSW@LAL | Stephen Curry | 34.0 | 30.7 | 4.6 | 4.1 | 5.6 | 1.0 | 0.2 |
| GSW@LAL | Luka Doncic | 36.0 | 30.5 | 8.3 | 7.7 | 4.5 | 0.9 | 0.2 |
| SAC@LAC | Domantas Sabonis | 34.0 | 15.5 | 14.4 | 4.4 | 0.6 | 0.8 | 0.6 |
| SAC@LAC | Darius Garland | 34.0 | 22.6 | 3.5 | 7.8 | 3.6 | 0.9 | 0.2 |

† Deni Avdija questionable; main forecast assumes available. All player 3PM and steals/blocks rely on partly imputed role priors; do not treat as validated props. Full 129-player distributions and threshold probabilities in accompanying JSON/CSV.

## 4. Per-matchup evidence and major risks

- **MIL@WAS:** Wizards add Trae Young and Anthony Davis; Bucks replace Giannis with Tyler Herro. Rookie AJ Dybantsa OUT; major roster-transfer coefficient.
- **ATL@ORL:** Both defenses nearly equivalent historically; Orlando short-handed without Anthony Black and Jonathan Isaac, so model is effectively a toss-up.
- **CHA@BKN:** Charlotte held 2025–26 stronger team offensive base, but LaMelo Ball is now MIN and Knueppel/Coby White OUT; Nets acquired Randle and MPJ.
- **CHI@TOR:** 2025–26 Toronto was clearly stronger defensively; addition of Kawhi vs Chicago Powell acquisition and missing Claxton amplifies uncertainty.
- **MIN@MIA:** Giannis now in Miami raises projected interior volume and efficiency; Minnesota has Anthony Edwards and LaMelo, but DiVincenzo OUT.
- **IND@NOP:** Haliburton 2025–26 sample absent; used older season. Pacers Nesmith and McConnell OUT, Pelicans projected core intact.
- **UTA@MEM:** Utah acquired Jaren Jackson Jr; Memphis now has rookie Cam Boozer and Edey return. Unvalidated rookie/roster priors.
- **DAL@HOU:** Houston retains Durant/Amen/Sengun and VanVleet returns; Dallas Kyrie return with Lively OUT. Adams availability unresolved for HOU.
- **PHX@POR:** Portland adds Morant/Lillard and is without Sharpe; Deni Avdija QUESTIONABLE. This is one of the lowest-confidence matches.
- **GSW@LAL:** GSW missing Butler, Porzingis, Moody and Podziemski; Curry PROBABLE; Lakers Luka and Reaves with acquired Kessler.
- **SAC@LAC:** LAC missing Ingram and others despite historic 2025–26 ratings; Kings starting rookie guard; Monk QUESTIONABLE.

## 5. Conditional nonweighted availability scenarios

- **PHX@POR, Deni Avdija zero minutes:** conditional home win probability 44.3%, total 222.2, under hypothetical extra team OffRtg -4.5, DefRtg +1.0. Not observed WOWY, no assumed probability of this occurring.
- **SAC@LAC, Malik Monk zero minutes:** conditional home win probability 62.0%, total 223.7, under hypothetical extra team OffRtg -1.5, DefRtg +0.5. Not observed WOWY, no assumed probability of this occurring.

## 6. Statistical integrity and data coverage

**Factual:** Full 2025–26 team offensive/defensive ratings, pace, effective FG%, aggregate rebounds and turnovers for all 22 teams; historical player PTS/REB/AST/minutes for known veterans where source verified; current (unconfirmed) projected active starting groups; 2026-10-21 4:45 PM ET official injury designations. **Imputed:** team OREB%, free-throw rate, 3PA share, opponent shot-zone defense, detailed player FGA/3PA/FTA, most player steals, blocks, PF, some prior PPG/REB/AST, and rookie outputs. Roster rating deltas are manually specified hypotheses, not trained lineup WOWY adjustments. No confirmed five-man lineup possession data, tracking-derived touches, potential assists, rebound chances or scheme labels. Partial regression tests do not confer validity.

With regulation outcomes, player minutes sum exactly to 240/team per simulation and named+other player points sum exactly to team regulation points; future player overtime production is NOT simulated. Shared pace and game scoring; simplified assist/steal/rebound allocations; bench grouped as an explicit residual. This is a broad shadow experiment, not a production/full-fidelity model. No legal clearance for commercial use of third-party sports data is implied.

## 7. Independent gate and later evaluation

All 11 are WATCH-RESEARCH. No market price was compared; no-vig, fee-adjusted EV, buy threshold, closing line and CLV **N/A**. After outcomes, compute exact model probability vs result, Brier/log-loss, team total and margin errors and player-stat predictive errors. Do not alter this frozen forecast; later factual revisions must have another timestamp/hash. The prior 2026-10-20 v0.1 and v0.2 artifacts remain unchanged.

### Data sources
- team_stats_2025_26: https://hoopsnightly.com/stats?sort=off
- league_2025_26_averages: https://www.basketball-reference.com/leagues/NBA_stats_per_poss.html
- nba_injury_2026_10_21_1645_ET: https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-21_04_45PM.pdf
- lineup_projection: https://www.rotowire.com/basketball/nba-lineups.php
- player_profiles: https://hoopsnightly.com/players/{player_slug}
- roster_notes: rotowire and verified current roster pages
- Official NBA team schedules and statistical source snapshots gathered Oct 21 2026, during pregame research. Public-source rights should be separately verified before commercial deployment.

### Files and reproducibility
- `nba_2026-10-21_shadow_v02_model.py` — SHA256 `44288375781d285460987a2ede2ed2b17f39272b300f6d21e1c1b0a80233628c`
- `nba_2026-10-21_shadow_v02_results.json` — SHA256 `5f684c3a9557c8e8af081ab7595f482cc6a4abac6df832daa3e1e938014fae8c`
- `nba_2026-10-21_shadow_v02_games.csv` — SHA256 `1f14e653c45d6e47f22f5ad3caf1b26a67440de72cb91eb96b78398678d18f2a`
- `nba_2026-10-21_shadow_v02_players.csv` — SHA256 `8d1223a51d844753336fd87fd9849e60eb258555f80e4e70fa648a5df16012c5`
- `nba_2026-10-21_shadow_v02_sensitivity.py` — SHA256 `f5c4a8d3f505003c18e5a3796077d12ddf0253a9bcb2078b7d28b00e3c46e1c9`
- `nba_2026-10-21_shadow_v02_sensitivity.json` — SHA256 `b2113f72a85eb2d81c9a4006aa3be2cc073cd6299eebc5f326c413ef29fae16b`
- `nba_2026-10-21_shadow_v02_checksums.json` — SHA256 `f327ed16c8967866760108f1d6a89d1ee546f01b79257db6af8b8cfbe7665646`