# The Daily Line — NBA October 28, 2026 | Full-Slate Shadow Audit v0.2.5

**Research-only and uncalibrated.** 12 games; 40,000 independent simulations/game; 147 named-player rows; no game results or sportsbook odds used to build probabilities. Source injury report: official **October 28 at 7:30 PM ET / 4:30 PM PDT**. Original baseline simulation completed **2026-10-28 5:04:56 PM PDT** (2026-10-29T00:04:56Z). All eight+ prior audits and frozen records remain unchanged.

**Timing integrity:** Only SAS@UTA (6 PM PDT), OKC@DAL (6:30 PM PDT), and LAL@LAC (7:30 PM PDT) are authentically PRE-TIP forecasts in this run. Nine other games had tipped or reached scheduled tip at forecast time, and their rows are **hypothetical tipoff-style, no-live-state baseline estimates, not a frozen pregame/real-time live forecast**. In particular **DEN@NOP is not a live probability**, because no current score, clock, possession, or lineups were ingested.

**Data-quality gate:** C/partial; all 12 WATCH-research / 0 PASS / 0 AVOID. Calibration and commercial data rights unverified; no approved bet. Source roster substitutions and rate effects are unfitted analyst assumptions; 2025–26 historical team rates do not perfectly represent 2026–27 rosters.

## I. Independent baseline (no market data)

| Matchup | Tip PDT | Baseline timing | Favorite | P(win) | Fair American (model) | Simulated away–home score | Full-game total | Total 10–90% range |
|---|---:|---|---|---:|---:|---|---:|---|
| MIA@ATL | 4:00 | AFTER TIP / NOT LIVE | **MIA** | 52.8% | -112 | 119.2–117.9 | 237.0 | 210–265 |
| WAS@CLE | 4:00 | AFTER TIP / NOT LIVE | **CLE** | 73.4% | -276 | 114.1–126.4 | 240.5 | 213–268 |
| CHA@DET | 4:00 | AFTER TIP / NOT LIVE | **DET** | 57.8% | -137 | 109.2–113.1 | 222.2 | 195–250 |
| PHI@IND | 4:00 | AFTER TIP / NOT LIVE | **PHI** | 72.6% | -265 | 119.4–107.9 | 227.3 | 200–255 |
| ORL@TOR | 4:30 | AFTER TIP / NOT LIVE | **TOR** | 64.3% | -180 | 107.4–114.3 | 221.6 | 195–249 |
| NYK@CHI | 5:00 | AFTER TIP / NOT LIVE | **NYK** | 64.0% | -178 | 119.3–112.2 | 231.5 | 204–259 |
| HOU@MIL | 5:00 | AFTER TIP / NOT LIVE | **HOU** | 63.2% | -171 | 113.1–106.8 | 219.9 | 193–247 |
| GSW@MIN | 5:00 | AFTER TIP / NOT LIVE | **MIN** | 51.6% | -107 | 112.4–113.2 | 225.6 | 198–254 |
| DEN@NOP | 5:00 | AFTER TIP / NOT LIVE | **DEN** | 63.3% | -173 | 123.5–117.0 | 240.5 | 214–268 |
| SAS@UTA | 6:00 | PRE-TIP | **SAS** | 78.6% | -367 | 124.8–109.4 | 234.2 | 207–262 |
| OKC@DAL | 6:30 | PRE-TIP | **OKC** | 58.6% | -142 | 114.6–110.3 | 225.0 | 198–252 |
| LAL@LAC | 7:30 | PRE-TIP | **LAC** | 56.2% | -128 | 108.9–111.9 | 220.8 | 194–248 |

All model fair odds are calculated from independent P(win), **not purchasable sportsbook prices**. Full-game results include heuristic overtime. Player props below reflect regulation only. Narrow 0.5–2 point differences are essentially coin flips. Published market price checks occurred only **after** the original simulation was saved.

## II. Each game — factual matchup and availability review

