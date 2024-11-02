import pygame
import random

class Player(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.touchsGround = True
        self.acc = 0 
        self.control = None

class Ground(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)


def initilizeEntities(self):
    self.player1 = Player(300, 440, 50, 50)
    self.player2 = Player(380, 440, 50, 50)

    self.ground1 = Ground(300, 500, 300, 10)
    self.ground2 = Ground(600, 420, 300, 10)
    self.ground3 = Ground(300, 340, 300, 10)
    self.ground4 = Ground(0, 260, 300, 10)

    self.players = [self.player1, self.player2]
    self.grounds = [self.ground1, self.ground2, self.ground3, self.ground4]
