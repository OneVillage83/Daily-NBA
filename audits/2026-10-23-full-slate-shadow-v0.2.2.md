# The Daily Line — NBA Full-Slate Independent Shadow Audit

**Friday, October 23, 2026 · Experimental v0.2.2 · SHADOW / WATCH ONLY**

## Audit integrity and as-of conditions

- First CHI@MIL forecast generated **2026-10-23 12:59:04 PM PDT**, before first scheduled tip (1:00 PM PDT). Original model version is v0.2.1 research; **never retroactively overwritten**.
- Eleven later game v0.2.2 forecasts generated/frozen as one run at **2026-10-23 1:08:19 PM PDT**, ahead of their scheduled 4:00 PM PDT or later start times.
- Latest official NBA injury input: 3:45 PM ET / 12:45 PM PDT report, October 23. Projected lineup sources last observed around 3:57 PM ET; all marked PROJECTION, not confirmed.
- All projections are *independent of sportsbook odds, other models, consensus picks or fantasy predictions*. No live play-by-play is used.
- Core: 60,000 simulations/game for game and player outcome distributions; team pace, opponent-adjusted OffRtg/DefRtg, four factors, assumed roster deltas, joint player event allocations, OT tie correction for full-game market scopes.
- Original-snapshot SHA-256: `65c693b985c342d632650ad0a06e3fd80efd399a111967061b9d01a4a1172ae4`; v0.2.2 full JSON SHA-256 documented in checksums.
- **Not a calibrated/published production forecast. Every matchup WATCH, not PASS. No verified odds, two-way market prices, transaction fees, EV or CLV: N/A.**

## Slate model output: scores, probabilities, fair prices, spreads and totals

Fair prices derive solely from our own independent probabilities, **not quotations or betting recommendations**. Positive home margin means home favored.

| Matchup | Favorite | P(favorite) | Fair ML | Expected away–home | Fair home margin | Total | Total 10–90% draw interval |
|---|---|---:|---:|---|---:|---:|---|
| CHI @ MIL | CHI | 53.9% | -117 | 115.9–114.1 | -1.9 | 230.0 | 203–257 |
| DAL @ IND | IND | 52.3% | -110 | 115.8–117.0 | +1.2 | 232.8 | 206–260 |
| MIN @ ORL | MIN | 51.2% | -105 | 115.5–115.0 | -0.5 | 230.5 | 203–258 |
| TOR @ WAS | TOR | 64.4% | -181 | 120.9–113.9 | -7.0 | 234.8 | 208–262 |
| NYK @ BOS | BOS | 52.4% | -110 | 111.4–112.5 | +1.1 | 224.0 | 197–251 |
| ATL @ CHA | CHA | 52.4% | -110 | 112.8–114.1 | +1.3 | 226.9 | 200–255 |
| DET @ MIA | MIA | 52.2% | -109 | 116.8–117.9 | +1.1 | 234.7 | 208–262 |
| NOP @ UTA | UTA | 50.8% | -103 | 120.4–120.9 | +0.5 | 241.3 | 214–269 |
| HOU @ SAS | SAS | 57.0% | -132 | 111.8–115.2 | +3.4 | 227.1 | 200–254 |
| POR @ SAC | POR | 63.8% | -176 | 119.3–112.4 | -6.8 | 231.7 | 205–259 |
| MEM @ GSW | GSW | 57.2% | -134 | 112.4–115.9 | +3.5 | 228.4 | 201–257 |
| LAC @ LAL | LAL | 65.3% | -188 | 108.8–116.1 | +7.3 | 224.8 | 198–252 |

## 2025–26 historical advanced-statistical inputs

All team inputs below are *last season*, not 2026–27 season rates. Pace = possessions per 48, offensive and defensive ratings = points per 100 possessions. 3PAr = 3PA/FGA; FTr = FTA/FGA. The percentages, pace and ratings are actual observed 2025–26 regular-season data; roster deltas are separately assumed.

