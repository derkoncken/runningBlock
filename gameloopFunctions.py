import pygame
class GameloopFunctions():

    def displayEntities(self):
        pygame.draw.rect(self.screen, (255,0,0), self.player)
        for ground in self.grounds:
            pygame.draw.rect(self.screen, (255,0,0), ground)
                        
    def collisionChecks(self):
        self.player.touchsGround = False
        for ground in self.grounds:
            if self.player.colliderect(ground):
                self.player.touchsGround = True
            
    def gravity(self):
        if self.player.touchsGround:
            self.player.acc =0
        else:
            self.player.acc += 0.5
