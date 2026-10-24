# October 24, 2026 — Full NBA independent SHADOW audit v0.2.3

**Status:** FROZEN before first NBA tip; uncalibrated research only. **Gate:** 0 PASS / 8 WATCH. No actual market odds, fee/EV/CLV calculation, consensus forecast or third-party predictive inputs.

- **Original forecast freeze:** 2026-10-24T20:15:42Z (1:15:42 PM Pacific), first game 2026-10-24T22:00:00Z (3 PM Pacific).
- **Factual source cutoff:** 2026-10-24T20:11:00Z. NBA injury bulletin at 2026-10-24 3:30 PM Eastern / 12:30 PM Pacific.
- **Engine:** `tdl-nba-2026-10-24-v0.2.3-shadow-uncalibrated`; seed `20261024023`, 60,000 independent event simulation draws/game, 8 games and 99 individually projected players.
- **Original frozen JSON SHA-256:** `7b0882b1275e260f88d7a959fcafae4f8d44aee8a718f3b51d5d924285acc77b`. Raw research JSON, CSV exports and Python source are retained in the dated companion research bundle.

## Frozen premarket game predictions

All probabilities and American prices below are derived from the **independent model** and not real market quotes. Team scores include heuristic OT, player forecasts are regulation only.

| Away @ Home | Tipoff PDT | Winner | P(win) | Expected Away–Home | Expected total | Expected home margin | Total 10–90% model draw interval | Winner fair odds |
|---|---|---|---:|---:|---:|---:|---:|---:|
| MIA@CHA | 3:00 PM | Miami | **57.97%** | 117.99–114.11 | 232.10 | -3.88 | 205–260 | -138 |
| BKN@CLE | 4:30 PM | Cleveland | **74.80%** | 108.65–121.73 | 230.38 | +13.09 | 203–258 | -297 |
| MIL@PHI | 4:30 PM | Philadelphia | **72.58%** | 107.01–118.60 | 225.62 | +11.59 | 199–253 | -265 |
| WAS@CHI | 5:00 PM | Washington | **50.36%** | 120.68–120.57 | 241.25 | -0.11 | 214–269 | -101 |
| SAS@DAL | 5:00 PM | San Antonio | **72.29%** | 119.70–108.40 | 228.11 | -11.30 | 201–255 | -261 |
| HOU@ATL | 5:30 PM | Houston | **51.06%** | 113.04–112.53 | 225.57 | -0.52 | 199–253 | -104 |
| NOP@DEN | 6:00 PM | Denver | **71.49%** | 114.21–125.13 | 239.35 | +10.92 | 212–267 | -251 |
| GSW@PHX | 7:00 PM | Phoenix | **71.37%** | 104.58–115.61 | 220.19 | +11.03 | 193–248 | -249 |

A small win-probability difference is **not** an exploitable edge absent a permissible documented market price, transaction costs, calibrated uncertainty and owner-approved qualification thresholds.

## Evidence and availability at freeze

Historical season baselines incorporate 2025–26 observed OffRtg, DefRtg, pace, eFG%, offensive/defensive rebound rates, turnover, assist rates, 3PA/FGA and FTA/FGA for all 16 teams. Underlying roster/role deltas, expected minutes and B2B fatigue effects are analyst priors, NOT observed this season and not estimated via causal on/off.

**Official NBA 3:30 PM ET injury report:** Charlotte Knueppel/White/Grant Williams OUT; Philadelphia LeBron James OUT, Dean Wade QUESTIONABLE; Dallas Cooper Flagg, Lively II, Aldama, Martin OUT and Kyrie Irving plus several others QUESTIONABLE; Houston Fred VanVleet/Steven Adams OUT, Marcus Smart and Reed Sheppard QUESTIONABLE; Denver Cam Johnson/Jones/Strawther OUT; New Orleans Missi OUT; Phoenix Mark Williams OUT, Ighodaro DOUBTFUL, Kennard QUESTIONABLE; Warriors team report NOT YET SUBMITTED. Separate contemporaneous reporting indicated Curry unlikely and Podziemski not playing; **GSW official status was not confirmed** by the bulletin. Never portray projected starters as confirmed.

**Strongest directional but unqualified model leans:** Cleveland, Philadelphia, San Antonio, Denver, Phoenix. **Very close:** Washington–Chicago and Houston–Atlanta.