| Team | OffRtg | DefRtg | Pace | eFG% | TOV% | OREB% | DRB% | 3PAr | FTr | AST% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| CHI | 113.0 | 118.1 | 102.5 | 54.7% | 13.3% | 23.1% | 75.5% | 44.3% | 24.6% | 67.2% |
| MIL | 112.9 | 119.3 | 97.6 | 56.5% | 13.9% | 21.1% | 74.2% | 45.7% | 22.3% | 63.3% |
| DAL | 111.2 | 116.5 | 101.7 | 52.7% | 12.6% | 23.2% | 74.1% | 35.5% | 28.7% | 60.4% |
| IND | 110.9 | 118.8 | 101.0 | 53.3% | 12.8% | 21.7% | 74.1% | 42.2% | 25.2% | 67.8% |
| MIN | 116.8 | 113.5 | 100.5 | 55.9% | 12.9% | 25.7% | 73.8% | 42.0% | 28.5% | 61.2% |
| ORL | 114.9 | 114.3 | 100.0 | 53.1% | 12.4% | 25.0% | 75.7% | 38.6% | 31.1% | 64.7% |
| TOR | 115.9 | 113.0 | 98.4 | 54.6% | 12.2% | 25.5% | 74.0% | 36.3% | 26.5% | 69.2% |
| WAS | 111.0 | 122.7 | 101.4 | 53.5% | 13.6% | 24.1% | 70.2% | 40.3% | 23.5% | 59.9% |
| NYK | 119.9 | 113.3 | 96.8 | 55.7% | 12.1% | 29.4% | 76.8% | 42.8% | 23.8% | 64.3% |
| BOS | 120.8 | 112.7 | 94.8 | 55.3% | 11.2% | 29.2% | 75.8% | 46.7% | 20.7% | 58.5% |
| ATL | 116.1 | 113.7 | 101.6 | 55.4% | 12.3% | 24.4% | 74.5% | 42.9% | 23.4% | 69.1% |
| CHA | 119.4 | 114.4 | 96.8 | 55.2% | 13.5% | 30.5% | 76.7% | 48.7% | 24.4% | 64.3% |
| DET | 117.9 | 109.7 | 99.2 | 54.6% | 13.0% | 30.9% | 74.3% | 34.5% | 29.2% | 64.1% |
| MIA | 116.7 | 114.5 | 103.4 | 54.2% | 11.6% | 25.4% | 74.9% | 40.6% | 26.8% | 66.3% |
| NOP | 114.4 | 118.9 | 100.3 | 52.7% | 12.2% | 27.0% | 71.4% | 35.5% | 28.4% | 59.6% |
| UTA | 114.1 | 122.3 | 102.3 | 53.6% | 13.2% | 26.2% | 72.9% | 40.2% | 27.7% | 69.6% |
| HOU | 118.6 | 113.2 | 96.1 | 54.2% | 13.3% | 34.9% | 74.6% | 35.0% | 26.0% | 59.1% |
| SAS | 119.6 | 111.3 | 99.9 | 55.9% | 11.8% | 26.2% | 77.4% | 42.2% | 27.4% | 64.6% |
| POR | 114.4 | 114.7 | 100.5 | 53.4% | 14.6% | 31.3% | 72.7% | 46.9% | 28.0% | 61.6% |
| SAC | 111.4 | 121.5 | 99.2 | 52.5% | 12.6% | 26.0% | 73.5% | 33.9% | 25.6% | 61.5% |
| MEM | 112.9 | 118.8 | 101.3 | 53.3% | 13.0% | 24.7% | 70.9% | 43.6% | 25.1% | 67.3% |
| GSW | 115.0 | 115.6 | 99.0 | 54.9% | 13.8% | 25.8% | 73.0% | 49.7% | 23.8% | 70.6% |
| LAC | 117.3 | 116.1 | 96.5 | 55.9% | 13.2% | 23.7% | 72.9% | 40.4% | 29.5% | 58.6% |
| LAL | 118.2 | 116.4 | 98.3 | 57.3% | 13.2% | 23.9% | 74.3% | 39.4% | 32.0% | 61.5% |

