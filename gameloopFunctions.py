import pygame
import random
class GameloopFunctions():

    def displayEntities(self):
        for player in self.players:

        
            pygame.draw.rect(self.screen, player.color, player)
            """
            lamaRaw = pygame.image.load("lama.png").convert_alpha()
            lama = pygame.transform.scale(lamaRaw, (50, 50))
            if player.control == "right":
                player.orientation = "right"
            if player.control == "left":
                player.orientation = "left"

            if player.orientation == "left":
                leftLama = pygame.transform.flip(lama, True, False)
                self.screen.blit(leftLama, player)
            if player.orientation == "right":
                self.screen.blit(lama, player)
            """
        for ground in self.grounds:
            pygame.draw.rect(self.screen, (255,0,0), ground)

                        
    def collisionChecks(self):
        for player in self.players:
            player.touchsGround = False
            for ground in self.grounds:
                # Prüfen, ob der untere Rand des Players mit der oberen Kante des Bodens kollidiert
                if player.colliderect(ground) and player.bottom >= ground.top and player.bottom <= ground.top + 5:
                    player.touchsGround = True

                
    def gravity(self):
        for player in self.players:
            if player.touchsGround:
                player.acc =0
            else:
                player.acc += 0.5


