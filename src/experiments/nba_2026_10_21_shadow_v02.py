"""Independent TDL NBA 2026-10-21 slate-wide shadow v0.2.1.

Research adaptation of the frozen 2026-10-20 nba-opening-possession v0.2 engine.
It executes historical team-efficiency and inferred shooting/player-minute
opportunity distributions WITHOUT odds, external forecasts or actual outcomes.
Everything not a directly observed statistic is tagged as an assumption/imputation.
NOT TRAINED, NOT CALIBRATED, research-only, no PASS. Not for wagering automation.
"""
from __future__ import annotations
import json, csv, hashlib, math
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.special import expit,logit
from scipy.optimize import brentq

ROOT=Path('/mnt/data')
SEED=20261021
SAMPLES=60000
VERSION='nba-20261021-v0.2.1-full-slate-shadow-uncalibrated'
LEAGUE_RTG=115.7
HOME_ADV=2.4
LEAGUE_ZONE_REF=np.array([.69,.44,.43,.40])
DEF_ZONES={}  # no matchup-specific shot-zone opponent measurements confirmed for today's 22 teams
# Statistical source: 2025–26 final season, NBA team advanced data, reproduced by HoopsNightly.
# Fields [offrtg, defrtg, pace per 48, eFG percent, rebounding percent, TOV percent].
# TOV definition differs from basketball-reference four factors. Normalize explicitly
# using a disclosed approximate ratio to BRef-like turnover-per-possession prior.
HIST={
 'MIL':(112.2,118.3,98.3,56.5,48.2,15.4),
 'WAS':(109.7,121.5,102.5,53.5,47.1,15.2),
 'ATL':(115.0,112.9,102.5,55.4,49.5,13.8),
 'ORL':(114.2,113.6,100.6,53.1,50.5,14.0),
 'CHA':(118.4,113.5,97.6,55.2,53.9,15.7),
 'BKN':(108.2,118.2,97.6,52.0,47.8,16.1),
 'CHI':(112.1,117.4,103.2,54.7,49.6,14.8),
 'TOR':(115.0,112.1,99.2,54.6,49.6,13.7),
 'MIN':(115.6,112.5,101.5,55.9,49.9,14.5),
 'MIA':(115.8,113.6,104.2,54.2,49.9,13.1),
 'IND':(110.1,117.9,101.8,53.3,47.5,14.2),
 'NOP':(113.3,117.6,101.4,52.7,49.1,13.9),
 'UTA':(112.7,120.8,103.5,53.6,49.2,14.9),
 'MEM':(112.4,118.4,101.7,53.3,47.8,14.8),
 'DAL':(110.3,115.5,102.6,52.7,49.2,14.1),
 'HOU':(117.5,112.1,97.0,54.2,54.5,15.7),
 'PHX':(114.2,112.9,98.1,53.7,49.8,14.7),
 'POR':(113.1,113.5,101.6,53.4,51.7,16.9),
 'GSW':(113.8,114.4,100.0,54.9,49.0,15.6),
 'LAL':(117.0,115.5,99.2,57.3,49.9,14.6),
 'SAC':(110.6,120.3,100.1,52.5,48.7,14.3),
 'LAC':(116.3,115.2,97.3,55.9,49.0,14.7),
}
# Manual, nonfitted OFF/DEF roster and availability adjustments, points/100
# over prior-season TEAM baselines, NOT observed 2026–27 performance or causally
# estimated WOWY. Each should be sensitivity-stressed by at least +/- 4 pts/100.
ADJUST={ # offense delta, defense delta (positive on defense => worse DRtg), rationale
 'MIL':(-3.0, +1.0,'Giannis departure; Herro acquisition'),
 'WAS':(+7.0, -2.0,'Trae Young and Anthony Davis additions; AJ Dybantsa OUT'),
 'ATL':(+0.0, +0.0,'Active established core; unvalidated roster shifts'),
 'ORL':(+0.5, +0.5,'Black and Isaac OUT; Bane/Paolo core'),
 'CHA':(-3.0, +1.0,'LaMelo departure; Knueppel and Coby White OUT'),
 'BKN':(+3.5, +1.0,'Randle and Porter Jr additions, Claxton departed'),
 'CHI':(+1.5, +2.0,'Norman Powell acquisition; Nic Claxton OUT'),
 'TOR':(+3.5, -1.5,'Kawhi Leonard acquisition'),
 'MIN':(+1.0, +0.5,'LaMelo Ball addition; DiVincenzo OUT'),
 'MIA':(+5.5, -1.5,'Giannis Antetokounmpo acquisition'),
 'IND':(+3.0, -1.0,'Haliburton return; Nesmith/McConnell OUT'),
 'NOP':(+1.0, +0.0,'Assumed healthier core; projected starters unconfirmed'),
 'UTA':(+2.5, -1.0,'Jaren Jackson Jr acquisition; Nurkic OUT'),
 'MEM':(-1.5, +1.0,'Jackson departure, Edey return, rookie Cam Boozer'),
 'DAL':(+2.5, +0.5,'Kyrie return, Lively OUT'),
 'HOU':(+1.0, +0.0,'VanVleet return, Adams QUESTIONABLE'),
 'PHX':(+0.0, +0.5,'Williams OUT, active Booker/Green/Brooks'),
 'POR':(+2.0, +0.5,'Morant/Lillard availability, Sharpe OUT, Avdija QUESTIONABLE'),
 'GSW':(-4.5, +2.0,'Butler, Moody, Podziemski, Porzingis OUT; Curry probable'),
 'LAL':(-0.5, -0.5,'LeBron gone, Walker Kessler acquisition'),
 'SAC':(+0.0, +0.0,'Core Sabonis/LaVine, rookie guard and Monk QUESTIONABLE'),
 'LAC':(-5.0, +2.0,'Kawhi departed; Ingram, Beal and multiple reserves OUT'),
}
# League priors for uncollected factors from 2025-26 Basketball-Reference league table.
# No fabricated team-specific historical OREB%, 3PA rate, free throw creation, opponent
# eFG/forced TOV/opp FT/FGA. They are proxies with wider epistemic uncertainty.
T={}
for code,(off,def_,pace,efg,reb,tov) in HIST.items():
 ao,ad,_=ADJUST[code]
 tp=tov/100*.87
 T[code]={'off':off,'def_':def_,'adjusted_off':off+ao,'adjusted_def':def_+ad,
          'pace':pace,'efg':efg/100,'tov':tp,
          'oreb':float(np.clip(.260+(reb-50)*.004,.18,.34)),
          'dreb':float(np.clip(.740+(reb-50)*.004,.66,.83)),
          'ftr':.264,'par3':.415,'opp_efg':.546,
          'forced_tov':.127,'opp_ftm_fga':.206,
          'ast_share':.637,'historical_reb_pct':reb/100,'historical_tov_pct_raw':tov/100,
          'roster_off_delta':ao,'roster_def_delta':ad}
