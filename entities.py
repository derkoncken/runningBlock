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
    def __init__(self, x, y, width, height, range=None):
        super().__init__(x, y, width, height)
        self.range = range
        self.control = "right"


def initilizeEntities(self):
    
    self.players = []
    n = 2000
    for i in range(n):
        player = Player(0, 520, 50, 50)
        self.players.append(player)

    self.ground0 = Ground(0, 580, 300, 2,)
    self.ground1 = Ground(0, 500, 100, 2, (0, 900))
    self.ground2 = Ground(800, 420, 100, 2, (0, 900))
    self.ground3 = Ground(450, 340, 100, 2, (0, 900))
    self.ground4 = Ground(0, 260, 100, 2, (0, 900))
    self.ground5 = Ground(600, 180, 100, 2, (0, 900))
    self.ground6 = Ground(600, 100, 300, 2)

    self.grounds = [self.ground0, 
                    self.ground1, 
                    self.ground2, 
                    self.ground3, 
                    self.ground4, 
                    self.ground5,
                    self.ground6]
