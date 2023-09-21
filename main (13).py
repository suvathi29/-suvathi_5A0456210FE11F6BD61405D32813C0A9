
class player:
  def play(self):
    print("The player is playinf cricket")

class Batsman(player):
  def play(self): 
    print("The batsman is batting")

class Bowler(player):
  def play(self):
    print("The Bowler is bowling")

batsman=Batsman()
bowler=Bowler()

batsman.play()
     
        


















