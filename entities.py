import pygame

class Player(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.touchsGround = True
        self.acc = 0 

class Ground(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)


def initilizeEntities(self):
    self.player = Player(100, 300, 50, 50)
    self.ground1 = Ground(0, 500, 700, 50)
    self.ground2 = Ground(400, 450, 300, 50)
    self.grounds = [self.ground1, self.ground2]
