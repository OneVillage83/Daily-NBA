# Daily NBA — Data Dictionary and Ingestion Contract

**Version:** 0.1; **2026-10-20**. Specification only; no connectors have been implemented or authenticated.

## 1. Source policy

Only collect verifiable, appropriately licensed factual basketball data. Candidate categories: official box scores/play-by-play and standings; reliable injury, roster, starters and schedules; licensed play-by-play, player tracking and lineup data. NBA Stats public-site access does **not** automatically grant commercial or betting-adjacent redistribution/use. Evaluate NBA-specific terms and each provider's permitted derived works, caching, historical use, live access and redistribution **before** selecting production adapters.

Keep a source register:
`source_id`, provider, endpoint/dataset, rights status, permission evidence/reference, update schedule, timezone, historical coverage, fields, reliability, latency, attribution obligations, retention/deletion limits, fallback precedence and access restrictions.

Avoid scraped unofficial feeds for commercial production absent appropriate permission. No third-party precomputed predictions, odds-adjusted team ratings or fantasy projection feeds in the independent feature store.

## 2. Primary keys, time and provenance

Every fact must be traceable. Required data lineage per observation:

| Field | Type | Meaning |
| --- | --- | --- |
| `source_id` | string | Registered authorized provider |
| `source_record_id` | string | Original ID if present |
| `league` | enum | `NBA` for this repo; keep NCAAB elsewhere or segregated |
| `season_id` | string | Season label / ID |
| `game_id` | string | Canonical game ID, mapped to provider IDs |
| `team_id`, `player_id` | strings nullable | Stable canonical IDs |
| `event_id`, `period`, `clock` | typed nullable | For event and live play-by-play |
| `event_time_utc` | timestamp nullable | When observation/event occurred |
| `provider_published_at_utc` | timestamp nullable | When provider says it was published |
| `ingested_at_utc` | timestamp | Our ingest time |
| `available_to_model_at_utc` | timestamp | Earliest provable availability |
| `updated_at_utc` | timestamp | Provider correction time |
| `snapshot_id` | string | Versioned as-of feature snapshot |
| `definition_version` | string | Metric / units / denominator definition |
| `raw_hash` | string | Integrity and changed-input detection |
| `status` | enum | preliminary/confirmed/corrected/unknown |
| `missing_reason` | nullable enum | not_published/not_licensed/not_applicable/source_unavailable/stale/unknown |

Required: clock synchronization, original timezone preservation, conversion to UTC, tipoff-local display timezone and rejection of future-dated inputs for historical replay. NBA games that begin before midnight and finish the following date must retain one game ID. Do not interpret a postgame-corrected record as a pregame-known fact.

## 3. Game/team core feature families

The table defines normalized **raw observations or reproducibly computed statistics**, not the outputs of other betting models.

| Column / family | Units / definition | Need | Data window |
| --- | --- | --- | --- |
| `tipoff_at_utc`, `home_team_id`, `away_team_id`, `venue_id` | timestamp / IDs | Required | Each game |
| `regulation_periods`, `period_seconds`, `game_status` | regulation vs OT schema | Required | Each game |
| `points_for`, `points_against` | final and by-period integers | Required | By period/game |
| `possessions_for`, `possessions_against` | per defined possession methodology | Required | By team/game |
| `off_rating`, `def_rating` | points per 100 possessions | Required | Prior seasons and rolling |
| `pace` | possessions / 48 regulation minutes | Required | Prior seasons and rolling |
| `fga`, `fgm`, `two_pa`, `two_pm`, `three_pa`, `three_pm` | counts | Required | By team/game |
| `fta`, `ftm`, `oreb`, `dreb`, `tov` | counts | Required | By team/game |
| `efg_pct`, `tov_pct`, `oreb_pct`, `ft_rate` | defined four-factor proportions | Required | Factual computed rollups |
| `opponent_adjusted_off`, `opponent_adjusted_def` | in-house model-derived coefficients | Required model outputs, **not external inputs** | Frozen feature version |
| `shot_zone`, `shot_attempts`, `shot_makes` | rim/paint/midrange/corner3/above-break3; mutually consistent definitions | Phase 3 | Event and rolling |
| `transition_possessions`, `halfcourt_possessions`, points | possession-specific counts | Phase 3 | Event and rolling |
| `team_fouls`, `opponent_ft_opportunities` | counts, period context | High | Game/period |
| `lineup_id`, `lineup_possessions`, `on_off_rates` | five-player IDs + sample size | Phase 2/3 | Segment/game/rolling |

**Metric definitions:** For example, eFG% = (FGM + 0.5 * 3PM) / FGA. FT rate can mean FTA/FGA or FTM/FGA depending on a provider; choose and version exactly one for model calculations and label conversion. TOV% also has competing estimators; record its exact denominator. Model possessions may be event-derived or an estimate (e.g., using FGA, OREB, TOV and FTA); store the estimator and distinguish from exact play-by-play.

Collect home/away, last 5/10/20, season-to-date, prior-season baselines, and opponent adjustments as *computed as-of views*, never permanently rewritten fields. Store underlying possessions/sample sizes for shrinkage.

## 4. Player and opportunity families

