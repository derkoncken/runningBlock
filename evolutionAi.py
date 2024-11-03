import random
from entities import initilizeEntities

class EvolutionAi():
    def EvolutionAiInit(self):
        self.AiTimer = 0
        self.stateMove = 0
        self.maxMoves = 0
        self.moves = []
        self.newMovements = 30
        self.gen = 0

    def doAiStuff(self):
        self.AiTimer += 1
        if self.AiTimer == 10:
            self.AiTimer = 0
            if self.stateMove == self.maxMoves:
                bestPlayer = self.players[0]
                for player in self.players:
                    player.vitality = player.top
                    if player.vitality < bestPlayer.vitality:
                        bestPlayer = player
                self.moves = bestPlayer.moveset
                self.stateMove = 0
                self.gen += 1
                self.maxMoves += self.newMovements
                initilizeEntities(self)
                print("-------------------------------------")
                print("Generation: " + str(self.gen))
                print("Amout of Moves: " + str(self.maxMoves))
                print("Best Instance had a vitality of: " + str(580 - bestPlayer.vitality))

                for player in self.players:
                    player.moveset = list(self.moves)
                    for i in range(self.newMovements):
                        player.moveset.append(random.choice(("jump", "right", "left")))
            for player in self.players:
                player.control = player.moveset[self.stateMove]
            self.stateMove += 1