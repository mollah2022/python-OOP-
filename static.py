class Player:

    total_run = 0

    def __init__(self,run):
        self.run = run

    def hit_four(self):
        self.run += 4
        Player.total_run += 4

    def hit_six(self):
        self.run += 6
        Player.total_run += 6

    def runView(self,name):
        self.name = name
        print(self.name," ",self.run)
    
shakib = Player(0)
tamim = Player(0)
shakib.hit_four()
tamim.hit_six()
shakib.hit_six()
tamim.hit_four()

shakib.runView("Shakib")
tamim.runView("Tamim")
h = Player.total_run
print("Total Run",h)


            