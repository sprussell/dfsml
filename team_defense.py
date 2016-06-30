import nflgame

class TeamDefense(object):
  """
  A class for computing defensive stats for a full team
  """
  def __init__(self):
    self.defense_sk = 0
    self.defense_int = 0
    self.defense_frec = 0
    self.kickret_tds = 0
    self.puntret_tds = 0
    self.defense_int_tds = 0
    self.defense_frec_tds = 0
    self.defense_misc_tds = 0
    self.defense_safe = 0
    self.blocked_kicks = 0  # sum defense_puntblk, defense_xpblk, defense_fgblk

  def get_team_stats(self, players, t):
    self.__init__()
    for p in players.defense().filter(team=t):
      self.defense_sk += p.defense_sk
      self.defense_int += p.defense_int
      self.defense_frec += p.defense_frec
      self.kickret_tds += p.kickret_tds
      self.puntret_tds += p.puntret_tds
      self.defense_int_tds += p.defense_int_tds
      self.defense_frec_tds += p.defense_frec_tds
      self.defense_misc_tds += p.defense_misc_tds
      self.defense_safe += p.defense_safe
      self.blocked_kicks += p.defense_puntblk
      self.blocked_kicks += p.defense_xpblk
      self.blocked_kicks += p.defense_fgblk

