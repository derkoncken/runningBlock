import random
from entities import initilizeEntities

class EvolutionAi():
    def EvolutionAiInit(self):
        self.AiTimer = 0
        self.stateMove = 0
        self.maxMoves = 0
        self.moves = []
        self.gen = 0
        #Parameters for Adjusting
        self.numberOfEntities = 100     #Number of entities
        self.newMovements = 5           #Amount of moves for every new gen
        self.durationOfMovement = 6     #Anmout of Ticks, how long a move should be executed
        self.mutationRatio = 10         #Reciprocal of the ratio, how many instruction of the moveset should get mutated


    def doAiStuff(self):
        self.AiTimer += 1
        if self.AiTimer == self.durationOfMovement:             #After durationOfMovement of frames, the next instruction will be used
            self.AiTimer = 0
            if self.stateMove == self.maxMoves:                 #After the last instruction...
                bestPlayer = self.players[0]
                for player in self.players:
                    player.vitality = player.top        
                    if player.vitality < bestPlayer.vitality:   #...the best player will be choosen
                        bestPlayer = player
                self.moves = bestPlayer.moveset
                self.stateMove = 0
                self.gen += 1
                self.maxMoves += self.newMovements
                initilizeEntities(self)                         #Status of the new Gen
                print("-------------------------------------")
                print("Generation: " + str(self.gen))
                print("Amout of Moves: " + str(self.maxMoves))
                print("Best Instance had a vitality of: " + str(580 - bestPlayer.vitality))

                for player in self.players:
                    player.moveset = list(self.moves)
                    for i in range(self.newMovements):
                        player.moveset.append(random.choice(("jump", "right", "left")))     #The list of instuctions will be expanded by random newMovements elements
                    for i in range(int(self.maxMoves/self.mutationRatio)):
                        index = random.randint(0, len(player.moveset) - 1)                  #Mutation is applied
                        player.moveset[index] = random.choice(("jump", "right", "left"))

                
            for player in self.players:
                player.control = player.moveset[self.stateMove]                             #Next instruction will be used
            self.stateMove += 1