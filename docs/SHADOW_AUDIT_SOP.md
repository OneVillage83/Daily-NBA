# Daily NBA — Independent Shadow Audit SOP and Model Acceptance

**Version:** 0.1 (2026-10-20). Planned operating procedure. **No completed audit, trained model, live feed or validated PASS is claimed by this document.**

## 1. Canonical evaluation chain (fixed order)

1. **Game identification:** game ID, tipoff UTC/local, both teams, home/away, regulation/OT and exact market/settlement definition.
2. **Prediction timestamp:** what was factually available then, feature snapshot/hash, licensing and source freshness.
3. **Independent statistical stage:** historical factual team/player features, lineup/injury scenarios, schedule, adjustments; joint outcome simulations.
4. **Frozen fair probability:** win, margin/total/player-threshold probability, fair price, model distribution and seeds, uncertainty/model range, source coverage and assumptions. Store as immutable forecast **before viewing or importing market prices into the comparison run**.
5. **Independent original quality/gate state:** qualification readiness from uncertainty, scenario dispersion, data quality; no market used.
6. **Market comparison stage:** timestamped quoted prices, quote type, yes/no contract direction, bid/ask and liquidity when known, venue/settlement rules. Compute market probability, no-vig if coherent two-sided prices, edge, fee-adjusted EV, price threshold and recommendation gate.
7. **Later factual revisions:** never overwrite original; only reforecast on documented changed injury/lineup/role/weather-context evidence, each with its own as-of timestamp and frozen version. Separate pure price changes (do **not** rerun independent model).
8. **Closing line:** retain timestamped actual available closing quote, contract direction and fee context. If missing, mark unavailable; do not invent CLV.
9. **Outcome and grading:** official/stat-corrected result under exact contract rules; WIN/LOSS/PUSH/VOID as applicable; realized P&L accounting separately from probability accuracy.
10. **Scoring and review:** Brier, log-loss, reliability, predictive interval coverage, distributional scores (where applicable), realized EV/CLV and performance stratified by confidence, market/contract type, data quality and original gate.

For historical replay, the only admissible predictor is what was known at each original prediction time; postgame injuries and final player minutes may not be backfilled as pregame knowledge.

## 2. How to derive prices without contamination

For a probability p in (0,1):
- **Fair decimal odds** = 1 / p; **fair implied probability** = p.
- **Fair American odds**: if p >= 0.5, `-100 * p/(1-p)`; otherwise `+100 * (1-p)/p`. Display appropriate rounding without altering the underlying probability.
- **Market implied probability** from displayed decimal payout multiplier `d` *only when* the quoted contract truly pays `d` gross per unit staked on a win and 0 otherwise (before fees) is `1/d`; be explicit on whether quotes are multipliers, odds, contract share prices or net payouts.
- **Two-sided no-vig** can be computed using a documented normalization, e.g. `q_yes/(q_yes + q_no)` if two complementary **comparable quotes** refer to the same settlement and instant. Do not pretend normalization always removes exchange spreads/transaction costs or that unrelated contract prices form a two-way market.
- **Edge in probability points** = `p_model - p_market` for the specifically chosen side; fair quote threshold reflects uncertainty, fees, and contract definitions.
- **Fee-adjusted expected value per unit stake** for simple win/lose decimal odds: `EV = p * (d - 1 - fee_win) - (1-p) * (1 + fee_loss)` where fees are in stake units and this exact convention is applicable. For an exchange share with purchase price, variable fees/refunds, voids, partial fills and settlements, compute EV from the **actual cash flows of that contract**, not a universal decimal-odds shortcut.

**Uncertainty:** publish sensitivity to pace, efficiency, rotation, questionable player status and model dispersion. No false precision from Monte Carlo sample count; sampling error is not the same as model uncertainty.

## 3. Gate rules and price discipline

Allowed labels: **PASS**, **WATCH**, **AVOID** (retain all in results, including nonqualifying outcomes).

- **PASS:** permitted data/terms, sufficiently fresh critical observations, acceptable model calibration and uncertainty, scenario stability, minimum fee-adjusted EV buffer and a recorded maximum buy price / minimum gross payout threshold. User-approved production policy determines the final numeric requirements. A historical ~5% EV floor plus uncertainty cushion may be treated as **provisional for research only**, not as an automatically validated trading rule.
- **WATCH:** directional edge apparent but market price, lineups/injury certainty, sample quality, calibration, volume or uncertainty has not cleared the approved gate. State exact reason and threshold to revisit.
- **AVOID:** evidence, contract, liquidity, safety of data, model-uncertainty or projected EV inadequate; negative EV or critical data fault; record why.

Bet/stake size must **not** change the underlying fair probability. Correlated exposure should be flagged across ML/spread/total and players, between game legs and shared injury/game-pace sources. Do not multiply leg probabilities as independent when correlated.

**Pre-price threshold** should be derived and logged in same comparison evaluation from p and policies, not retrofitted after seeing a preferred line. If prices move with no factual model update, recompute only market/EV/gate against the unchanged frozen p.

## 4. Required audit row schema

