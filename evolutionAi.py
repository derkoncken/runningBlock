import random

class EvolutionAi():
    def EvolutionAiInit(self):
        self.AiTimer = 0
        self.gen = 1
        self.actionlist = []

    def doAiStuff(self):
        self.AiTimer += 1
        if self.AiTimer == 10:
            self.AiTimer = 0


            #for player in self.players:




                #player.control = random.choice(("jump", "right", "left"))