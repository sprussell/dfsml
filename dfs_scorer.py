import nflgame


class DraftKingsScorer(object):
  """
  A class for computing a player's score based on the Draft Kings scoring rubric
  """
  def __init__(self):
    # Offensive categories
    self.passing_tds_pts = 4
    self.passing_yds_pts = 0.04
    self.passing_yds_300_bonus = 3
    self.passing_ints_pts = -1
    self.rushing_yds_pts = 0.1
    self.rushing_tds_pts = 6
    self.rushing_yds_100_bonus = 3
    self.receiving_yds_pts = 0.1
    self.receiving_rec_pts = 1
    self.receiving_tds_pts = 6
    self.receiving_yds_100_bonus = 3
    self.puntret_tds_pts = 6
    self.kickret_tds_pts = 6
    self.fumbles_lost_pts = -1
    self.passing_twoptm_pts = 2
    self.receiving_twoptm_pts = 2
    self.rushing_twoptm_pts = 2

    # Defensive categories
    self.defense_sk_pts = 1
    self.defense_int_pts = 2
    self.defense_frec_pts = 2
    self.kickret_tds_pts = 6
    self.puntret_tds_pts = 6
    self.defense_int_tds_pts = 6
    self.defense_frec_tds_pts = 6
    self.defense_misc_tds_pts = 6
    self.defense_safe_pts = 2
    self.blocked_kick_pts = 2

  def score(self, year, week=None):
    games = nflgame.games_gen(year, week)
    players = nflgame.combine_play_stats(games)
    output = {}
    for p in players:
      score = 0
      score += p.passing_tds * self.passing_tds_pts
      score += p.passing_yds * self.passing_yds_pts
      score += self.passing_yds_300_bonus if p.passing_yds >= 300 else 0
      score += p.passing_ints * self.passing_ints_pts
      score += p.rushing_yds * self.rushing_yds_pts
      score += p.rushing_tds * self.rushing_tds_pts
      score += self.rushing_yds_100_bonus if p.rushing_yds >= 100 else 0
      score += p.receiving_yds * self.receiving_yds_pts
      score += p.receiving_rec * self.receiving_rec_pts
      score += p.receiving_tds * self.receiving_tds_pts
      score += self.receiving_yds_100_bonus if p.receiving_yds >= 100 else 0
      score += p.puntret_tds * self.puntret_tds_pts
      score += p.kickret_tds * self.kickret_tds_pts
      score += p.fumbles_lost * self.fumbles_lost_pts
      score += p.passing_twoptm * self.passing_twoptm_pts
      score += p.rushing_twoptm * self.rushing_twoptm_pts
      score += p.receiving_twoptm * self.receiving_twoptm_pts
      output[p.name] = score

    return output