# Historical 2025-26 factual player points/rebounds/assists, minutes, game counts.
# All notes below label rookies and missing 2025-26 cases as prior/proxy, not facts.
# each row = Name, last season PPG, RPG, APG, MPG, GP, role-class, proj_min, flag.
# 2024-25 veteran carry-forwards are labeled; rookies get population priors.
R={
'MIL':[
 ('Ryan Rollins',17.3,4.0,5.0,32.1,70,'guard',33,'historic other stats imputed'),
 ('Tyler Herro',20.5,4.8,4.1,31.3,33,'guard',33,'observed'),
 ('Jaime Jaquez Jr.',15.4,5.0,4.5,28.3,72,'wing',29,'reb/ast prior approximation'),
 ('Kyle Kuzma',13.0,4.5,2.7,26.2,69,'forward',29,'observed'),
 ('Myles Turner',11.9,5.5,1.6,26.9,70,'big',28,'reb/ast prior approximation'),
 ('AJ Green',10.4,2.8,1.7,29.1,70,'guard',26,'other stat priors')],
'WAS':[
 ('Trae Young',17.9,2.0,8.0,25.6,15,'guard',33,'2025-26 small sample'),
 ('Kyshawn George',14.8,5.6,4.0,29,70,'wing',30,'reb/ast prior approximation'),
 ('Bilal Coulibaly',11.7,4.3,2.6,26.2,56,'wing',29,'observed'),
 ('Anthony Davis',20.4,11.1,2.8,31.3,20,'big',32,'2025-26 small sample'),
 ('Alex Sarr',16.3,7.6,2.5,27.2,70,'big',31,'reb/ast prior approximation'),
 ('Bub Carrington',10.7,3.8,4.0,27.7,70,'guard',25,'reb/ast prior approximation')],
'ATL':[
 ('CJ McCollum',18.7,3.4,4.1,29.8,70,'guard',31,'reb/ast prior approximation'),
 ('Nickeil Alexander-Walker',20.8,3.4,3.4,33.4,75,'guard',34,'reb/ast prior approximation'),
 ('Dyson Daniels',11.9,6.2,4.4,33.2,77,'wing',34,'reb/ast prior approximation'),
 ('Jalen Johnson',22.5,10.3,7.9,35.2,72,'forward',35,'observed'),
 ('Onyeka Okongwu',15.2,7.8,3.0,31,72,'big',31,'reb/ast prior approximation')],
'ORL':[
 ('Jalen Suggs',13.8,3.9,5.5,27.6,57,'guard',30,'observed'),
 ('Desmond Bane',20.1,4.4,4.0,33.6,70,'guard',35,'reb/ast prior approximation'),
 ('Franz Wagner',20.6,5.7,3.6,30.0,63,'wing',33,'reb/ast prior approximation'),
 ('Paolo Banchero',22.2,8.4,5.2,34.7,72,'forward',35,'observed'),
 ('Wendell Carter Jr.',11.8,7.3,2.1,29.3,70,'big',29,'reb/ast prior approximation'),
 ('Nikola Vucevic',15.1,9.2,3.4,28.4,74,'big',27,'reb/ast prior approximation')],
'CHA':[
 ('Dennis Schroder',10.8,2.7,4.9,24.2,70,'guard',31,'observed'),
 ('Grayson Allen',16.5,3.4,4.2,28.8,70,'guard',33,'reb/ast prior approximation'),
 ('Brandon Miller',20.2,4.9,3.3,30.3,65,'wing',35,'observed'),
 ('Naz Reid',13.6,6.0,2.3,26.1,75,'forward',32,'reb/ast prior approximation'),
 ('Moussa Diabate',7.9,7.4,1.4,26,70,'big',29,'reb/ast prior approximation'),
 ("Royce O'Neale",9.8,4.0,2.2,28.4,70,'wing',24,'reb/ast prior approximation')],
'BKN':[
 ('Egor Demin',10.3,3.7,5.1,25.2,70,'guard',31,'reb/ast prior approximation'),
 ('Keon Ellis',6.7,1.9,1.0,20.5,72,'wing',27,'observed'),
 ('Michael Porter Jr.',24.2,7.1,3.0,32.5,52,'wing',34,'observed'),
 ('Julius Randle',21.1,6.7,5.0,33.0,79,'forward',35,'observed'),
 ("Day'Ron Sharpe",8.7,6.7,2.3,18.7,62,'big',28,'observed'),
 ('Noah Clowney',12.3,5.1,1.2,27,70,'forward',27,'reb/ast prior approximation')],
'CHI':[
 ('Josh Giddey',17.0,8.3,9.1,32.1,54,'guard',34,'observed'),
 ('Norman Powell',21.7,3.2,2.8,29.6,65,'guard',33,'reb/ast prior approximation'),
 ('Matas Buzelis',16.3,5.5,2.2,29.2,70,'forward',34,'reb/ast prior approximation'),
 ('Caleb Wilson',12.0,5.0,1.5,27.,1,'rookie',27,'ROOKIE PRIOR NOT OBSERVED'),
 ('Jalen Smith',10.2,6.7,1.2,20.7,53,'big',28,'observed'),
 ('Tre Jones',14.1,3.6,5.9,27,70,'guard',27,'reb/ast prior approximation')],
'TOR':[
 ('Immanuel Quickley',16.4,3.5,6.3,31.9,68,'guard',33,'reb/ast prior approximation'),
 ('RJ Barrett',19.3,5.2,3.6,30.3,70,'wing',31,'reb/ast prior approximation'),
 ('Kawhi Leonard',27.9,6.4,3.6,32.1,65,'wing',34,'observed'),
 ('Scottie Barnes',18.1,7.5,5.9,33.5,80,'forward',34,'observed'),
 ('Jakob Poeltl',10.7,8.5,2.6,25,70,'big',28,'reb/ast prior approximation')],
'MIN':[
 ('LaMelo Ball',20.1,5.1,7.4,28.0,60,'guard',34,'reb/ast prior approximation'),
 ('Anthony Edwards',28.8,5.1,3.8,35.0,68,'wing',36,'observed points/minutes'),
 ('Jonathan Kuminga',12.5,4.7,2.0,25.0,50,'forward',29,'proxy prior estimates'),
 ('Jaden McDaniels',14.8,4.9,2.4,31.7,74,'wing',32,'reb/ast prior approximation'),
 ('Rudy Gobert',10.9,11.2,1.8,31.3,72,'big',31,'reb/ast prior approximation'),
 ('Ayo Dosunmu',14.8,3.4,4.5,27.3,70,'guard',26,'reb/ast prior approximation')],
'MIA':[
 ('Davion Mitchell',9.3,2.4,5.2,28.6,65,'guard',29,'reb/ast prior approximation'),
 ('Klay Thompson',11.9,2.5,1.5,27.1,67,'guard',28,'proxy historical role'),
 ('Andrew Wiggins',15.4,4.9,2.7,30.3,70,'wing',31,'reb/ast prior approximation'),
 ('Giannis Antetokounmpo',27.6,9.8,5.4,28.9,36,'forward',33,'observed'),
 ('Bam Adebayo',20.1,10.0,3.2,32.4,73,'big',34,'observed'),
 ('Tim Hardaway Jr.',13.5,2.7,1.6,26.6,70,'wing',25,'reb/ast prior approximation')],
'IND':[
 ('Tyrese Haliburton',18.6,3.5,9.2,33.6,73,'guard',34,'2024-25 historical prior NOT 2025-26'),
 ('Andrew Nembhard',16.9,3.1,6.7,31.3,66,'guard',33,'reb/ast prior approximation'),
 ('Kelly Oubre Jr.',14.1,4.8,1.7,31.5,70,'wing',32,'reb/ast prior approximation'),
 ('Pascal Siakam',24.0,6.6,3.8,33.2,62,'forward',34,'observed'),
 ('Ivica Zubac',14.1,11.0,2.2,30.1,75,'big',32,'reb/ast prior approximation'),
 ('Jarace Walker',11.6,4.5,2.2,25.7,70,'forward',24,'reb/ast prior approximation')],
'NOP':[
 ('Dejounte Murray',16.0,5.3,6.3,29,45,'guard',32,'old-season/proxy prior'),
 ('Trey Murphy III',21.5,5.7,3.8,35.5,66,'wing',35,'observed'),
 ('Herbert Jones',8.9,3.7,2.7,28.4,70,'wing',30,'reb/ast prior approximation'),
 ('Zion Williamson',21.0,5.7,3.2,29.7,62,'forward',32,'observed'),
 ('Yves Missi',10.0,8.0,1.5,26,69,'big',28,'proxy prior'),
 ('Saddiq Bey',17.7,5.7,2.0,31.2,72,'forward',28,'reb/ast prior approximation')],
'UTA':[
 ('Keyonte George',23.6,3.7,6.1,33.1,54,'guard',34,'observed'),
 ('Darryn Peterson',16.0,4.0,3.5,30,1,'rookie',31,'ROOKIE PRIOR NOT OBSERVED'),
 ('Lauri Markkanen',26.7,6.9,2.1,34.3,42,'forward',34,'observed'),
 ('Jaren Jackson Jr.',19.4,5.7,2.0,30.3,48,'forward',33,'observed'),
 ('Jaxson Hayes',6.8,4.5,0.8,17,67,'big',28,'proxy prior'),
 ('Ace Bailey',13.8,4.3,1.4,27.6,74,'wing',25,'reb/ast prior approximation')],
'MEM':[
 ('Ty Jerome',19.7,2.8,5.7,22.6,15,'guard',31,'observed small sample'),
 ('Cedric Coward',13.6,6.2,2.8,25.8,70,'wing',31,'reb/ast prior approximation'),
 ('Jaylen Wells',12.5,3.2,1.9,26.4,70,'wing',29,'reb/ast prior approximation'),
 ('Cam Boozer',14.0,7.0,2.5,29,1,'rookie',30,'ROOKIE PRIOR NOT OBSERVED'),
 ('Zach Edey',13.6,11.1,1.1,25.8,11,'big',31,'observed small sample'),
 ('Jerami Grant',18.6,3.7,2.1,29.7,72,'forward',29,'reb/ast prior approximation')],
'DAL':[
 ('Kyrie Irving',24.7,4.8,4.6,36,50,'guard',33,'2024-25 historical prior NOT 2025-26'),
 ('Zaccharie Risacher',9.6,3.2,1.2,22.4,68,'wing',29,'reb/ast prior approximation'),
 ('Cooper Flagg',21.0,6.7,4.5,33.5,70,'forward',35,'observed'),
 ('P.J. Washington',14.2,7.9,2.3,31,65,'forward',33,'reb/ast prior approximation'),
 ('Daniel Gafford',12.0,6.4,1.2,22.0,65,'big',29,'proxy prior'),
 ('Naji Marshall',15.2,4.6,3.1,29.5,70,'wing',27,'reb/ast prior approximation')],
'HOU':[
 ('Fred VanVleet',14.1,3.7,5.6,35.2,60,'guard',33,'2024-25 historical prior NOT 2025-26'),
 ('Amen Thompson',18.3,7.6,5.6,37.4,75,'wing',35,'reb/ast prior approximation'),
 ('Kevin Durant',26.0,5.5,4.8,36.4,78,'forward',35,'observed'),
 ('Jabari Smith Jr.',15.8,7.0,1.7,35.1,70,'forward',33,'reb/ast prior approximation'),
 ('Alperen Sengun',20.4,8.9,6.2,33.3,72,'big',34,'observed'),
 ('Marcus Smart',9.3,2.8,2.8,28.5,70,'guard',24,'reb/ast prior approximation')],
'PHX':[
 ('Devin Booker',26.1,3.9,6.0,33.5,64,'guard',35,'observed'),
 ('Jalen Green',17.8,3.7,2.9,25.9,65,'guard',31,'reb/ast prior approximation'),
 ('Dillon Brooks',20.2,3.7,1.8,30.4,70,'wing',32,'reb/ast prior approximation'),
 ('Miles Bridges',17.1,6.3,3.4,31,70,'forward',32,'reb/ast prior approximation'),
 ('Oso Ighodaro',6.8,5.0,2.0,22.3,70,'big',29,'proxy prior'),
 ('Collin Gillespie',12.7,2.8,4.0,28.5,70,'guard',26,'reb/ast prior approximation')],
'POR':[
 ('Damian Lillard',24.9,4.7,7.1,36.1,58,'guard',33,'2024-25 historical prior NOT 2025-26'),
 ('Ja Morant',19.5,3.3,8.1,28.4,20,'guard',33,'2025-26 small sample'),
 ('Toumani Camara',13.4,5.4,2.5,33.3,70,'wing',32,'reb/ast prior approximation'),
 ('Deni Avdija',24.2,6.9,6.7,33.3,66,'forward',34,'QUESTIONABLE assumption: plays'),
 ('Donovan Clingan',12.1,10.8,1.8,27.2,75,'big',30,'reb/ast prior approximation'),
 ('Jrue Holiday',16.3,4.5,5.1,29.4,70,'guard',26,'reb/ast prior approximation')],
'GSW':[
 ('Stephen Curry',26.6,3.6,4.7,30.9,43,'guard',34,'PROBABLE; observed'),
 ("De'Anthony Melton",12.3,3.2,2.8,23,64,'guard',31,'reb/ast prior approximation'),
 ('Yaxel Lendeborg',12.0,5.0,2.0,27,1,'rookie',29,'ROOKIE PRIOR NOT OBSERVED'),
 ('Gui Santos',7.0,3.4,2.1,22,70,'forward',30,'proxy prior'),
 ('Draymond Green',8.4,5.5,5.8,27.5,65,'forward',32,'reb/ast prior approximation'),
 ('Al Horford',8.3,5.1,2.0,21.5,58,'big',27,'reb/ast prior approximation')],
'LAL':[
 ('Luka Doncic',33.5,7.7,8.3,35.8,64,'guard',36,'observed'),
 ('Austin Reaves',23.3,4.7,5.5,34.5,51,'guard',35,'observed'),
 ('Quentin Grimes',13.4,4.1,2.8,29.4,70,'wing',30,'reb/ast prior approximation'),
 ('Jake LaRavia',8.2,3.8,2.1,25.1,65,'forward',29,'reb/ast prior approximation'),
 ('Walker Kessler',11.1,10.4,1.4,29,65,'big',31,'proxy historical role'),
 ('Ziaire Williams',10.2,4.2,1.5,22.9,68,'wing',24,'reb/ast prior approximation')],
'SAC':[
 ('Darius Acuff Jr.',15.0,3.0,4.5,29,1,'rookie',31,'ROOKIE PRIOR NOT OBSERVED'),
 ('Zach LaVine',19.2,2.8,2.3,31.4,39,'guard',33,'observed'),
 ("De'Andre Hunter",15.0,4.1,1.5,28,65,'wing',30,'proxy prior'),
 ('Keegan Murray',15.0,6.8,2.1,32,65,'forward',34,'proxy prior'),
 ('Domantas Sabonis',15.8,11.4,4.1,29.7,19,'big',34,'2025-26 small sample'),
 ('Malik Monk',12.3,2.4,3.8,23.5,55,'guard',22,'QUESTIONABLE assumption: plays')],
'LAC':[
 ('Darius Garland',18.8,2.4,6.7,29.9,45,'guard',34,'observed'),
 ('Keaton Wagler',12.0,3.3,2.7,28,1,'rookie',31,'ROOKIE PRIOR NOT OBSERVED'),
 ('Rui Hachimura',12.0,4.3,1.1,27,69,'forward',33,'proxy prior'),
 ('Derrick Jones Jr.',11.0,3.8,1.2,26,70,'forward',31,'proxy prior'),
 ('Isaiah Jackson',8.5,5.5,1.3,20,60,'big',28,'proxy prior')]
}

