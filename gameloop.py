import pygame
from gameloopFunctions import GameloopFunctions

class Gameloop(GameloopFunctions):

    def __init__(self, screen, player, grounds):
        self.AiTimer = 0
        self.screen = screen
        self.player = player
        self.grounds = grounds


    def loop(self):
        #key = pygame.key.get_pressed()
        self.doAiStuff()
        self.collisionChecks()
        self.gravity()
        
        for player in self.players:

            if player.control == "jump" and player.touchsGround:
                player.acc -= 10
            player.move_ip(0, player.acc)


            if player.control == "left":
                player.move_ip(-4,0)
            if player.control == "right":
                player.move_ip(4,0)

        self.displayEntities()     
    