**Known limitations:** team-to-team opponent shot-quality/defensive scheme factors are not fully measured; only some prior player shooting zones are verified and other players use imputed profiles. Actual opponent effective FG% and forced turnover percentages are league-proxy where a team-specific historical series was unavailable. New roster impact delta assumptions are *not* fitted coefficients.

## Key historical factors and matchup interpretation

- **Chicago @ Milwaukee:** MIL shot 38.7% on threes last season (3,205 attempts) compared with Chicago’s 35.6%. However Milwaukee had a worse historical defense (119.3 DefRtg), Chicago had higher pace (102.5 versus 97.6). Giddey available; Claxton OUT. Original pregame CHI 53.9% maintained. No late refresh after tip.
- **Dallas @ Indiana:** Both last-season defensive ratings were poor (116.5 vs 118.8); Indiana’s Haliburton/Zubac/Siakam group is improving from personnel changes but not calibrated, and Mavericks Kyrie played only about 24 minutes in opener following injury. DAL Lively/Aldama OUT; Indiana McConnell OUT and Nesmith/Sheppard QUESTIONABLE.
- **Minnesota @ Orlando:** Minnesota 116.8 OffRtg/113.5 DefRtg versus Orlando 114.9/114.3, with both using high-efficiency scorers. Orlando Black and Isaac OUT; Minnesota DiVincenzo OUT. Very close result and modest model edge to MIN.
- **Toronto @ Washington:** TOR historical 115.9 OffRtg, 113.0 DefRtg versus WAS 111.0 and 122.7; roster shifts include Kawhi for TOR, Trae/Anthony Davis for WAS, with Dybantsa OUT. The model still favors TOR but is unusually sensitive to speculative roster coefficients.
- **New York @ Boston:** Highest historical scoring efficiencies in this game: BOS 120.8 OffRtg and NYK 119.9; both pace comparatively slow (94.8 and 96.8). Tatum/George versus Brunson/Towns with no missing main starters on official report; NYK Towns opening-game foul trouble caused minutes drop to 23 and adds uncertainty.
- **Atlanta @ Charlotte:** Charlotte had 119.4 OffRtg, 30.5 OREB%, 48.7% 3PA/FGA prior season; Atlanta played faster (101.6 pace). CHA Knueppel/White OUT; ATL Gueye and Veesaar OUT. Lean CHA is too weak for PASS.
- **Detroit @ Miami:** DET’s 109.7 defense and 30.9 offensive rebound share are structural strengths; Miami now features Giannis+Bam and faster historical pace of 103.4. DET has more historical minutes/lineup stability; Miami’s huge roster adjustment produces wider epistemic uncertainty.
- **New Orleans @ Utah:** UTA’s defense was 122.3 DefRtg and NOP 118.9, with 100+ pace each. High predicted total but a nearly 50/50 winner, and Utah Nurkić OUT. Player defensive matchup data remains limited.
- **Houston @ San Antonio:** HOU 118.6/113.2 Off/Def vs SAS 119.6/111.3. SAS Fox QUESTIONABLE, Keldon QUESTIONABLE, Tobias Harris OUT; HOU Adams and Reed Sheppard QUESTIONABLE. Use distinct conditional scenario, not invented probability weighting.
- **Portland @ Sacramento:** POR historic 31.3% offensive rebound rate and SAC 121.5 DefRtg; Portland’s new Morant/Lillard lineup against Sacramento’s weaker defensive baseline creates POR 63.8% lean. Sharpe OUT; SAC Monk AVAILABLE. 41-point Portland opener win is not reweighted as predictive consensus.
- **Memphis @ Golden State:** Both last-season defenses struggled; Warriors Curry is healthy but Butler/Moody/Porzingis OUT, and Memphis Coward is DOUBTFUL with Stewart QUESTIONABLE. Baseline assumes Coward effectively OUT; his available scenario stored separately.
- **LA Clippers @ LA Lakers:** Lakers have stronger historical offense (118.2 vs 117.3) and Clippers absent Beal/Ingram/Strus. LAL Doncic/Reaves/Kessler with LaRavia QUESTIONABLE; Lakers 65.3% lean, but injury minutes/roster assumptions not calibrated.