P={}
for code,guys in R.items():
 P[code]=[]
 for name,points,reb,ast,mp,gp,role,proj_min,note in guys:
  three_share={'guard':.45,'wing':.45,'forward':.33,'big':.10,'rookie':.32}[role]
  if name in ['Giannis Antetokounmpo','Zion Williamson','Anthony Davis','Jalen Johnson']:
   three_share=.15
  if name=='Stephen Curry':three_share=.57
  if name=='Luka Doncic':three_share=.50
  if name=='Klay Thompson':three_share=.72
  fga=max(2.0,points/1.33)
  three=fga*three_share
  fta=max(.75,points*.18 if role not in ['big','forward'] else points*.235)
  p2=.54 if role in ['forward','big'] else .51
  p3=.36 if role not in ['big'] else .29
  pft=.79
  if name=='Giannis Antetokounmpo':p2=.64;p3=.333;pft=.65
  if name=='Stephen Curry':p2=.54;p3=.4;pft=.92
  if name in ['Zion Williamson','Rudy Gobert']:p2=.64;p3=.23;pft=.69
  if name in ['Devin Booker','Kevin Durant']:p2=.54;p3=.38;pft=.88
  row=dict(name=name,mp=mp,proj_min=proj_min,fga=fga,three_pa=three,fta=fta,
           p2=p2,p3=p3,pft=pft,reb=reb,ast=ast,role=1.0,gp=gp,
           stl=.88 if role in ['guard','wing'] else .7,
           blk=.75 if role=='big' else .30,
           turn=max(.55,ast*.38),pf=2.3,
           shot_zone_source='UNOBSERVED / league role mix IMUPTED, no 2025-26 player shot-zone record',
           defense_source='UNOBSERVED / role prior for steal, block, PF',
           data_status=note)
  if role=='rookie':row['gp']=1
  if name=='Giannis Antetokounmpo':row.update(stl=.9,blk=.7,turn=3.2)
  if name=='Stephen Curry':row.update(stl=1.0,blk=.3,turn=2.8)
  P[code].append(row)
 assert len(P[code])>=5
