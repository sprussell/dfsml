import math
import numpy as np
import pandas as pd
import string
from IPython import display

pd.options.display.float_format = '{:.1f}'.format

# Dictionary of nflgame:dk team aliases
aliases = {
    # same
    'ari': 'ari',
    'atl': 'atl',
    'bal': 'bal',
    'buf': 'buf',
    'car': 'car',
    'chi': 'chi',
    'cin': 'cin',
    'cle': 'cle',
    'dal': 'dal',
    'den': 'den',
    'det': 'det',
    'hou': 'hou',
    'ind': 'ind',
    'jac': 'jac',
    'mia': 'mia',
    'min': 'min',
    'nyg': 'nyg',
    'nyj': 'nyj',
    'oak': 'oak',
    'phi': 'phi',
    'pit': 'pit',
    'sea': 'sea',
    'stl': 'stl',
    'ten': 'ten',
    'was': 'was',
    # different: nflgame to dk
    'gb': 'gnb',
    'kc': 'kan',
    'ne': 'nwe',
    'no': 'nor',
    'sd': 'sdg',
    'sf': 'sfo',
    'tb': 'tam',
    # different: dk to nflgame
    'gnb': 'gb',
    'kan': 'kc',
    'nwe': 'ne',
    'nor': 'no',
    'sdg': 'sd',
    'sfo': 'sf',
    'tam': 'tb'
}

for week in range(1, 18):
  dk = pd.read_csv('./dk-salaries/dk-salaries-2014-wk%02d.csv' % week,
                   sep=';')
  stats = pd.read_csv('./stats/player_stats_wk%02d.csv' % week)
  # Print some info on the data
  # pd.set_option('display.max_rows', len(stats.name))
  # print(zip(dk.Name, dk.Team))
  # pd.reset_option('display.max_rows')
  no_match = 0
  no_match_pos = {}
  id_index = []
  salaries = []
  opponents = []
  dk_points = []
  for i, n, t, p in zip(stats.index.values.tolist(),
                        stats['name'],
                        stats['team'],
                        stats['pos']):
    id_index.append(i)
    # Split the player name on the period
    if '.' in n:
      firstname = string.split(n, '.')[0].strip()
      lastname = string.split(n, '.')[1].strip()
      matches = (dk[dk.Name.str.contains(lastname) &
                    (dk.Name.str.split(', ').str.get(1).str.contains(firstname)) &
                    (dk.Team.str.contains(aliases[string.lower(t)]))])
    else:
      matches = (dk[(dk.Name.str.contains(n)) &
                    (dk.Team.str.contains(string.lower(t)))])

    # If no matches exist, increment counters
    if len(matches) == 0:
      no_match += 1
      if p in no_match_pos:
        no_match_pos[p] += 1
      else:
        no_match_pos[p] = 1
      salaries.append(np.nan)
      opponents.append('')
      dk_points.append(np.nan)
      continue
    # For multiple matches, try to use position to disambiguate
    elif len(matches) > 1:
      if isinstance(p, str):
        matches = matches[matches.Pos.str.contains(p)]
        if len(matches) > 1:
          print('Unable to find a unique match for ' + n)
          continue
      elif math.isnan(p):
        print('Unable to find a unique match for ' + n)
        continue
    # Add Draft Kings data to lists
    match = matches.squeeze()
    salaries.append(match.get_value('DK salary'))
    opponents.append(string.upper(aliases[match.get_value('Oppt')]))
    dk_points.append(match.get_value('DK points'))

  # Append Draft Kings data to nflgame stats dataframe
  stats['salary'] = pd.Series(salaries, index=id_index)
  stats['opponent'] = pd.Series(opponents, index=id_index)
  stats['dk_points'] = pd.Series(dk_points, index=id_index)

  display.display(stats.head())
  stats.to_csv('./combined/combined_stats_week%02d.csv' % week)
  print('Wrote combined stats for week %d' % week)