- **MIA@ATL:** Giannis/Bam availability boosts Miami on old team priors; Atlanta has Johnson/Okongwu and guard efficiency. Miami 0–4 entering; nearly coin-flip, roster coefficients unfitted.
- **WAS@CLE:** Mitchell/Harden/Mobley/Allen core and prior defensive edge over Washington. Trae/AD and rookie Dybantsa available; rookie minutes highly uncertain.
- **CHA@DET:** Detroit Duren/Isaiah Joe OUT; Charlotte Knueppel/White/Grant Williams OUT. Detroit on back-to-back, making the 58% baseline especially fragile.
- **PHI@IND:** Philadelphia Maxey/Brown/Embiid/LeBron projected available; Indiana Haliburton/Zubac/McConnell OUT, Nembhard/Nesmith available. Philadelphia is the large model favorite, but minutes and early-season priors are uncertain.
- **ORL@TOR:** Orlando Paolo Banchero, Suggs, Isaac OUT; Toronto Kawhi out. Raptors favored despite losing star from its current lineup.
- **NYK@CHI:** Knicks won Tuesday and are on B2B. Chicago Claxton/Patrick Williams OUT; Brunson/Towns projected available. New York moderate favorite.
- **HOU@MIL:** Houston Şengün, Smart, Adams OUT. Durant and Amen projected available; Milwaukee Herro/Turner core. Without Şengün the Rockets edge is less secure.
- **GSW@MIN:** Minnesota Edwards and DiVincenzo OUT, Golden State Butler/Moody/Porziņģis OUT; Curry and Lendeborg available. The baseline is effectively 50/50.
- **DEN@NOP:** Denver Nikola Jokić/Murray versus Zion/Murphy; Denver Cam Johnson/Strawther OUT and New Orleans Missi OUT; Poole available. Denver won 141–135 in OT four days earlier. Game had started before model run: NOT a live win probability.
- **SAS@UTA:** Spurs Wembanyama/Fox/Castle core; Utah Jaren Jackson Jr. and Nurkić OUT, Markkanen questionable and assumed 28 minutes. Biggest baseline favorite, but Q is material.
- **OKC@DAL:** OKC Holmgren, Jalen Williams, Caruso, Wallace OUT; Shai usage raised. Dallas Flagg active, Kyrie questionable assumed 25 min; remaining margin narrow.
- **LAL@LAC:** Lakers Luka Dončić OUT, Reaves primary, on back-to-back. Clippers Ingram/Beal/Rui OUT and Garland-led. Model favors Clippers narrowly; published market snapshots favored Lakers, a major model-vs-price disagreement requiring independent validation.

## III. Player distributions and threshold examples (regulation only)

