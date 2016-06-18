from dfs_scorer import DraftKingsScorer

for w in range(1, 5):
  scores = DraftKingsScorer().score(year=2015, week=w)
  sorted_scores = sorted(scores, key=scores.get, reverse=True)
  print('Week {0:d}\n-----'.format(w))
  for s in sorted_scores[1:10]:
    print('{0:s}: {1:f}'.format(s, scores[s]))
  print('\n')
