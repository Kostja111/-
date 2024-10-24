class Cs2:
    def __init__(self):
        # super().__init__()
        self.graphics = "2K"
class Pubg:
  def __init__(self):
   # super().__init__()
   self.xd = 2
class StandOff(Cs2, Pubg):
  def print_info(self):
   print(self.graphics)
   print(self.xd)

Game = StandOff()
Game.print_info()