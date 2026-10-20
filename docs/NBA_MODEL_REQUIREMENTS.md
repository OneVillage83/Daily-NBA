# Daily NBA — Independent Model Requirements & Architecture

**Version:** 0.1 (requirements baseline)  
**Date:** 2026-10-20  
**Status:** Proposed implementation specification; **SHADOW MODE ONLY**; **not implemented or calibrated**.  
**Project:** The Daily Line / Daily NBA. Owner retains final approval over deployment, gates and product changes.

## 1. Mission and non-negotiable rules

Build an original, possession-based, lineup-aware NBA outcome engine generating *coherent independent* team and player distributions. Inputs in the prediction stage are factual observations only: box scores, raw/advanced rates, possession and play-by-play facts, officially/legitimately sourced tracking, availability, scheduling and weather only when causally relevant (NBA indoor arena weather normally not a direct game input).

**Never feed into the independent prediction stage:** third-party predictive models, consensus picks, sportsbook implied probabilities, betting market movements, externally produced fantasy projections or ratings derived from betting markets. Retain source provenance and timestamps. Model training/testing must prevent look-ahead leakage. After prediction and uncertainty are frozen, market prices can be compared for no-vig, edge, fee-adjusted expected value and PASS/WATCH/AVOID only.

All unqualified selections remain visible in the ledger. Pregame, live, injury-conditioned and post-news revisions are versioned separately; no silent overwriting.

## 2. Required statistical inputs

### 2.1 Team and opponent baselines (critical)

| Feature | Meaning / recommended treatment |
| --- | --- |
| Offensive rating (OffRtg) | Points scored per 100 team possessions. Model possession-weighted and opponent-adjusted. |
| Defensive rating (DefRtg) | Points allowed per 100 opponent possessions. Opponent-adjusted. |
| Pace | Possessions per 48 regulation minutes; project actual joint possession count, not two unrelated values. |
| Four factors: eFG%, TOV%, OREB%, FTr | Shooting, turnover, offensive rebounding and free-throw creation. Track both for and allowed, with exact denominator/definition. |
| FGA, 2PA, 3PA, 3P%, 3PA rate | Volume and type of shooting; attach shooting uncertainty. |
| Rim, paint, midrange, corner-three, above-break-three attempt rates/accuracy | Location-specific offensive profile versus defense's allowed profile. Use when source licensed/available. |
| Free-throw attempts and FT% | Separate FTA creation from FT conversion. |
| Points in the paint, transition and half-court efficiency | Situational scoring, when a verifiable definition/feed exists. |
| Team foul rate and opponent fouls drawn | Foul/bonus and free-throw exposures. |
| Offensive / defensive rebound chances, box-outs | Enhanced possession/rebounding features where available. |
| Home/away and opponent strength | Explicit contextual and schedule adjustments. |
| Net rating and TS% | Diagnostic/redundant descriptive metrics; avoid double counting as independent explanatory signals. |

Minimum observation horizons: prior seasons (up to ~3 relevant seasons, weighted/rebased for roster changes), current season, last 20/10/5 games, home/away, and on/off situations. Choose weights/shrinkage through chronological cross-validation; no fixed arbitrary recent-game dominance. Track denominator, possession count, sample size and coverage for every rollup.

### 2.2 Player rates and opportunities (critical for props)

- Projected and observed minutes, starters/bench roles, rotation slots, minute volatility and minutes restrictions.
- Usage rate, touches, time of possession, drives, paint touches, shot attempts/minute, 2PA/3PA/FTA volume, assisted/unassisted shot type and shooting accuracy by zone.
- Potential assists, passes, assist-conversion rate, and teammate-dependent shot opportunities; measure assists from opportunities rather than APG alone.
- Rebound chances, contested/uncontested rebounds, rebounding conversion, missed-shot opportunities and role/position.
- Fouls per minute, foul trouble, steals, blocks, turnovers, and defensive assignment facts if available.
- Starter and 2-/3-/5-player lineup possessions, substitution sequences, with/without-teammate usage and minute changes; label small-sample effects explicitly.
- On/off-court scoring rates and teammate dependencies; avoid treating unadjusted on/off as causal without lineup/opponent adjustment.
- Independent fantasy points derived from these player statistical outcomes and a stated scoring system, **before** looking at fantasy market prices.