## Official injury and scenario register

Exact availability labels from [NBA 3:45 PM ET injury report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-23_03_45PM.pdf); only notable injury/rotation effects are listed, not every two-way assignment.

| Team | Relevant status |
|---|---|
| CHI | Nic Claxton: **OUT** |
| DAL | Dereck Lively II: **OUT**; Santi Aldama: **OUT**; Caleb Martin: **OUT** |
| IND | T.J. McConnell: **OUT**; Aaron Nesmith: **QUESTIONABLE**; Ben Sheppard: **QUESTIONABLE** |
| MIN | Donte DiVincenzo: **OUT** |
| ORL | Anthony Black: **OUT**; Jonathan Isaac: **OUT** |
| WAS | AJ Dybantsa: **OUT** |
| BOS | Devin Carter: **OUT** |
| ATL | Mouhamed Gueye: **OUT**; Henri Veesaar: **OUT** |
| CHA | Kon Knueppel: **OUT**; Coby White: **OUT**; Grant Williams: **OUT** |
| DET | Taurean Prince: **AVAILABLE** |
| UTA | Jusuf Nurkic: **OUT** |
| HOU | Steven Adams: **QUESTIONABLE**; Reed Sheppard: **QUESTIONABLE** |
| SAS | De'Aaron Fox: **QUESTIONABLE**; Keldon Johnson: **QUESTIONABLE**; Tobias Harris: **OUT** |
| POR | Shaedon Sharpe: **OUT** |
| SAC | Malik Monk: **AVAILABLE**; Ben Simmons: **OUT** |
| MEM | Cedric Coward: **DOUBTFUL**; Isaiah Stewart: **QUESTIONABLE** |
| GSW | Jimmy Butler: **OUT**; Moses Moody: **OUT**; Kristaps Porzingis: **OUT**; Brandin Podziemski: **PROBABLE** |
| LAC | Bradley Beal: **OUT**; Brandon Ingram: **OUT**; Max Strus: **OUT** |
| LAL | Jake LaRavia: **QUESTIONABLE**; Walker Kessler: **AVAILABLE** |

### Conditional materiality tests, NOT the frozen baseline

Out scenarios use explicitly *assumed* changes to team OffRtg/DefRtg, not measured WOWY impact, and are never blended using invented probabilities.

| Matchup / scenario | Baseline home win | Conditional home win | Change |
|---|---:|---:|---:|
| HOU@SAS — Fox OUT; hypothetical SAS -2.0 off, +0.3 def; no outcome-informed scenario weighting | 57.0% | 53.8% | -3.2 pp |
| LAC@LAL — LaRavia OUT; hypothetical LAL -0.6 off, +0.5 def | 65.3% | 63.4% | -1.9 pp |
| MEM@GSW — Cedric Coward plays 25 min rather than doubtful-OUT base; MEM +0.8 off, +0.1 def assumed | 57.2% | 55.9% | -1.4 pp |
| DAL@IND — Nesmith+Sheppard healthy scenario vs baseline uncertain status; IND +0.8 off, -0.4 def assumed | 52.3% | 54.2% | +1.9 pp |
| HOU@SAS — Houston Steven Adams/Sheppard both out; HOU -0.7 off,+0.4 def assumed | 57.0% | 58.6% | +1.6 pp |

### Broader offensive-regime stress test

Independent each-team ±4 points per 100 possessions in opposing directions; **this is not a statistical confidence interval**.

