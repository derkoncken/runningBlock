import pygame
from gameloopFunctions import GameloopFunctions

class Gameloop(GameloopFunctions):

    def __init__(self, screen, player, grounds):
        self.screen = screen
        self.player = player
        self.grounds = grounds
        
    def loop(self):
        key = pygame.key.get_pressed()
        
        self.collisionChecks()
        self.gravity()

        if key[pygame.K_w] and self.player.touchsGround:
            self.player.acc -= 10


        self.player.move_ip(0, self.player.acc)

        if key[pygame.K_a]:
            self.player.move_ip(-4,0)
        if key[pygame.K_d]:
            self.player.move_ip(4,0)

        self.displayEntities()     
    