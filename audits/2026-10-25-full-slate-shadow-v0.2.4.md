# The Daily Line — NBA October 25, 2026 | Independent Full-Slate Shadow Audit v0.2.4

**Mode:** experimental/untrained/unvalidated research. **7 NBA games; 60,000 seeded simulations each; 89 named-player records.** This audit contains a pregame **independent** model forecast, without sportsbook, consensus, third-party predictions, or external fantasy projections used as inputs. **PASS 0; WATCH 7; AVOID 0; EV/CLV N/A.**

## Provenance, timestamp and freeze rules

- **Immutable pregame freeze:** 2026-10-25T16:19:31+00:00 = **9:19:31 AM Pacific**, before the first game at 2:00 PM Pacific.
- **Official injury input:** Oct 25, **11:30 AM Eastern / 8:30 AM Pacific** NBA bulletin. A 12:00 PM Eastern bulletin was subsequently consulted only as a follow-up, not inserted retroactively into the original frozen forecast.
- **Model ID:** `tdl-nba-2026-10-25-v0.2.4-shadow-uncalibrated`; seed `20261025024`.
- **Original full machine-readable simulation JSON integrity SHA-256:** `3d84393c7c1e11df1407510b5e586d06abb70f4818088e8a4a83a18a0f45866b`. Original filename `nba_2026_10_25_frozen_shadow_v024.json`. Archived in the dated companion research ZIP; never rewrite the original JSON for later lineups, market prices, or outcomes.
- **Model source SHA-256:** `8cee8b52b2002bae11a77cbaeb6f9fe367576e68487921806897c22a544e353d` (`nba_2026_10_25_shadow_v024.py`). All original data-source references and analyst roster/role adjustments are retained in frozen JSON and source.
- **Historical observations:** 2025–26 OffRtg/DefRtg, pace, eFG%, OREB%, team turnover/rebounding, 3PA and FTA opportunities; current 2026–27 first 2–3 games used only as weak, explicit short-sample empirical scoring context; current injury/availability facts, projected rotations, rest and matchup.
- **Unfitted analyst assumptions:** roster efficiency deltas, assumed game script/minutes, pace/prior event rates; not validated NBA player tracking or measured WOWY. Injury scenario probabilities NOT invented.
- Team score/moneyline includes approximate overtime; **player stats are regulation-only** and not exact full-game player prop settlement probabilities.

## Original independent game forecasts (immutable)

| Away @ Home | Model winner | P(win) | Fair American price (not market) | Projected away-home points | Total | Expected home margin | Simulated total 10–90% |
|---|---|---:|---:|---|---:|---:|---|
| LAL@UTA | LAL | 58.3% | -140 | 120.1–116.0 | 236.1 | -4.1 | 209–264 |
| IND@BKN | IND | 53.0% | -113 | 114.3–112.8 | 227.0 | -1.5 | 200–255 |
| TOR@MIN | TOR | 52.2% | -109 | 114.6–113.6 | 228.3 | -1.0 | 201–255 |
| ORL@NYK | NYK | 72.2% | -259 | 106.4–117.7 | 224.1 | +11.2 | 197–251 |
| LAC@OKC | OKC | 76.9% | -333 | 103.5–117.5 | 221.0 | +14.1 | 194–248 |
| DET@PHI | DET | 61.6% | -160 | 115.4–109.8 | 225.1 | -5.6 | 199–252 |
| MEM@SAC | SAC | 50.4% | -101 | 115.8–116.0 | 231.8 | +0.2 | 205–259 |

**Home margin = projected home minus away points.** The original DET/PHI baseline explicitly assumes Embiid rests after Saturday and LeBron remains unavailable, while the official Philadelphia report was not submitted at the initial source cut. All original starting lineups are projected unless verified otherwise. Brooklyn's official team report also remained pending.

### Evidence, context, and qualitative matchup factors

