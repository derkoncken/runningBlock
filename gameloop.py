import pygame
from gameloopFunctions import GameloopFunctions

class Gameloop(GameloopFunctions):

    def __init__(self, screen, player, grounds):
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


        for ground in self.grounds:
            if ground.control is not None:
                if ground.control == "right":
                    ground.move_ip(2,0)
                    if ground.centerx > 600:
                        ground.control = "left"
                if ground.control == "left":
                    ground.move_ip(-2,0)
                    if ground.centerx < 300:
                        ground.control = "right"
        
            
        
        self.displayEntities()     
    