| Game | Player | Projected minutes | PTS | REB | AST | P(25+ pts) | P(10+ reb) | P(8+ ast) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| MIA@ATL | Giannis Antetokounmpo | 34.0 | 30.6 | 12.7 | 6.4 | 77.2% | 81.5% | 31.5% |
| WAS@CLE | Trae Young | 33.0 | 20.8 | 2.4 | 7.7 | 28.7% | 0.0% | 50.0% |
| WAS@CLE | Anthony Davis | 32.0 | 18.2 | 10.3 | 2.1 | 14.8% | 57.6% | 0.1% |
| WAS@CLE | Donovan Mitchell | 35.0 | 27.5 | 5.1 | 5.8 | 62.5% | 3.9% | 23.4% |
| CHA@DET | Cade Cunningham | 36.0 | 27.0 | 6.5 | 9.6 | 61.1% | 12.1% | 75.2% |
| PHI@IND | Tyrese Maxey | 31.6 | 20.6 | 3.9 | 5.0 | 27.4% | 0.7% | 13.5% |
| PHI@IND | Jaylen Brown | 30.8 | 22.3 | 7.0 | 4.2 | 35.5% | 17.2% | 6.2% |
| PHI@IND | Joel Embiid | 25.5 | 18.4 | 7.0 | 2.9 | 15.8% | 17.6% | 0.9% |
| NYK@CHI | Jalen Brunson | 35.0 | 25.7 | 3.4 | 6.5 | 53.7% | 0.3% | 32.2% |
| HOU@MIL | Kevin Durant | 36.0 | 26.6 | 7.0 | 3.9 | 59.2% | 17.2% | 4.5% |
| GSW@MIN | Stephen Curry | 32.1 | 27.1 | 4.8 | 4.5 | 60.5% | 2.5% | 9.2% |
| GSW@MIN | LaMelo Ball | 35.0 | 24.2 | 6.8 | 7.4 | 46.2% | 15.8% | 45.8% |
| DEN@NOP | Nikola Jokic | 35.0 | 25.9 | 12.7 | 9.2 | 55.2% | 80.8% | 70.0% |
| DEN@NOP | Jamal Murray | 35.9 | 25.4 | 4.4 | 6.2 | 52.7% | 1.5% | 28.1% |
| DEN@NOP | Zion Williamson | 30.6 | 21.9 | 6.4 | 3.0 | 32.9% | 11.7% | 1.1% |
| SAS@UTA | Victor Wembanyama | 33.0 | 26.7 | 14.4 | 3.0 | 59.8% | 90.4% | 1.3% |
| SAS@UTA | Lauri Markkanen | 28.0 | 19.5 | 6.1 | 1.8 | 21.7% | 9.6% | 0.1% |
| OKC@DAL | Shai Gilgeous-Alexander | 36.0 | 33.2 | 5.1 | 5.8 | 84.8% | 3.8% | 23.6% |
| OKC@DAL | Kyrie Irving | 25.0 | 15.6 | 3.5 | 3.2 | 8.2% | 0.4% | 1.8% |
| OKC@DAL | Cooper Flagg | 36.0 | 19.9 | 7.6 | 4.9 | 23.6% | 24.2% | 12.2% |
| LAL@LAC | Austin Reaves | 37.0 | 26.1 | 5.6 | 5.5 | 56.0% | 6.1% | 19.4% |
| LAL@LAC | Darius Garland | 37.0 | 24.3 | 3.7 | 6.6 | 46.7% | 0.5% | 34.1% |

All probabilities above are experimental distribution outputs. They are not market prices, do not incorporate overtime and are uncalibrated. A questionable player is modeled under one **assumed** playing-time baseline, not confirmed active. Fantasy points in CSV use the explicitly documented custom independent scoring formula from prior versions.

## IV. Sensitivity and unresolved injury alternatives

For each game, I approximated the effect of adding 4 points/100 possessions to one team’s offensive rating and subtracting 4 from the opponent (and vice versa), using its simulated margin variance. Ranges are *heuristic scenario tests*, **not calibrated confidence intervals**.

| Matchup | Base home-win P | Home-win stress range |
|---|---:|---:|
| MIA@ATL | 47.2% | 31.4–63.8% |
| WAS@CLE | 73.4% | 58.7–85.2% |
| CHA@DET | 57.8% | 42.0–72.6% |
| PHI@IND | 27.4% | 15.3–42.6% |
| ORL@TOR | 64.3% | 47.8–78.6% |
| NYK@CHI | 36.0% | 22.1–51.7% |
| HOU@MIL | 36.8% | 23.0–52.8% |
| GSW@MIN | 51.6% | 35.8–67.5% |
| DEN@NOP | 36.7% | 22.5–53.0% |
| SAS@UTA | 21.4% | 11.0–35.1% |
| OKC@DAL | 41.4% | 26.0–57.8% |
| LAL@LAC | 56.2% | 39.9–71.7% |

Separately (not blended into original forecasts), we tested qualitative hypothetical team-impact assumptions: Lauri OUT (−4.0 Utah OffRtg, +0.5 DefRtg) raises SAS model P(win) from 78.6% to roughly 83.5%; Kyrie OUT (−3.0 Dallas OffRtg, +0.2 DefRtg) raises OKC from 58.6% to roughly 63.8%; Ajay Mitchell OUT (−1.5 OKC OffRtg, +0.6 DefRtg) lowers OKC to roughly 55.9%. These effects are **invented stress magnitudes**, not observed player WOWY or official status probabilities, and therefore are NOT bet-grade inputs.