- **LAL/UTA:** LAL eFG% 57.3% vs UTA 53.6% historical, but Lakers defense not elite; Doncic/Reaves scoring against Markkanen and Jaren Jackson Jr.; Walker Kessler available, Jusuf Nurkić out.
- **IND/BKN:** both had weak defenses (historical 118.8 and 119.0 DefRtg respectively); Haliburton/Siakam vs Porter Jr./Randle, Brooklyn Saturday rest disadvantage. T.J. McConnell out, Aaron Nesmith probable. Very close baseline.
- **TOR/MIN:** both started 2–0, Toronto historical defensive profile good and new Leonard/Barnes lineup versus Edwards/Ball for MIN; DiVincenzo out. Tiny current-season samples, favorite fragile.
- **ORL/NYK:** Orlando Banchero and Jonathan Isaac out; uncertain Black availability. Knicks Brunson/Towns projected core, historical efficiency advantage despite 0–2 early start.
- **LAC/OKC:** elite OKC historical defense (107.7 points/100), Clippers Bradley Beal and Brandon Ingram unavailable; Thunder more rest, projected Shai/Holmgren core.
- **DET/PHI:** Detroit missing Jalen Duren, Ausar Thompson questionable; PHI played the previous night and Embiid expected rest rather than official ruled-out. High two-sided roster sensitivity.
- **MEM/SAC:** Memphis Zach Edey out, Cedric Coward questionable; Sacramento Keegan Murray questionable, Sabonis projected to rebound heavily. Baseline almost exactly 50/50.

## Selected independent player projections — regulation only

| Player | Team | Expected PTS | REB | AST | Example threshold probability |
|---|---|---:|---:|---:|---|
| Luka Dončić | LAL | 31.9 | 8.0 | 7.9 | 25+ PTS 80% |
| Austin Reaves | LAL | 22.5 | 4.9 | 5.3 | — |
| Lauri Markkanen | UTA | 23.8 | 7.4 | 2.7 | — |
| Tyrese Haliburton | IND | 17.3 | 3.8 | 7.9 | 8+ AST 53% |
| Pascal Siakam | IND | 23.3 | 7.2 | 3.3 | — |
| Michael Porter Jr. | BKN | 24.7 | 7.5 | 3.1 | 3+ 3PM 76% |
| Kawhi Leonard | TOR | 24.4 | 6.7 | 3.3 | — |
| Anthony Edwards | MIN | 25.2 | 5.5 | 3.2 | 25+ PTS 51% |
| LaMelo Ball | MIN | 20.8 | 6.4 | 7.4 | — |
| Franz Wagner | ORL | 21.5 | 7.1 | 3.6 | — |
| Jalen Brunson | NYK | 25.2 | 3.4 | 6.3 | — |
| Karl-Anthony Towns | NYK | 20.3 | 13.2 | 3.0 | 10+ REB 85% |
| Shai Gilgeous-Alexander | OKC | 29.1 | 4.6 | 5.8 | 25+ PTS 71% |
| Chet Holmgren | OKC | 18.5 | 10.6 | 1.6 | 10+ REB 61% |
| Cade Cunningham | DET | 26.8 | 6.5 | 9.6 | 8+ AST 74% |
| Paul Reed | DET | 11.2 | 11.0 | 2.1 | 10+ REB 66% |
| Tyrese Maxey | PHI | 23.9 | 4.6 | 5.8 | — |
| Jaylen Brown | PHI | 25.8 | 8.4 | 4.8 | — |
| Ty Jerome | MEM | 27.4 | 4.3 | 9.6 | 8+ AST 75% |
| Domantas Sabonis | SAC | 18.2 | 15.4 | 4.7 | 10+ REB 94% |

**Important caution:** Jerome's projection scales up a very small historical sample to a manually projected 33-minute role and is high uncertainty. All threshold estimates are uncalibrated and exclude player OT. Full 89 player rows and composite props, three-point, steals, blocks, fouls, turnovers and fantasy outputs are archived separately.

## Unweighted and separately evaluated injury scenarios (never alter original forecast)

| Game | Hypothetical change from baseline | Original home P(win) | Conditional home P(win) |
|---|---|---:|---:|
| DET@PHI | Embiid **active** 31m rather than rest | 38.4% | 46.0% |
| DET@PHI | Ausar Thompson **out** rather than active | 38.4% | 41.5% |
| MEM@SAC | Cedric Coward **active** 28m vs expected out | 50.4% | 48.5% |
| MEM@SAC | Keegan Murray **out** vs baseline active | 50.4% | 46.5% |
| ORL@NYK | Anthony Black **active** 23m vs baseline unavailable | 72.2% | 71.0% |