## Selected independent player means (regulation)

| Player | PTS | REB | AST | 
|---|---:|---:|---:|
| Giannis Antetokounmpo | 30.34 | 12.53 | 6.42 |
| Brandon Miller | 23.43 | 6.58 | 3.61 |
| Donovan Mitchell | 26.50 | 5.02 | 5.64 |
| Evan Mobley | 16.56 | 10.21 | 3.64 |
| Jaylen Brown | 25.10 | 8.02 | 4.83 |
| Tyrese Maxey | 22.99 | 4.43 | 5.80 |
| Trae Young | 22.81 | 2.54 | 8.24 |
| Josh Giddey | 17.79 | 9.15 | 9.17 |
| Victor Wembanyama | 26.48 | 14.53 | 2.95 |
| Kyrie Irving (questionable baseline 27min) | 16.87 | 3.80 | 3.53 |
| Kevin Durant | 24.98 | 6.24 | 3.73 |
| Jalen Johnson | 19.60 | 11.25 | 6.74 |
| Nikola Jokic | 26.23 | 12.89 | 9.38 |
| Jamal Murray | 25.17 | 4.33 | 6.14 |
| Devin Booker | 24.29 | 5.41 | 5.78 |

All 99 player rows including steals/blocks/fouls/turnovers/3PM/fantasy/thresholds remain in the original companion CSV/JSON research archive.

## Sensitivity, separate from freeze

Under **unweighted ±4 points per 100 possessions of offensive-rating perturbations to each team in opposing directions**, favorite probabilities span: MIA 46–69%, CLE 64–84%, PHI 62–82%, WAS 37–63%, SAS 61–82%, HOU 39–63%, DEN 60–81%, PHX 60–80%. These are **stress-test scenarios, NOT calibrated intervals**.

- With Kyrie Irving OUT rather than the 27-minute questionable-playing baseline, Dallas P(win) falls from **27.71%** to **23.27%** in the model.
- With Curry playing 30 minutes (hypothetical conditional scenario), Phoenix P(win) falls from **71.37%** to **63.34%**.
- Rockets Sheppard and Smart out scenario: Hawks P(win) increases from **48.94%** to **52.33%**, but the implementation changed team ratings, **not both player allocations**.

**Scenario errata / do not silently alter original snapshot:** The fifth frozen scenario was labeled “Curry ACTIVE + Podziemski ACTIVE” but the implementation **only reinserted Curry**, adding an assumed +6.2 team offensive-rating adjustment. The extra Podziemski minutes were **not simulated**. Treat that scenario solely as Curry reinstated + extra assumed team-rating uplift, not a verified two-player lineup. This errata is interpretive and keeps the original frozen JSON unchanged.

## Validated structure and outstanding model limitations

**Passed functional checks:** eight matchups complete; `P(home)+P(away)=1`; exactly 240 minutes allocated per team in regulation; simulation player points reconcile to team regulation points; original random seed/feature assumptions archived; no market inputs.

**Not demonstrated:** historically calibrated win or player threshold probabilities; true five-player on/off stints, observed potential assists/touches/rebound chances, comprehensive player-specific shot zones/defensive scheme, reliable 2026–27 roster-change estimates, properly settled overtime player-prop distributions, full legal/commercial data-source permission. Therefore **all games remain WATCH-research, no PASS**, and market probability/no-vig/fee-adjusted EV/CLV are **N/A**.

## Data provenance (factual sources, not third-party forecasts)

- [Official NBA Saturday schedule](https://www.nba.com/games?date=2026-10-24)
- [Official 3:30 PM ET NBA injury bulletin](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-24_03_30PM.pdf)
- [2025–26 advanced team baselines](https://basketball.realgm.com/nba/team-stats/2026/Advanced_Stats/Team_Totals/Regular_Season)
- [2025–26 team shooting/rebounds/turnovers](https://basketball.realgm.com/nba/team-stats/2026/Totals/Team_Totals/Regular_Season)
- [Contemporaneous Warriors injury report](https://www.nbcsportsbayarea.com/nba/golden-state-warriors/steph-curry-brandin-podziemski-not-expected-to-play-suns/1973812/)

**Freeze policy:** Every subsequent availability correction, market price snapshot, or postgame review must be a new separately timestamped record; do not overwrite original probabilities or assert no-vig/CLV without an authentic contemporaneous contract quote.