# Fresh official injury reports and contextual input are not market-derived.
GAMES=[
 ('MIL','WAS','2026-10-21T23:00:00Z'),
 ('ATL','ORL','2026-10-21T23:00:00Z'),
 ('CHA','BKN','2026-10-21T23:30:00Z'),
 ('CHI','TOR','2026-10-21T23:30:00Z'),
 ('MIN','MIA','2026-10-21T23:30:00Z'),
 ('IND','NOP','2026-10-22T00:00:00Z'),
 ('UTA','MEM','2026-10-22T00:00:00Z'),
 ('DAL','HOU','2026-10-22T00:30:00Z'),
 ('PHX','POR','2026-10-22T02:00:00Z'),
 ('GSW','LAL','2026-10-22T02:00:00Z'),
 ('SAC','LAC','2026-10-22T02:30:00Z')]
SOURCES={
 'team_stats_2025_26':'https://hoopsnightly.com/stats?sort=off',
 'league_2025_26_averages':'https://www.basketball-reference.com/leagues/NBA_stats_per_poss.html',
 'nba_injury_2026_10_21_1645_ET':'https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-21_04_45PM.pdf',
 'lineup_projection':'https://www.rotowire.com/basketball/nba-lineups.php',
 'player_profiles':'https://hoopsnightly.com/players/{player_slug}',
 'roster_notes':'rotowire and verified current roster pages'
}
DATA_FLAGS={
 'status':'EXPERIMENTAL shadow, not trained or calibrated. FAIL PASS quality gate.',
 'team_baselines':'2025-26 factual team OffRtg, DefRtg, pace, eFG, REB%, turnover%; latest roster adjusted HEURISTIC not measured',
 'four_factors':'eFG, TOV team observed under NBA provider-specific definitions; OREB%, FTr, 3PA, opponent eFG and turnover forcing are LEAGUE PRIORS/PROXIES, not team-specific observed metrics',
 'player_inputs':'2025-26 PTS/REB/AST, MP partly verified, others approximated and labeled; no verified shot-by-shot player statistics in full slate',
 'player_shooting':'FGA/3PA/FTA and efficiencies IMPUTED from role/PPG; individual 3PM and ALT props particularly unreliable',
 'injury':'official 4:45 ET statuses; projected groups NOT confirmed, optimistic questionable-player baseline; conditional alternate computed separately',
 'bench':'all unlisted bench grouped Other, separate group can total more than 43 minutes',
 'missing_advanced':'No verified historical five-man stint matrices, WOWY, exact rebound chances, true potential assists, tracking data or defensive schemes; do not claim included',
 'stat_reconciliation':'240 regulation player-minutes per team, exact player sum to regulation team points, sharing of rebound/assist/steal/turnover events (limited and simplified)',
 'overtime':'full-game win/totals use approximate overtime tie breaker; player outputs are regulation-only',
 'model_uncertainty':'model-draw quantiles understate structural/epistemic uncertainty; use +/-4 rating-shock sensitivity, not a calibration confidence interval',
 'market':'market odds, market forecasts, outside models, no-vig and fee EV not read by model. PASS/AVOID/WATCH only provisional research WATCH, no PASS.',
 'fantasy':'1xPTS+1.2xREB+1.5xAST+3xSTL+3xBLK-1xTOV experimental, not official scoring',
}
def alloc(trials,weights,rng):
 """Allocate exact nonnegative event counts to players, including bench group."""
 trials=np.maximum(0,np.asarray(trials,dtype=int));weights=np.maximum(0,weights)
 out=np.zeros_like(weights,dtype=np.int32);remain=trials.copy()
 denom=weights.sum(axis=1)
 for j in range(weights.shape[1]-1):
  q=np.divide(weights[:,j],denom,out=np.zeros(len(remain)),where=denom>0)
  out[:,j]=rng.binomial(remain,np.clip(q,0,1))
  remain-=out[:,j];denom-=weights[:,j]
 out[:,-1]=remain
 return out