### 2.3 Matchup interactions

- Offense shot-location frequencies and expected conversion versus opponent location-specific attempts allowed, rim protection, perimeter defense.
- Ball-handler versus scheme (drop, switch, zone where classified from sourced events), drive lanes, pick-and-roll action rates and frequency of transition chances.
- Available opponent lineup, projected cross-matches, height/size/rim protection only where observed and reproducible.
- Team turnover pressure, transition creation/prevention, foul propensity, opponent rebounding and second-chance quality.
- Record sample strength, matchup relevance and uncertainty. Use partial pooling to avoid noise from short head-to-head matchup samples.

### 2.4 Situational and availability

Official injury reports, suspected/probable starters **labeled projected**, lineup confirmation timestamps, questionable/out/doubtful/available statuses, restrictions, recent trades, rotation changes, back-to-backs, 3-in-4 scheduling, venue/home court, altitude, travel/time zones, rest days and game importance when supported. Injury-dependent team/player scenarios must be explicit and separately frozen.

Do not assume a 2025-26 team roster or prior-year player role persists into 2026-27 without validation.

## 3. Prediction engine: coherent team and player distributions

### 3.1 Pregame engine

1. Resolve pre-tipoff *as-of* features. Carry season/lineup changes and uncertainty.
2. Project joint regulation possessions from home/away pace, opponent interactions, rest/rotation and uncertainty. Account for possession timing/clock, end-of-period effects and game state where supportable.
3. Infer opponent-adjusted offensive efficiency from the four factors, shot profile, lineup and situational effects. Retain partial-pooling priors to stabilize small samples; prevent overlapping metrics from causing double counting.
4. Construct joint regulation scoring distribution for both teams. A descriptive expectation: projected points ~= projected possessions * adjusted OffRtg / 100. This is **not** itself a complete probabilistic model.
5. Couple possessions, shooting accuracy, rebound/turnover opportunities, fouls/bonus, player minutes and game script so score margin, totals and player props remain statistically coherent.
6. Explicitly model overtime eligibility/probability and points when full-game/including-OT contracts require it. Treat regulation-only markets separately.
7. Simulate reproducibly (seed/model version) or use an equivalently validated probabilistic method. Output predictive intervals, sensitivity, and calibration bins, not point estimates alone.

### 3.2 Player engine

Estimate minute distributions conditioned on injury/rotation, early foul trouble, competitiveness/blowout and availability. Within shared team possessions allocate usage and event opportunities with lineup constraints. Estimate point outcomes (2PA/3PA/FTA + conversion), assists from potential assists and teammate makes, rebounds from shared missed shots/rebound chances, steals/blocks/turnovers from fitted event opportunities. Enforce feasible totals and reconciliation.

Build joint rather than independent marginal distributions for points/rebounds/assists, 3PM, double-doubles, combined thresholds, and fantasy point scoring. Explicitly measure dependencies among team totals, player touches, pace and playing time. For example, do **not** sum marginal PRA probabilities as if independent.

### 3.3 Probability and uncertainty outputs

**Team markets:** win probability, fair decimal/American odds, margin and score expectations + intervals, spread-cover probabilities at specified contract lines, full-game/regulation total distributions, team totals, quarters/halves when supported.

**Player markets:** points/rebounds/assists/3PM thresholds, alternate ladders, PRA/PR/PA/RA, double-double, triple-double and independent fantasy scoring with exact stat/settlement definitions.

Every prediction records:
- `prediction_id`, model & feature versions, UTC and local timestamps, tipoff, as-of cutoff, source IDs and data-received timestamps;
- scenario ID and probability assumptions **if** scenario blending is used; do not disguise assumed scenario weights as observed data;
- fair probability and price, Monte Carlo/epistemic interval, data-quality state, missing inputs and sensitivity to lineup/pace;
- ledger status before and after market entry, never conflated.

## 4. Early season, drift, and missing data

At season start, use transferable multi-season player skill priors plus reconstructed **current-roster** lineup/rotation expectations. Shrink toward broad position/team population where sufficient history is absent. Update rolling trends via learned recency weights and explicit drift/roster-change triggers.