These are manual what-if team/player effects, not estimated causal WOWY nor probabilistically blended status forecasts.

### Model-parameter sensitivity (±4 opposite OffRtg changes, NOT calibrated intervals)

| Game | Base home P(win) | Range from stress scenarios |
|---|---:|---:|
| LAL@UTA | 41.7% | 30.1–54.0% |
| IND@BKN | 47.0% | 35.0–59.3% |
| TOR@MIN | 47.8% | 36.2–59.7% |
| ORL@NYK | 72.2% | 61.5–81.5% |
| LAC@OKC | 76.9% | 66.9–85.1% |
| DET@PHI | 38.4% | 27.7–50.4% |
| MEM@SAC | 50.4% | 37.7–63.1% |

## Independent forecast versus post-freeze market-context observation

Only **after** original immutable forecast was written did a sports lineup page present indicative spreads/totals for these games, e.g. LAL -6.5 / total237.5; IND -7.5 / 231.5; MIN -1.5 /230.5; NYK -7.5 /224.5; OKC -15.5 /223.5; PHI -1.5 /228.5; MEM -3.5 /235.5. Those lack verified execution timestamp, comparable two-sided executable quotes, fees and contract terms, hence no market-no-vig, EV, buy threshold or CLV claims. Large model/reference disagreements such as IND -7.5 versus our tiny away margin or PHI reference favoritism versus DET favored under Embiid-rest assumption are **research flags, NOT qualified edges**.

## Previous day's out-of-sample diagnostic — separate and not used to retrofit Oct 25

The Oct 24 frozen v0.2.3 model favored **7/8 winning teams**, mean ML Brier **0.1501**, mean log-loss **0.4791**, mean absolute total score error **15.2 points**. Crucially, observed game totals were on average **13.4 points HIGHER** than the prior model's predictions. This is a meaningful model-misspecification warning on only eight observations, **not** evidence of calibrating today's totals; the Oct25 frozen forecast was not altered. No under recommendations may pass without a larger chronological calibration sample.

## Statistical/data-quality restrictions and gates

Structural unit checks passed for this research run: 7 games, p_home+p_away=1, 240 simulated player regulation minutes/team, player points reconciled to team points, excluded confirmed-out players, deterministic RNG, no odds in prediction feature store.

Critical *unresolved* components: validated season-specific five-man lineup stints/WOWY, actual potential assists/rebound chances/optical touches, reliable opponent shot-zone and defensive coverage data, fitted and chronologically backtested roster/injury deltas, calibration across multiple seasons, real player overtime opportunities, confirmed starter reconciliation and commercial-data rights. Data quality **C/partial**, and PHI/BKN injury availability unresolved as of original cut. Model intervals capture simulated game randomness, NOT full epistemic/model uncertainty.

**Gate all games: WATCH-RESEARCH. PASS 0; WATCH 7; AVOID 0.** No approved wager, no demonstrated model edge, no authenticated quote/fees, no-vig or CLV.

## Sources (factual research only; source-use licensing not asserted)

- [NBA official October 25 schedule](https://www.nba.com/games?date=2026-10-25)
- [NBA 11:30 AM ET official injury report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-25_11_30AM.pdf)
- [2025–26 NBA advanced team rates](https://basketball.realgm.com/nba/team-stats/2026/Advanced_Stats/Team_Totals/Regular_Season)
- [2025–26 NBA team totals](https://basketball.realgm.com/nba/team-stats/2026/Totals/Team_Totals/Regular_Season)
- [2026–27 early standings/results](https://www.basketball-reference.com/leagues/NBA_2027_standings.html)
- [Embiid expected rest, pregame reporting](https://www.reuters.com/sports/basketball/unbeaten-76ers-pistons-test-mettle-early-season-showdown--flm-2026-10-25/)
- [Post-freeze reference lines](https://www.rotowire.com/basketball/nba-lineups.php)

### Companion archive identity

Model/source, full independently frozen input/output JSON, two CSV exports (games, 89 player rows), sensitivity cases and last-day Brier/total grading CSV are preserved in research bundle `daily_nba_2026_10_25_full_slate_shadow_v024_bundle.zip`. Original freeze SHA at top; append future market-only checks and postgame grading as new files rather than altering this one.