## V. Market-comparison phase AFTER independent freeze (indicative, not executable)

The following publicly listed paired moneylines were checked only after the independent run. The publication pages do not prove a matching current executable bid/ask, proper jurisdiction, fee and liquidity, or that the quotes reflect every newly ruled-out player. Consequently market differences below are **research comparisons only**, not tradeable edges/EV/PASS.

| Late game | Source-indicative market ML (away / home) | Market no-vig P(away) | Our P(away) | Difference (percentage points) |
|---|---:|---:|---:|---:|
| SAS@UTA | -650 / +470 | 83.2% | 78.6% | -4.6 |
| OKC@DAL | -205 / +170 | 64.5% | 58.6% | -5.9 |
| LAL@LAC | -190 / +158 | 62.8% | 43.8% | -19.0 |

**Model-market disagreement to investigate:** LAL@LAC has Luka Dončić officially OUT while indicative published sportsbook snapshots still favored the Lakers. That may reflect stale/unmatched quotes and errors in our unfitted injury adjustment. It **does not** establish a playable Clippers edge. Kalshi-specific bid/ask and fees were not verified, so no Kalshi EV or threshold is claimed.

- **SAS@UTA indicative quote provenance:** https://dknetwork.draftkings.com/2026/10/28/san-antonio-spurs-at-utah-jazz-prediction-pick-for-wednesday-10-28-26/
- **OKC@DAL indicative quote provenance:** https://sportsedgemodel.com/game/1905-oklahoma-city-thunder-dallas-mavericks
- **LAL@LAC indicative quote provenance:** https://gridironandwine.com/predictions/nba/2026-10-28-los-angeles-lakers-vs-los-angeles-clippers.html

## VI. Structural checks and restrictions

- 12 simulated matchups and 147 named player projection rows. Independent win probabilities sum to 1 for every game; max regulation team-minutes accounting error 1.137e-13; maximum player/team regulation points discrepancy 0.000e+00.
- **Not implemented/verified:** fully historical calibrated team/prop distributions, accurate ongoing live state, full 2026 player tracking, lineup WOWY/casual player impacts, team/opponent shot-zone matchups for every club, overtime on player props, verified exact starter/stint durations, source commercial licensing, or approved bet sizing.
- **Not observed:** contemporaneous executable sportsbook or Kalshi contract quotes with jurisdiction, spreads and fees; therefore net EV, buy threshold, CLV, actual bet or qualified PASS are N/A.
- Structural consistency and 40,000 Monte Carlo samples do not prove prediction accuracy. The earliest 9 games cannot be archived as legitimate original pregame predictions because the calculations happened after tip.

## VII. Source/provenance and archive integrity

- NBA official schedule: https://www.nba.com/games?date=2026-10-28
- NBA official injury report 7:30 PM ET: https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-28_07_30PM.pdf
- Historical 2025–26 team advanced data: https://basketball.realgm.com/nba/team-stats/2026/Advanced_Stats/Team_Totals/Regular_Season
- Denver official Oct 28 preview, previous 141–135 OT result: https://www.nba.com/nuggets/news/nuggets-play-pelicans-road
- Previously accepted Daily-NBA experiments: https://github.com/OneVillage83/Daily-NBA
- **Original snapshot SHA-256:** `8535da586aa0898f08ec5692aace04caf444de462475ad310cdfd85250c4e7b4`
- **Original source SHA-256:** `6922176e8f3dfe02a62ca18bfc231edec5c1d9ecc2bcf760f9667499b4c23b94`
- **Original snapshot UTC freeze time:** `2026-10-29T00:04:56+00:00`. Additional sensitivity and market context are separate files created after this snapshot.

## Final gate

**WATCH / research only for all 12. Zero PASS.** Before action, require correctly timestamped actual live score/possession or verified pretip availability, improved calibrations and exact comparable executable odds including fees. Preserve every original prediction as append-only; postgame outcomes are to be graded in a separate audit.
