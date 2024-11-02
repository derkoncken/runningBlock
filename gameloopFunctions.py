import pygame
import random
class GameloopFunctions():

    def displayEntities(self):
        for player in self.players:
            pygame.draw.rect(self.screen, player.color, player)
        for ground in self.grounds:
            pygame.draw.rect(self.screen, (255,0,0), ground)
                        
    def collisionChecks(self):
        for player in self.players:
            player.touchsGround = False
            for ground in self.grounds:
                if player.colliderect(ground):
                    player.touchsGround = True
                
    def gravity(self):
        for player in self.players:
            if player.touchsGround:
                player.acc =0
            else:
                player.acc += 0.5

    def doAiStuff(self):
        self.gameloop.AiTimer += 1
        if self.gameloop.AiTimer == 10:
            self.gameloop.AiTimer = 0
            for player in self.players:
                player.control = random.choice(("jump", "right", "left"))