| Matchup | Baseline home P | Stress-test home P range |
|---|---:|---:|
| DAL@IND | 52.3% | 39.7%–64.6% |
| MIN@ORL | 48.8% | 36.7%–61.3% |
| TOR@WAS | 35.6% | 25.0%–48.1% |
| NYK@BOS | 52.4% | 40.7%–63.3% |
| ATL@CHA | 52.4% | 40.4%–64.7% |
| DET@MIA | 52.2% | 40.6%–64.4% |
| NOP@UTA | 50.8% | 38.1%–63.7% |
| HOU@SAS | 57.0% | 45.6%–68.5% |
| POR@SAC | 36.2% | 25.3%–49.0% |
| MEM@GSW | 57.2% | 44.4%–68.8% |
| LAC@LAL | 65.3% | 52.7%–75.7% |

## Player-level projection highlights (regulation-only)

**CAUTION**: player thresholds here exclude overtime, whereas many actual betting contracts include overtime; use for model research only until matching settlement simulations are validated. All mean outputs and threshold probabilities are in `nba_2026_10_23_players.csv`.

| Matchup | Player | Minutes | PTS | REB | AST | 25+ PTS | 10+ REB | 8+ AST |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| CHI@MIL | Norman Powell (CHI) | 33.0 | 22.2 | 3.7 | 2.6 | 35% | 1% | 1% |
| CHI@MIL | Matas Buzelis (CHI) | 34.0 | 18.2 | 6.7 | 2.2 | 16% | 15% | 0% |
| CHI@MIL | Tyler Herro (MIL) | 33.0 | 20.7 | 6.4 | 4.0 | 28% | 11% | 5% |
| CHI@MIL | Ryan Rollins (MIL) | 33.0 | 17.1 | 5.2 | 4.8 | 12% | 4% | 11% |
| DAL@IND | Cooper Flagg (DAL) | 34.0 | 20.8 | 7.2 | 5.0 | 28% | 19% | 14% |
| DAL@IND | Kyrie Irving (DAL) | 28.0 | 17.5 | 3.9 | 3.9 | 14% | 1% | 5% |
| DAL@IND | Pascal Siakam (IND) | 35.0 | 24.5 | 7.5 | 3.5 | 48% | 22% | 3% |
| DAL@IND | Tyrese Haliburton (IND) | 33.0 | 17.2 | 3.7 | 7.9 | 13% | 1% | 54% |
| MIN@ORL | Anthony Edwards (MIN) | 35.0 | 25.1 | 5.3 | 3.2 | 51% | 5% | 2% |
| MIN@ORL | LaMelo Ball (MIN) | 32.0 | 20.0 | 6.1 | 7.1 | 25% | 9% | 42% |
| MIN@ORL | Paolo Banchero (ORL) | 35.0 | 20.7 | 8.4 | 4.5 | 27% | 34% | 9% |
| MIN@ORL | Franz Wagner (ORL) | 33.0 | 20.1 | 6.2 | 3.4 | 25% | 10% | 2% |
| TOR@WAS | Kawhi Leonard (TOR) | 32.0 | 25.0 | 6.5 | 3.4 | 50% | 13% | 2% |
| TOR@WAS | RJ Barrett (TOR) | 31.0 | 17.8 | 5.5 | 3.5 | 15% | 5% | 3% |
| TOR@WAS | Trae Young (WAS) | 33.0 | 21.2 | 2.4 | 7.5 | 31% | 0% | 48% |
| TOR@WAS | Anthony Davis (WAS) | 32.0 | 18.3 | 10.6 | 2.1 | 15% | 61% | 0% |
| NYK@BOS | Jalen Brunson (NYK) | 35.0 | 23.8 | 3.6 | 5.7 | 44% | 0% | 22% |
| NYK@BOS | Karl-Anthony Towns (NYK) | 31.0 | 18.0 | 12.9 | 2.5 | 14% | 83% | 0% |
| NYK@BOS | Jayson Tatum (BOS) | 35.0 | 24.6 | 9.9 | 5.0 | 49% | 54% | 13% |
| NYK@BOS | Paul George (BOS) | 31.0 | 17.3 | 5.0 | 3.2 | 13% | 3% | 2% |
| ATL@CHA | Nickeil Alexander-Walker (ATL) | 34.0 | 20.2 | 3.8 | 3.0 | 26% | 1% | 1% |
| ATL@CHA | Jalen Johnson (ATL) | 35.0 | 19.8 | 11.2 | 6.8 | 22% | 68% | 37% |
| ATL@CHA | Brandon Miller (CHA) | 35.0 | 24.1 | 7.0 | 3.7 | 46% | 17% | 4% |
| ATL@CHA | Grayson Allen (CHA) | 33.0 | 19.6 | 4.8 | 4.7 | 23% | 3% | 10% |
| DET@MIA | Cade Cunningham (DET) | 35.0 | 24.9 | 5.9 | 9.1 | 50% | 8% | 69% |
| DET@MIA | Jalen Duren (DET) | 29.0 | 17.7 | 11.3 | 1.8 | 12% | 69% | 0% |
| DET@MIA | Giannis Antetokounmpo (MIA) | 33.0 | 29.6 | 12.2 | 6.2 | 73% | 77% | 28% |
| DET@MIA | Bam Adebayo (MIA) | 32.0 | 16.9 | 10.7 | 3.2 | 10% | 62% | 2% |
| NOP@UTA | Zion Williamson (NOP) | 32.0 | 23.8 | 6.5 | 3.3 | 44% | 12% | 2% |
| NOP@UTA | Trey Murphy III (NOP) | 35.0 | 20.1 | 5.9 | 3.6 | 25% | 8% | 3% |
| NOP@UTA | Lauri Markkanen (UTA) | 34.0 | 24.1 | 7.6 | 2.7 | 46% | 24% | 1% |
| NOP@UTA | Keyonte George (UTA) | 34.0 | 21.3 | 4.2 | 8.1 | 31% | 1% | 56% |
| HOU@SAS | Kevin Durant (HOU) | 36.0 | 25.4 | 6.2 | 3.7 | 53% | 11% | 3% |
| HOU@SAS | Alperen Sengun (HOU) | 32.0 | 18.1 | 9.8 | 4.7 | 14% | 52% | 10% |
| HOU@SAS | Victor Wembanyama (SAS) | 33.0 | 25.0 | 13.7 | 2.8 | 50% | 87% | 1% |
| HOU@SAS | De’Aaron Fox (SAS) | 31.0 | 16.5 | 4.0 | 4.9 | 10% | 1% | 12% |
| POR@SAC | Deni Avdija (POR) | 32.0 | 21.7 | 7.2 | 4.5 | 33% | 19% | 8% |
| POR@SAC | Ja Morant (POR) | 31.0 | 19.4 | 3.9 | 6.1 | 22% | 1% | 28% |
| POR@SAC | Zach LaVine (SAC) | 33.0 | 18.1 | 3.3 | 2.3 | 16% | 0% | 0% |
| POR@SAC | Domantas Sabonis (SAC) | 34.0 | 17.0 | 14.6 | 4.5 | 10% | 91% | 9% |
| MEM@GSW | Ty Jerome (MEM) | 32.0 | 25.0 | 4.1 | 7.8 | 50% | 1% | 53% |
| MEM@GSW | Jerami Grant (MEM) | 28.0 | 15.9 | 3.6 | 1.9 | 8% | 0% | 0% |
| MEM@GSW | Stephen Curry (GSW) | 33.0 | 32.5 | 4.6 | 4.7 | 81% | 2% | 11% |
| MEM@GSW | De'Anthony Melton (GSW) | 31.0 | 16.6 | 5.2 | 3.6 | 11% | 4% | 3% |
| LAC@LAL | Darius Garland (LAC) | 33.0 | 21.0 | 3.1 | 6.3 | 30% | 0% | 31% |
| LAC@LAL | Rui Hachimura (LAC) | 32.0 | 14.8 | 6.0 | 1.1 | 6% | 9% | 0% |
| LAC@LAL | Luka Doncic (LAL) | 35.0 | 30.2 | 7.8 | 7.5 | 75% | 26% | 47% |
| LAC@LAL | Austin Reaves (LAL) | 34.0 | 21.3 | 4.8 | 5.0 | 30% | 3% | 13% |