def shooter_prior(p,zone=None):
 gp=p['gp'];three=p['three_pa'];two=p['fga']-three
 if zone is None:
  # Partial pooling by attempts and sample size for efficiency; skill uncertainty remains.
  return ((p['p2']*two*gp+70*.535)/(two*gp+70), (p['p3']*three*gp+65*.355)/(three*gp+65), (p['pft']*p['fta']*gp+45*.78)/(p['fta']*gp+45))
 return None


def minute_matrix(code,n,rng,scenario=None):
 people=P[code]; means=np.array([p['proj_min'] for p in people],float)
 if scenario and code==scenario.get('team'):
  name=scenario.get('player');target=scenario.get('minutes')
  for i,p in enumerate(people):
   if p['name']==name:means[i]=float(target)
 # Historical likely bench coverage; extra 'other' explicitly consumes remaining minutes.
 residual=max(10.,240.-means.sum())
 meanall=np.r_[means,residual]
 # As a guard, projected 'Other' minute capacity never pretends bench absent.
 shape=np.exp(rng.normal(np.log(meanall)[None,:],.075 if code in ['BOS','NYK','DET'] else .095,(n,len(meanall))))
 minutes=shape/shape.sum(axis=1,keepdims=True)*240.
 # Cap individual players at 43; OTHER is an aggregate of several bench players and may exceed 43.
 individual_excess=np.maximum(minutes[:,:-1]-43.,0.)
 minutes[:,:-1]=np.minimum(minutes[:,:-1],43.)
 minutes[:,-1]+=individual_excess.sum(axis=1)
 assert np.max(abs(minutes.sum(axis=1)-240))<1e-6
 assert np.max(minutes[:,:-1])<43.0001
 return minutes