**Audit identity:** `audit_id`, league, season, game, selection side, contract descriptor, regulation/full-game/OT, threshold/half-point, time zone, event start.

**Forecast:** `prediction_id`, frozen_at, scenario ID, feature hash, model version, seed, independent win/cover/threshold p, fair odds, prediction interval, sensitivity, data quality grade, injury/starting-five assumptions, completeness codes.

**Market:** `market_snapshot_id`, venue, quote timestamp, bid/ask/last (with proper interpretation), side, full settlement terms, fees/liquidity assumptions, market p, no-vig rule, edge, fee-adjusted EV, original gate and explicit buy threshold.

**Lifecycle:** factual updates and distinct prediction IDs, subsequent market-only evaluations, closed_at/closing quote, settled_at, actual result, stake-independent forecast metrics and stake-dependent realized P&L if applicable. Null and `unavailable` are valid for absent market or closing quotes; do not fabricate.

Append-only event history. No original frozen probability may be replaced during postgame evaluation.

## 5. Pregame versus live

Live NBA must use the **same evidence-first principle**, not the same stored probability. At each live snapshot record: remaining regulation time, period, score differential, possession, players currently on floor, foul state, recent substitution, remaining expected possessions, live event feed latency, snapshot timestamp, and conditional scoring distribution.

A live model may condition on observed current score and factual play-by-play **only**. Live odds are introduced after a distinct, live-versioned prediction freeze. Compare each live forecast to eventual settlement separately and never overwrite pregame outcomes or calibration denominators.

When provider data is delayed or conflicting, pause live PASS rather than assume current lineup/possessions.

## 6. Model evaluation, safety and tests

### Reproducibility
- Snapshot hash + frozen timestamp + model/parameters/feature versions + deterministic seed.
- Every reported number can be reconstructed from the archived inputs.
- Block premarket modeling stages from importing or reading market-related tables/fields by API and test.
- Preserve both original recommendation and any future model revisions.

### Statistical validation
- Chronological holdout, forward-chaining backtests; no temporal leakage.
- Moneyline: Brier, log-loss, reliability bins and calibration plots.
- Margin, total, player count distributions: proper distributional scoring (CRPS or log predictive density as appropriate), quantile coverage, PIT/discrete calibration checks; compare full predictive distributions rather than only average absolute error.
- By market and situation: data quality, early season, opponent strength, injuries, back-to-backs, home/away, blowout probability, and contract rule variants.
- Accuracy-first policy: a claimed “edge” is never validation by itself; analyze sample size, confidence intervals, transaction fees, liquidity, selection bias and CLV only when a real quote exists.
- Baseline and ablation tests: adding tracking, lineup or defensive-matchup features must show defensible out-of-sample gain or robustness.

### Minimum functional test matrix (proposed)
| Test | Expected result |
| --- | --- |
| No sportsbook info before freeze | Market input prohibited / detected |
| Historical replay with late injury report | Injury unavailable until publication time |
| Questionable star player | Conditional scenarios saved, not silently merged |
| Missing verified lineup | Projected labeled and uncertainty widened / gate qualified |
| Line move with no factual change | Original model p unchanged |
| Material new fact | New linked frozen prediction, old version retained |
| OT and regulation-only markets | Contract-aware probabilities and settlement |
| Correlated PRA / double-double | From joint event simulations, not independent marginals |
| Team/player scoring consistency | Shared possessions and point totals reconcile within rules |
| Absent/stale tracking | Approved documented fallback or BLOCK PASS |
| Market fee / bid-ask variation | Recomputed EV and threshold from exact contract cash flow |
| Missing close, no-bet and lost props | Preserved ledger; no fabricated closing quote |
| Postgame audit | Original p + timestamp retained for Brier/log-loss |
| Live snapshot | Separate version, evidence and error/latency accounting |

## 7. Proposed acceptance gates

There is **no automatic promotion** from documented design to qualified production. Require an authorized, licensed data source; reproducible dataset and training scripts; leak-free OOS benchmarks versus simple baselines; demonstrated probability and interval calibration; simulation/stat reconciliation; reliable premarket freezes, QA and error handling; documented data-quality grades; and owner approval of numerical EV/uncertainty thresholds and user presentation.

Keep the initial implementation in **shadow mode**. Even a fully functioning model cannot claim a verified market edge without enough tracked, prospective performance evidence.

## 8. Audit report format

Each game report should state: as-of time and source coverage; expected possessions, projected points and fair ML/spread/total distributions; injury-conditioned scenarios and assumptions; uncertainty / DQ; timestamped original premarket forecast; later market price, edge/fee-adjusted EV, PASS/WATCH/AVOID and exact buy threshold. Each player row should include expected minutes, raw component opportunities, distribution and scenario dependence.

At close and postgame, append observed outcomes, frozen-vs-closing accuracy, Brier/log-loss/CLV where documented, and whether the original recommendation met the gate. Never erase an earlier losing selection or upgrade it retroactively.

See [Model Requirements](NBA_MODEL_REQUIREMENTS.md) and [Data Dictionary](DATA_DICTIONARY.md).
