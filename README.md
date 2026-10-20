# Daily NBA

The Daily NBA project is the NBA-specific prediction, simulation, and audit engine for **The Daily Line**.

> **Status (2026-10-20):** Architecture and requirements baseline only. No model, data feeds, historical backtests, or production recommendations have been implemented or validated in this repository. All forecasts must remain **shadow mode** until evidence-backed acceptance criteria are met.

## Mission

Use independently derived basketball outcome distributions based on **raw/advanced stats, play-by-play, factual player tracking, injuries/lineups, minutes/usage, rest, travel, and verified matchup context**. Never use sportsbook prices, betting consensus, third-party predictive forecasts, or fantasy projections to create or alter independent premarket probabilities.

### Model outputs

- Pregame win probability, fair moneyline, projected points, margin, spread/total distributions, team totals.
- Player points, rebounds, assists, 3PM, combo props (PRA/PR/PA/RA), double-doubles and independently derived fantasy points.
- Conditional player-availability scenarios: available / unavailable / restricted minutes; starting lineups remain clearly labeled projected until confirmed.
- Market-only stage **after** a timestamped forecast freeze: contract definition, no-vig where applicable, edge, fees, EV, uncertainty, buy threshold, PASS/WATCH/AVOID.
- Independent live snapshots (separate from immutable pregame records), then closing-line and actual-outcome validation.

## Architecture documents

1. [NBA model specification](docs/NBA_MODEL_REQUIREMENTS.md) — features, statistical engine, distribution design, modeling constraints and staged build.
2. [Data dictionary and ingestion contract](docs/DATA_DICTIONARY.md) — normalized statistics, minimum fields, data completeness, source permissions, provenance and quality.
3. [Shadow audit and acceptance](docs/SHADOW_AUDIT_SOP.md) — exact freeze-first audit sequence, quality gates, EV, calibration, release criteria.

## Pipeline

```text
Licensed/authorized factual data sources
  -> Daily Data Core ingestion + immutable, versioned feature snapshot
  -> Daily NBA team possession/efficiency model
     + minutes/usage/lineup-dependent player model
  -> coherent joint game+player outcome distributions
  -> independent fair probabilities + uncertainty + sensitivity
  -> timestamped frozen shadow forecast (pre-market)
  -> isolated market comparison: contracts / no-vig / fee-adjusted EV
  -> PASS / WATCH / AVOID + explicitly recorded price threshold
  -> final outcomes / closing line / calibration / Brier / log-loss / CLV
```

**LIVE:** separate live-data input and snapshot engine; live market prices never rewrite the frozen pregame forecast.

## Initial build order

1. Acquire and verify permitted historical + timely feeds; ingest team/game/player/play-by-play/injury/lineup/schedule inputs with timestamps and reproducible IDs.
2. Fit hierarchical, opponent-adjusted possession, efficiency, margin and total models. Validate chronological out-of-sample calibration.
3. Add minutes, availability, shot/rebound/assist opportunity player models; reconcile player and team totals within joint simulations.
4. Add actionable lineup/matchup context, independent fantasy outcomes and player/combination props.
5. Add market isolation, shadow recommendations, closing outcomes and automated audit exports.
6. Add independent live NBA engine only after snapshot/data latency tests.

No claimed model accuracy, live operation, source license, or performance is implied by this requirements repository.
