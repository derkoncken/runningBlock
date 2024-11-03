import random
from entities import initilizeEntities

class EvolutionAi():
    def EvolutionAiInit(self):
        self.AiTimer = 0
        self.state = 0
        self.gen = 0
        self.actionList = []
        self.newMovements = 50

    def doAiStuff(self):
        self.AiTimer += 1
        if self.AiTimer == 5:
            self.AiTimer = 0
            if self.state == self.gen:
                bestPlayer = self.players[0]
                for player in self.players:
                    if player.centery < bestPlayer.centery:
                        bestPlayer = player
                self.actionList = bestPlayer.moveset
                self.state = 0
                self.gen += self.newMovements
                initilizeEntities(self)
                print(self.gen)

                for player in self.players:
                    player.moveset = list(self.actionList)
                    for i in range(self.newMovements):
                        player.moveset.append(random.choice(("jump", "right", "left")))
            for player in self.players:
                player.control = player.moveset[self.state]
            self.state += 1