| Column / family | Units / definition | Need |
| --- | --- | --- |
| `minutes_played`, `started`, `rotation_stint` | seconds and stint identifiers | Required |
| `projected_minutes_distribution` | internal forecast only, not third-party input | Model output |
| `usage_pct`, `fga_per_min`, `three_pa_per_min`, `fta_per_min` | per possessions/minute with denominator | Required |
| `two_pa`, `two_pm`, `three_pa`, `three_pm`, `fta`, `ftm` | actual counts | Required |
| `points`, `assists`, `rebounds`, `oreb`, `dreb` | actual box-score counts | Required |
| `turnovers`, `steals`, `blocks`, `personal_fouls` | counts | Required |
| `touches`, `time_possession`, `drives`, `paint_touches` | provider-defined tracking counts | Phase 2/3 |
| `potential_assists`, `passes`, `secondary_assists` | opportunity counts, **not a fantasy prediction** | Phase 2 |
| `rebound_chances`, `contested_rebounds` | opportunity counts | Phase 2 |
| `shot_zone`, `defender_distance`, `assisted` | context for location-specific accuracy | Phase 3 |
| `lineup_id`, `with_without_teammate_id` | lineup/role interactions, possession count | Phase 2/3 |
| `injury_status`, `minutes_limit`, `starter_status` | time-versioned availability | Required |
| `foul_stint_state`, `remaining_minutes` | period-specific live conditions | Live phase |

Keep `starter_status = projected | confirmed | unknown`. Do not confuse a published projected lineup with an official confirmed five; latest source timestamp and injury scenario determine which can be used.

**Fantasy outputs** must have explicit `scoring_rule_id` (points for PTS/REB/AST/STL/BLK/3PM/TO etc.), raw simulated components and derived distribution. Do not ingest third-party fantasy projections.

## 5. Availability, schedule, and live data

Availability: official player status, source timestamp, reason, projected/confirmed starters, minutes restrictions, lineup status, rotation fit, replacement probabilities if modeled. An **unknown** lineup probability is a model uncertainty, not an observed probability.

Schedule: local venue, tipoff, travel days/distance if reliably computable, days since last game, back-to-back, 3-in-4, rest inequality, altitude, time zones, home/away. Keep franchise and roster version IDs.

Live-only event contract: period, regulation/OT flag, game clock, score, current on-court players, event type, team/player, shot location & value, foul state, free throws, possession changes, substitutions, provider event sequence, source/event and ingest timestamps. Detect and reconcile duplicate, late and corrected events. Live snapshots never alter the immutable pregame inputs.

## 6. As-of data integrity and quality

Every daily NBA forecast must carry:
1. Game ID, contract scope and tipoff.
2. Source freshness and data-as-of timestamp *before* freeze, including injury lineups.
3. Feature coverage per category (complete / partial / missing), last available timestamp, record count and denominators.
4. Season and historical sample sizes plus rotation/roster drift evidence.
5. Provenance, license class, source corrections and deterministic feature hash.
6. Explicit scenario ID and assumptions for questionable players, restricted minutes and unconfirmed starters.
7. Data Quality grade and machine-readable reasons; quality rules set via validation, **not declared achieved here**.

**Proposed hard failure classes:** missing game/team identity, missing historical efficiency or pace *without viable documented fallback*, unlicensed input, contradictory lineup/roster, stale critical availability, impossible possession/stat values, prediction timestamp after market use or missing immutable freeze. These produce no PASS.

Optional tracking gaps can use a validated fall-back model with wider uncertainty and a clearly indicated lower-quality grade. Never fabricate unknown stats or pretend absence of coverage is complete.

## 7. Snapshot, feature store and audit storage

Recommended entities (logical, implementation-agnostic):

- `source_register`, `source_observation`, `canonical_games`, `roster_memberships`, `player_availability_events`
- `team_game_fact`, `player_game_fact`, `play_by_play_event`, `lineup_stint`, `shot_event`, `schedule_fact`
- `feature_snapshot` (as-of timestamp, hash, version, completeness), `model_run` (seed, code and parameter versions)
- `prediction` (independent fair distribution and per-contract fair probabilities, frozen_at, scenario)
- `market_snapshot` (isolated after freeze, provider, terms, odds and observed_at)
- `gate_evaluation`, `closing_snapshot`, `settlement`, `scoring_metrics`

Maintain append-only historical versions. Revisions link with `supersedes_prediction_id`; original freeze/outcomes remain auditable. Make ingestion idempotent by canonical ID + source update/version.

## 8. Data-source evaluation checklist

Before committing an adapter, record factual availability for NBA history, 2026-27 roster/injury refresh, starters, advanced shooting, play-by-play, live substitutions, tracking, rate limits, data license, pricing, redistribution, audit-storage and derived-prediction rights. Separate “available for display/manual research” from “permitted for commercial automated production.”

Potential vendors to evaluate, not yet selected or authorized: official NBA data licensing, Sportradar, SportsDataIO, and other licensed distributors. PBP-derived analysis can inform methodology but should not be copied as unlicensed proprietary results.

See [Model Requirements](NBA_MODEL_REQUIREMENTS.md) and [Shadow Audit SOP](SHADOW_AUDIT_SOP.md).
