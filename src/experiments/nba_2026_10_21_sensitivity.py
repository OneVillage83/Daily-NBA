"""Supplemental rating-sensitivity and conditional injury scenarios.
Does NOT modify frozen 2026-10-21 v0.2.1 original simulation files.
Mechanistic sensitivity assumptions, not empirical predictions or odds.
"""
import importlib.util, json, hashlib, csv
from pathlib import Path
M=Path('/mnt/data/nba_2026-10-21_shadow_v02_model.py')
spec=importlib.util.spec_from_file_location('shadow20261021',M)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.SAMPLES=14000 # supplemental only, base used 60k/game
frozen=Path('/mnt/data/nba_2026-10-21_shadow_v02_results.json')
base=json.loads(frozen.read_text())
assert len(base['games'])==11
out={'base_frozen_sha256':hashlib.sha256(frozen.read_bytes()).hexdigest(),
  'supplement':'EXPERIMENTAL nonfitted +/-4 offense per100 both teams, independently priced sensitivity (no odds); assumptions only',
  'supplement_drawwise_seed':20261021,'supplement_draws_each':m.SAMPLES,'games':[],'conditional':[]}
for i,g in enumerate(base['games']):
 a,h=g['away'],g['home']; tip=g['tipoff_utc']
 olda=m.T[a]['adjusted_off'];oldh=m.T[h]['adjusted_off']
 # The directional range from uncertain 2026 roster calibration, not a confidence interval.
 try:
  m.T[a]['adjusted_off']=olda+4.0;m.T[h]['adjusted_off']=oldh-4.0
  home_low=m.simulate(a,h,tip,20261021+200+i,full_players=False)
  m.T[a]['adjusted_off']=olda-4.0;m.T[h]['adjusted_off']=oldh+4.0
  home_high=m.simulate(a,h,tip,20261021+200+i,full_players=False)
 finally:
  m.T[a]['adjusted_off']=olda;m.T[h]['adjusted_off']=oldh
 out['games'].append({'game':a+'@'+h,'base_p_home':g['p_home_win'],
                      'home_p_low':home_low['p_home_win'],'home_p_high':home_high['p_home_win'],
                      'method':'Home roster offense +/-4 and away roster offense -/+4 points per 100 from baseline'})
 print('SENSITIVITY',a,h,round(home_low['p_home_win'],3),round(home_high['p_home_win'],3),flush=True)
# conditional starter availability, explicitly *not inferred* from WOWY
for a,h,index,team,name,offpenalty,defpenalty,mins in [
 ('PHX','POR',8,'POR','Deni Avdija',-4.5,+1.0,0),
 ('SAC','LAC',10,'SAC','Malik Monk',-1.5,+0.5,0)]:
 tip=m.GAMES[index][2];oldoff=m.T[team]['adjusted_off'];olddef=m.T[team]['adjusted_def']
 try:
  m.T[team]['adjusted_off']=oldoff+offpenalty
  m.T[team]['adjusted_def']=olddef+defpenalty
  s=m.simulate(a,h,tip,20261021+6000+index,scenario={'team':team,'player':name,'minutes':mins},full_players=False)
 finally:
  m.T[team]['adjusted_off']=oldoff;m.T[team]['adjusted_def']=olddef
 out['conditional'].append({'game':a+'@'+h,'player':name,'assumed_minutes':mins,
  'offense_rating_delta':offpenalty,'defense_rating_delta':defpenalty,
  'model_conditional_home_win':s['p_home_win'],'model_conditional_total':s['expected_full_total'],
  'assumption_warning':'NOT verified injury substitution response; no lineup WOWY; zero appearance probability assumed only within conditional scenario'})
 print('CONDITIONAL',name,s['p_home_win'],s['expected_full_total'],flush=True)
fp=Path('/mnt/data/nba_2026-10-21_shadow_v02_sensitivity.json');fp.write_text(json.dumps(out,indent=2))
assert hashlib.sha256(frozen.read_bytes()).hexdigest()==out['base_frozen_sha256']
print('FROZEN preserved',out['base_frozen_sha256'])