def generate_team(code,opp,poss,rng,home,scenario=None):
 n=len(poss); people=P[code];k=len(people)
 mins=minute_matrix(code,n,rng,scenario)
 t=T[code];d=T[opp]
 # As-of 2025-26 baseline + opponent defense; no speculative/unverified on/off claims.
 offense=t['adjusted_off']*d['adjusted_def']/LEAGUE_RTG
 target=poss.mean()*offense/100+(HOME_ADV/2 if home else -HOME_ADV/2)
 # Shared game pace, opponent forced turnover and free-throw chance.
 # Possessions are regulation estimate, not claimed exact historical event replay.
 tov=np.clip(.5*(t['tov']+d['forced_tov']),.06,.20)
 num_tov=rng.binomial(poss.astype(int),tov)
 oreb=np.clip(.5*(t['oreb']+1-d['dreb']),.14,.40)
 ftr=np.clip(.5*(t['ftr']+d['opp_ftm_fga']/.78),.12,.40)
 FGA=np.maximum(1,np.rint((poss-num_tov)/(1+.44*ftr-.52*oreb)+rng.normal(0,2.0,n))).astype(int)
 three_share=np.clip(t['par3'],.15,.65)
 _3PA=rng.binomial(FGA,three_share)
 _2PA=FGA-_3PA
 FTA=rng.poisson(FGA*ftr*np.exp(rng.normal(-.002,.06,n)))
 
 # Allocate FGA/3PA/FTA exactly within same minutes and joint game possession draws.
 use=np.array([p['role'] for p in people])
 w2=np.column_stack([mins[:,i]/p['mp']*max(.01,p['fga']-p['three_pa'])*p['role'] for i,p in enumerate(people)]+[mins[:,-1]*.24])
 w3=np.column_stack([mins[:,i]/p['mp']*max(.001,p['three_pa'])*p['role'] for i,p in enumerate(people)]+[mins[:,-1]*.095])
 wf=np.column_stack([mins[:,i]/p['mp']*max(.001,p['fta'])*p['role'] for i,p in enumerate(people)]+[mins[:,-1]*.08])
 two=alloc(_2PA,w2,rng); three=alloc(_3PA,w3,rng);ft=alloc(FTA,wf,rng)
 
 p2=np.array([shooter_prior(p)[0] for p in people]+[.53]); p3=np.array([shooter_prior(p)[1] for p in people]+[.355]); pf=np.array([shooter_prior(p)[2] for p in people]+[.78])
 # Opponent defensive **overall eFG** adjustment observed; does not impersonate a zone-specific defense.
 opp_delta=float((.545-d['opp_efg'])*.52)
 logit2=logit(p2)+opp_delta*2.2
 # New actual zone-specific calculation available for nine named regular-season shooters.
 # Matchup defense zone effect uses BOS zones only; different opponent's zone defense is NOT known.
 if opp in DEF_ZONES:
  defender=(DEF_ZONES[opp]-LEAGUE_ZONE_REF)
 else:defender=np.zeros(4)
 zoneP={}
 for j,p in enumerate(people):
  if 'zones' not in p:continue
  base=np.array(p['zone_accuracy'],float)
  gp=p['gp'];total_two=(p['fga']-p['three_pa'])*gp
  zone_shots=np.array(p['zones'])/sum(p['zones'])*total_two
  shrink=(zone_shots*base+22*np.array([.69,.45,.43,.40]))/(zone_shots+22)
  zoneP[j]=expit(logit(np.clip(shrink,.01,.99))+opp_delta*2.2+0.55*defender)
 
 # Anchor level to opponent-adjusted TEAM production but leave 25% of shot-profile
 # difference (statistic-dependent) rather than force all shoot location effect away.
 avg3=float(np.mean(_3PA));avg2=float(np.mean(_2PA));avgFT=float(np.mean(FTA))
 mu3=float((w3.mean(axis=0)@p3)/(w3.mean(axis=0).sum()))
 muf=float((wf.mean(axis=0)@pf)/(wf.mean(axis=0).sum()))
 tgt2=np.clip((target-3*avg3*mu3-avgFT*muf)/(2*max(1,avg2)),.32,.73)
 now2=float((w2.mean(axis=0)@expit(logit2))/(w2.mean(axis=0).sum()))
 desired=.75*tgt2+.25*now2
 base2=np.clip(expit(logit2),.02,.98)
 try:shift=brentq(lambda sh: float((w2.mean(axis=0)@expit(logit(base2)+sh))/(w2.mean(axis=0).sum())-desired),-5,5)
 except ValueError:shift=0.
 # Shared game-scoring shocks plus per-player sampled minutes/volume induce
 # joint PTS / AST / REB / team total dependence.
 shock2=rng.normal(0,.075,n);shock3=rng.normal(0,.125,n)
 two_made=np.zeros((n,k+1),int)
 for j in range(k+1):
  if j in zoneP:
   p=people[j]
   frac=np.array(p['zones'])/sum(p['zones'])
   zones=alloc(two[:,j],np.broadcast_to(frac,(n,4)),rng)
   zone_probs=expit(logit(np.clip(zoneP[j],.01,.99))+shift+shock2[:,None])
   two_made[:,j]=rng.binomial(zones,zone_probs).sum(axis=1)
  else:
   two_made[:,j]=rng.binomial(two[:,j],expit(logit(base2[j])+shift+shock2))
 three_made=rng.binomial(three,expit(logit(np.clip(p3,.01,.99))[None,:]+shock3[:,None]))
 ft_made=rng.binomial(ft,pf[None,:])
 points=2*two_made+3*three_made+ft_made
 totalpoints=points.sum(axis=1)
 FGM=two_made.sum(axis=1)+three_made.sum(axis=1)
 ast_total=rng.binomial(FGM,t['ast_share'])
 # Actual potential assists not available, so distribute observed-made FGs by
 # prior assists and current shared simulated minutes; NOT tracking-derived.
 ast_weights=np.column_stack([mins[:,i]/p['mp']*p['ast'] for i,p in enumerate(people)]+[np.maximum(mins[:,-1]*.13,.05)])
 ast=alloc(ast_total,ast_weights,rng)
 return dict(code=code,points=points,team_pts=totalpoints,mins=mins,ast=ast,FGM=FGM,ownmiss=FGA-FGM,tov=num_tov,
             two_at=two,three_at=three,three_made=three_made,ft_at=ft,
             numtwo=two_made.sum(axis=1),numthree=three_made.sum(axis=1),
             fga=FGA,oreb=oreb,team_target=target,model_shoot2_mean=desired,team_four_factor=dict(
                 turnovers_pct=round(float(num_tov.mean()/poss.mean()),3),
                 three_attempt_rate=round(float(_3PA.sum()/FGA.sum()),3),
                 fta_per_fga=round(float(FTA.sum()/FGA.sum()),3)))


