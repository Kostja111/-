class Doom_shroom:
    def __init__(self):
        self.reload = '2m'
class Sun_shroom:
    def __init__(self):
        self.cost = "25sun"
class Scaredy_shroom(Doom_shroom, Sun_shroom):
   def print_info(self):
    super().__init__()
    print(self.reload)
    print(self.cost)

Plants = Sun_shroom()
print(Plants, )