### Player prop distribution support

For all 147 player rows, outputs include points/rebounds/assists/3PM/steals/blocks/turnovers/fouls/fantasy means, 10–90% model quantiles, points 20+/25+/30+, 10+ rebounds, 8+ assists, 3+ made threes, PRA 30+/35+, and double-double threshold probability. Combined stats are sampled from the same joint game draws. These probabilities are **uncalibrated**.

Custom independent fantasy research scoring = PTS + 1.2×REB + 1.5×AST + 3×STL + 3×BLK − TO (not any platform scoring rule).

## Model diagnostics, original gates, and retrospective context

- All 12 game forecast probabilities sum to 1.0 for each side. Team regulation points reconcile to the sum of simulated named players plus the explicitly tracked bench `Other` group.
- Each team has exactly 240 regulation player-minutes for every draw; overtime is modeled for full-game game scores only, so player-market player totals are **not** market settlement compatible.
- CHI@MIL remains the immutable **12:59:04 PM PDT** v0.2.1-base forecast; all other 11 full-game outcomes freeze at **2026-10-23 1:08:19 PM PDT**. Simulation did not see CHI–MIL live score during the later run.
- On the previous October 21 slate, the **original v0.2.1 model** favored the eventual winner 7 of 11 times, with mean Brier ≈0.2011 and log-loss ≈0.5907. This is **descriptive retrospective grading**, not historical calibration, proof of edge or a reason to tune this snapshot.
- Model quality grade: **C / partial**; every row **WATCH (RESEARCH)**. This is a methodological gate, not a finding that a sportsbook edge is present.
- No external game-winner projections, line consensus, sportsbooks, Betfair/Kalshi quotes or fantasy forecasts entered independent predictions. **Market probability, no-vig, edge, fees, EV, buy threshold and CLV: N/A.**
- Model missing/limitations: validated long-run rolling backtest/calibration, actual five-man lineup stint histories, opponent defensive assignments, complete player shot-location and rebound chances, actual potential assists and touches, exposure correlations beyond shared basic game event draws, robust 2026 offseason effects.
- Owner-approved PASS gate and external commercial data permissions not established; no purchase recommendation.

## Sources

- [2025–26 team advanced stats (RealGM)](https://basketball.realgm.com/nba/team-stats/2026/Advanced_Stats/Team_Totals/Regular_Season)
- [2025–26 team shooting/FT totals (RealGM)](https://basketball.realgm.com/nba/team-stats/2026/Totals/Team_Totals/Regular_Season)
- [Official injury PDF (Oct 23, 3:45PM ET)](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-23_03_45PM.pdf)
- [Current NBA projected lineups and team recent minutes](https://nba-lineups.com/)
- [Original Daily Line Oct 21 independent v0.2.1 experiment](https://github.com/OneVillage83/Daily-NBA/blob/main/audits/2026-10-21-full-slate-shadow-v0.2.1.md)

## Immutable record protocol

Original probabilities, source-as-of times, assumptions, player outputs, deterministic seed, scenario-only what-if estimates and integrity hashes are archived separately. Future line movement will not change forecasts. Any factual lineup correction should create a **new version** with its own timestamp, never overwrite this record. Closing/outcome/Brier/log-loss/CLV appended **only** where authentic evidence exists.