def gen_secondary(code,opp,selfg,other,rng):
 people=P[code];n=len(selfg['team_pts'])
 own_orb=rng.binomial(np.maximum(0,selfg['ownmiss']),selfg['oreb'])
 def_reb=rng.binomial(np.maximum(0,other['ownmiss']),np.clip(T[code]['dreb'],.5,.95))
 own_reb=own_orb+def_reb
 reb_w=np.column_stack([selfg['mins'][:,i]/p['mp']*p['reb'] for i,p in enumerate(people)]+[np.maximum(.16*selfg['mins'][:,-1],.5)])
 reb=alloc(own_reb,reb_w,rng)
 # A steal always implies an opponent turnover, not the reverse.
 team_steal=rng.binomial(other['tov'],.58)
 stl_w=np.column_stack([selfg['mins'][:,i]/p['mp']*p['stl'] for i,p in enumerate(people)]+[np.maximum(.04*selfg['mins'][:,-1],.05)])
 stl=alloc(team_steal,stl_w,rng)
 # Blocks arise on 2PA misses, ignoring exotic blocked 3PT attempts, 
 # with assumed 2PA block fraction (not fitted to historical play-by-play).
 # Tie expected team blocks to verified player BLK histories before distributing:
 # block attempt probability is a HEURISTIC fit to historical prior moments, not tracking.
 miss2=np.maximum(0,other['two_at'].sum(axis=1)-other['numtwo'])
 blk_exposure=sum(float(p['blk']*p['proj_min']/p['mp']) for p in people)+.35
 block_chance=np.clip(blk_exposure/max(1,float(np.mean(miss2))),.08,.38)
 block_opp=rng.binomial(miss2,block_chance)
 blk_w=np.column_stack([selfg['mins'][:,i]/p['mp']*p['blk'] for i,p in enumerate(people)]+[np.maximum(.03*selfg['mins'][:,-1],.05)])
 blk=alloc(block_opp,blk_w,rng)
 # Give player turnovers exactly matching team turnover total.
 tov_w=np.column_stack([selfg['mins'][:,i]/p['mp']*p['turn'] for i,p in enumerate(people)]+[np.maximum(.045*selfg['mins'][:,-1],.05)])
 personal_tov=alloc(selfg['tov'],tov_w,rng)
 # No observed situation-specific foul rates; approximate from per-minute season fouls, cap at 6.
 foul=np.column_stack([np.minimum(6,rng.poisson(selfg['mins'][:,i]/p['mp']*p['pf'])) for i,p in enumerate(people)]+[
  np.minimum(6,rng.poisson(selfg['mins'][:,-1]/27.*1.7))])
 # Research-only custom NBA fantasy scoring, not a published provider rule.
 fantasy=selfg['points']+1.2*reb+1.5*selfg['ast']+3*stl+3*blk-personal_tov
 assert np.array_equal(stl.sum(axis=1),team_steal)
 assert np.array_equal(personal_tov.sum(axis=1),selfg['tov'])
 assert np.array_equal(blk.sum(axis=1),block_opp)
 assert np.array_equal(reb.sum(axis=1),own_reb)
 return dict(reb=reb,stl=stl,blk=blk,tov=personal_tov,fouls=foul,fantasy=fantasy,
             team_reb=own_reb,team_stl=team_steal,team_blk=block_opp)


def fair(p):
 if p<=0 or p>=1:return None
 return round(-100*p/(1-p) if p>=.5 else 100*(1-p)/p)


def summ(x):
 return dict(mean=round(float(np.mean(x)),2),p10=float(np.quantile(x,.10)),p90=float(np.quantile(x,.9)))


def simulate(away,home,tip,seed,scenario=None,full_players=True):
 rng=np.random.default_rng(seed)
 a,h=T[away],T[home]
 pace_mean=(a['pace']+h['pace'])/2 - .08*abs(a['pace']-h['pace'])
 poss=np.clip(rng.normal(pace_mean,3.7,SAMPLES),80,118)
 gA=generate_team(away,home,poss,rng,False,scenario);gH=generate_team(home,away,poss,rng,True,scenario)
 sA=gen_secondary(away,home,gA,gH,rng);sH=gen_secondary(home,away,gH,gA,rng)
 regA=gA['team_pts'];regH=gH['team_pts']
 # Incomplete model: approximate overtime solely for full-game ML/totals.
 isOT=regA==regH
 pointsA=regA.copy();pointsH=regH.copy()
 for j in np.where(isOT)[0]:
  da,dh=int(rng.poisson(11.4)),int(rng.poisson(11.5))
  if da==dh:
   if rng.random()<.5:da+=1
   else:dh+=1
  pointsA[j]+=da;pointsH[j]+=dh
 assert np.all(pointsA!=pointsH)
 total=pointsA+pointsH; margin=pointsH-pointsA
 winhome=float(np.mean(margin>0))
 res=dict(away=away,home=home,tipoff_utc=tip,model_version=VERSION,
          scenario=scenario or {'kind':'baseline'},
          simulations=SAMPLES,pace_mean=round(pace_mean,2),p_home_win=winhome,p_away_win=1-winhome,
          fair_american_home=fair(winhome),fair_american_away=fair(1-winhome),
          regulation_pred_away=round(float(regA.mean()),2),regulation_pred_home=round(float(regH.mean()),2),
          fullgame_pts_away=round(float(pointsA.mean()),2),fullgame_pts_home=round(float(pointsH.mean()),2),
          expected_full_total=round(float(total.mean()),2),expected_home_margin=round(float(margin.mean()),2),
          total_80=[float(np.quantile(total,.1)),float(np.quantile(total,.9))],
          margin_80=[float(np.quantile(margin,.1)),float(np.quantile(margin,.9))],
          ottie_rate=round(float(isOT.mean()),4),
          fair_thresholds={f'home_cover_{v:+.1f}':round(float(np.mean(margin+v>0)),4) for v in [-5.5,-3.5,-1.5,1.5,3.5,5.5]}|
          {f'over_{v:.1f}':round(float(np.mean(total>v)),4) for v in [214.5,219.5,224.5,229.5,234.5,239.5]},
          team_details={away:{'points':summ(regA),'factors':gA['team_four_factor']},
                        home:{'points':summ(regH),'factors':gH['team_four_factor']}},
          diagnostic={away:{'minutes_abs_err_max':float(np.max(abs(gA['mins'].sum(axis=1)-240))),
                              'offense_points_gap':float(np.max(abs(gA['points'].sum(axis=1)-regA)))},
                      home:{'minutes_abs_err_max':float(np.max(abs(gH['mins'].sum(axis=1)-240))),
                              'offense_points_gap':float(np.max(abs(gH['points'].sum(axis=1)-regH)))}},
          player=[])
 if not full_players:return res
 for code,g,s in [(away,gA,sA),(home,gH,sH)]:
  for j,p in enumerate(P[code]):
   name=p['name'];pts=g['points'][:,j];rebs=s['reb'][:,j];asts=g['ast'][:,j];thr=g['three_made'][:,j]
   row=dict(team=code,name=name,minutes=round(float(g['mins'][:,j].mean()),1),
            pts=summ(pts),reb=summ(rebs),ast=summ(asts),three=summ(thr),
            stl=summ(s['stl'][:,j]),blk=summ(s['blk'][:,j]),turnovers=summ(s['tov'][:,j]),
            fouls=summ(s['fouls'][:,j]),fantasy=summ(s['fantasy'][:,j]),
            shot_zone_source=p['shot_zone_source'],defense_rate_source=p['defense_source'],
            p_pts_20=round(float(np.mean(pts>=20)),4),p_pts_25=round(float(np.mean(pts>=25)),4),
            p_pts_30=round(float(np.mean(pts>=30)),4),p_reb_10=round(float(np.mean(rebs>=10)),4),
            p_ast_8=round(float(np.mean(asts>=8)),4),p_3pm_3=round(float(np.mean(thr>=3)),4),
            p_pra_30=round(float(np.mean(pts+rebs+asts>=30)),4),
            p_pra_35=round(float(np.mean(pts+rebs+asts>=35)),4),
            p_double_double=round(float(np.mean(((pts>=10).astype(int)+(rebs>=10).astype(int)+(asts>=10).astype(int))>=2)),4))
   res['player'].append(row)
 return res



