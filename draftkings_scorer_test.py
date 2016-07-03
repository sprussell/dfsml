import nflgame
from dfs_scorer import DraftKingsScorer
from team_defense import TeamDefense

# Print top 10 scorers for weeks 1-3 of 2015
for w in range(1, 4):
  scores = DraftKingsScorer().get_scores(year=2015, week=w)
  sorted_scores = sorted(scores, key=scores.get, reverse=True)
  print('Week {0:d}\n-----'.format(w))
  for s in sorted_scores[1:10]:
    print('{0:s}: {1:f}'.format(s, scores[s]))
  print('\n')

# Print Broncos team defense stats for week 1 of 2015
games = nflgame.games(year=2015, week=1)
players = nflgame.combine_play_stats(games)
den_defense = TeamDefense()
den_defense.get_team_stats(players, t='DEN')
print 'DEN sacks: {0:f}'.format(den_defense.defense_sk)
print 'DEN interceptions: {0:f}'.format(den_defense.defense_int)

# Print all team abbreviations
for t in nflgame.teams:
  print t[0] + ', ',
print '\n'

games = nflgame.games(2015)
players = nflgame.combine_play_stats(games)
# Print all plays that resulted in a defensive touchdown
print 'Defensive touchdown plays\n-----'
for g in games:
  # for p in g.drives.plays().players().touchdowns().defense():
  for p in g.drives.plays().filter(defense_tds__ge=1):
    print '{0:s} at {1:s}: {2:s}'.format(g.away, g.home, p)
print '\n'
# Compute total interceptions in the league
total_int = 0
for p in players.defense().sort('defense_int'):
  total_int += p.defense_int
print 'Total interceptions: {0:d}\n'.format(total_int)
# Print top 5 defensive touchdown earners
for p in players.defense().sort('defense_tds').limit(5):
  print '%s: %s' % (p.name, p.formatted_stats())

# Write out all player stats for each week as a csv
year = 2014
for week in range(1, 18):
  nflgame.combine_play_stats(
      nflgame.games(year, week)).csv('./stats/player_stats_wk%02d.csv' % week)
