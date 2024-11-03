import pygame
import random

class Player(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.touchsGround = True
        self.acc = 0 
        self.control = None
        self.orientation = "right"
        self.moveset = []
        self.vitality = None

class Ground(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)


def initilizeEntities(self):
    
    self.players = []
    n = 20
    for i in range(n):
        player = Player(0, 520, 50, 50)
        self.players.append(player)

    self.ground0 = Ground(0, 580, 300, 2)
    self.ground1 = Ground(300, 500, 300, 2)
    self.ground2 = Ground(600, 420, 300, 2)
    self.ground3 = Ground(300, 340, 300, 2)
    self.ground4 = Ground(0, 260, 300, 2)
    self.ground5 = Ground(300, 180, 300, 2)
    self.ground6 = Ground(600, 100, 300, 2)

    self.grounds = [self.ground0, 
                    self.ground1, 
                    self.ground2, 
                    self.ground3, 
                    self.ground4, 
                    self.ground5,
                    self.ground6]