def run():
 now=datetime.now(timezone.utc).isoformat(timespec='seconds')
 out={
  'title':'The Daily Line NBA 2026-10-21 full 11-game shadow v0.2.1 experiment',
  'run_at_utc':now,'source_asof_utc':'2026-10-21T20:45:00Z',
  'forecast_frozen_at_utc':now,'first_tip_utc':'2026-10-21T23:00:00Z',
  'model_version':VERSION,'seed':SEED,'simulations_per_game':SAMPLES,
  'independent_without_market':True,'calibration':'none',
  'quality_gate':'WATCH-RESEARCH-ONLY; no PASS',
  'baseline_sources':SOURCES,'data_quality_notes':DATA_FLAGS,
  'team_baselines':HIST,'team_heuristic_adjustments':ADJUST,
  'projected_players':R,
  'games':[], 'conditional_scenarios':[],
 }
 for i,(away,home,tip) in enumerate(GAMES):
  x=simulate(away,home,tip,SEED+197*i)
  out['games'].append(x)
  print(f"{away}@{home}: {x['fullgame_pts_away']:.1f}-{x['fullgame_pts_home']:.1f} Home win {x['p_home_win']*100:.1f}% total {x['expected_full_total']:.1f} margin {x['expected_home_margin']:+.1f}",flush=True)
 # Player-availability scenario. No invented probability weights.
 out['conditional_scenarios'].append({'meaning':'Deni Avdija questionable: conditional MINUTES LIMIT, not proof of OUT and not weighted',
   'scenario':{'team':'POR','player':'Deni Avdija','minutes':0},
   'game':simulate('PHX','POR',GAMES[8][2],SEED+9001,scenario={'team':'POR','player':'Deni Avdija','minutes':0},full_players=False)})
 out['conditional_scenarios'].append({'meaning':'Malik Monk questionable: conditional MINUTES LIMIT, not weighted',
   'scenario':{'team':'SAC','player':'Malik Monk','minutes':0},
   'game':simulate('SAC','LAC',GAMES[10][2],SEED+9002,scenario={'team':'SAC','player':'Malik Monk','minutes':0},full_players=False)})
 # Due to model rebalance without changing role rates and includes 'Other', these
 # are sensitivity scaffolds, not evidence-based out/wowy forecasts.
 root=ROOT
 jf=root/'nba_2026-10-21_shadow_v02_results.json'
 jf.write_text(json.dumps(out,indent=2,ensure_ascii=False))
 games=[dict(away=x['away'],home=x['home'],tip_utc=x['tipoff_utc'],
        away_win=x['p_away_win'],home_win=x['p_home_win'],
        away_fair_american=x['fair_american_away'],home_fair_american=x['fair_american_home'],
        away_points=x['fullgame_pts_away'],home_points=x['fullgame_pts_home'],
        expected_total=x['expected_full_total'],expected_home_margin=x['expected_home_margin'],
        total_p10=x['total_80'][0],total_p90=x['total_80'][1],
        margin_p10=x['margin_80'][0],margin_p90=x['margin_80'][1],
        gate='WATCH-RESEARCH',data_quality='C/partial') for x in out['games']]
 pf=root/'nba_2026-10-21_shadow_v02_games.csv'
 with pf.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=games[0].keys());w.writeheader();w.writerows(games)
 pl=[]
 for x in out['games']:
  for y in x['player']:
   pl.append({'match':x['away']+'@'+x['home'],'team':y['team'],'name':y['name'],'minutes':y['minutes'],
      **{k: y[k]['mean'] for k in ('pts','reb','ast','three','stl','blk','turnovers','fouls','fantasy')},
      **{k: y[k] for k in ('p_pts_20','p_pts_25','p_pts_30','p_reb_10','p_ast_8','p_3pm_3','p_pra_30','p_pra_35','p_double_double')},
      'input_quality':next(t[7] for t in R[y['team']] if t[0]==y['name'])})
 pp=root/'nba_2026-10-21_shadow_v02_players.csv'
 with pp.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=pl[0].keys());w.writeheader();w.writerows(pl)
 summary=dict(frozen_at_utc=now,model_version=VERSION,seed=SEED,total_games=len(games),players=len(pl),
  input_cut_utc=out['source_asof_utc'],scoreboard_count=11,
  tests={'all_games':len(games)==11,'win_probs_sum_one':all(abs(x['p_home_win']+x['p_away_win']-1)<1e-12 for x in out['games']),
  'player_minute_gap_max':max(v['minutes_abs_err_max'] for g in out['games'] for v in g['diagnostic'].values()),
  'player_team_scoring_gap_max':max(v['offense_points_gap'] for g in out['games'] for v in g['diagnostic'].values())},
  sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (jf,pf,pp)})
 (root/'nba_2026-10-21_shadow_v02_checksums.json').write_text(json.dumps(summary,indent=2))
 print('WROTE',json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':run()