A missing critical injury status, unreliable source rights, unavailable rotation data or stale roster must lower confidence or block PASS; never silently substitute a fabricated metric. Lower-priority optional tracking missing may fall back to box score+play-by-play with documented wider uncertainty and a testable missingness policy.

Always preserve projected versus confirmed lineups, record when updates arrive, and only rerun a distinct prediction version when material evidence changed; never post-edit the earlier frozen record.

## 5. The Daily Line integration boundaries

```text
Factual source adapters (rights verified; timestamped)
        |
The Daily Data Core (normalized game/player/team/lineup/possessions/injuries)
        |
Daily-NBA raw features and as-of snapshot
        |
Team efficiency + shared possessions   Player minutes + usage/role
        |                                  |
        +----> coherent joint NBA simulation <----+
                           |
        probability / fair price / intervals / DQ
                           |
               IMMUTABLE PREGAME FREEZE
                           |
       market odds, no-vig, fees, edge, EV, gates
                           |
       report / archive / infographics / website
                           |
       settlement + closing line + validation
```

Daily Data Core owns shared source normalization and provenance; Daily-NBA owns sport-specific assumptions, feature engineering, model and calibration. Daily-NBA Live consumes a separate timestamped live snapshot; it must **not** mutate the pregame forecast.

The website should expose projected/confirmed lineups, as-of timestamp, scenario version, independent fair price, data quality, PASS/WATCH/AVOID, and sensitivity/why; do not present a shadow result as live validated advice.

## 6. Staged implementation

| Stage | Deliverable | Acceptance focus |
| --- | --- | --- |
| 0: Rights + schema | Authorized historical/live feed matrix, feature definitions, primary keys and source provenance | Access and commercial use confirmed; no unlicensed production dependencies |
| 1: Team pregame baseline | Pace, opponent-adjusted efficiency, point/margin/ML/spread/total simulations | Leak-free time-split evaluation, probabilistic calibration, reproducibility |
| 2: Player distributions | Minutes, usage, attempts, assists/rebounds, player/combination and fantasy outcomes | Player-to-team reconciliation, sensible joint correlations, calibration |
| 3: Matchups and lineup refinement | Shot zones, opponent schemes, partial-pooling lineup effects | Measurable out-of-sample incremental gain; ablation tests |
| 4: Market and shadow audit | Contract-normalized prices, market isolation, fee-adjusted EV, gates, outcome and CLV ledger | Freeze proof, correctness tests, missingness gates; **no auto publishing** |
| 5: Live NBA | Live possession/substitution/foul state and separate versioned distributions | Latency/provenance, separate audit, no pregame contamination |

No stage is considered implemented merely because it appears in this document.

## 7. Testing and release controls

- Train/validation/test are strictly chronological; use rolling-origin evaluations and historical **as-of** injuries/lineups. Include no future final box-score fields in pregame input.
- Evaluate fair probability with Brier, log-loss, reliability curves and intervals; margin/totals/props with proper distributional scores and coverage; segment by home/away, rest, injury uncertainty, early season and line types.
- Compare an explicit simple team-efficiency baseline against each complex feature addition. Keep only out-of-sample improvements or defend separately on predictive robustness.
- Validate Monte Carlo reproducibility, feasible possession/stat counts, shared event accounting, contract settlement, OT, missing-data cases and sample-size shrinkage.
- Store original predictions, revisions, outcomes, closing lines and fees to evaluate CLV and forecast calibration without survivorship bias. Retain PASS, WATCH and AVOID rows.
- Production, direct wagering integrations or release gates require owner review and evidence-backed acceptance. User-facing material must be accurate about model readiness and data-feed licenses.

## 8. Open design questions (resolve with evidence)

1. Which feeds have written commercial/analytics/odds-adjacent usage rights, viable historical depth, player tracking and live latency?
2. Exact player-stat contract settlement scopes (regulation versus OT, official corrections) and supported market taxonomy?
3. Learned priors for roster-change and recency, out-of-sample sharpness/calibration, and uncertainty/quality gates?
4. Robust lineup/injury scenarios when starting lineups are unpublished?
5. Model service interface, storage choices and schema compatibility with the existing Daily Data Core and Daily Line reports?

See [Data Dictionary](DATA_DICTIONARY.md) and [Shadow Audit SOP](SHADOW_AUDIT_SOP.md) for operational details.
