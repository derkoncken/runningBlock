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
    def __init__(self, x, y, width, height, control=None):
        super().__init__(x, y, width, height)
        self.control = control


def initilizeEntities(self):
    
    self.players = []
    n = 2000
    for i in range(n):
        player = Player(0, 520, 50, 50)
        self.players.append(player)

    self.ground0 = Ground(0, 580, 300, 2)
    self.ground1 = Ground(300, 500, 100, 2, "right")
    self.ground2 = Ground(600, 420, 300, 2)
    self.ground3 = Ground(300, 340, 100, 2, "left")
    self.ground4 = Ground(0, 260, 300, 2)
    self.ground5 = Ground(300, 180, 100, 2, "right")
    self.ground6 = Ground(600, 100, 300, 2)

    self.grounds = [self.ground0, 
                    self.ground1, 
                    self.ground2, 
                    self.ground3, 
                    self.ground4, 
                    self.ground5,
                    self.ground6]
