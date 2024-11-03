#Hi
import pygame
from gameloop import Gameloop
from entities import Player, Ground, initilizeEntities
from evolutionAi import EvolutionAi
 

class Game(Gameloop, Player, Ground, EvolutionAi):
    def __init__(self):
        pygame.init()
        
        self.SCREEN_WIDTH = 900
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.run = True
        self.EvolutionAiInit()
        initilizeEntities(self)
        self.gameloop = Gameloop(self.screen, self.players, self.grounds)
        
        
    def execute(self):
        while self.run:
            pygame.display.update()
            self.screen.fill((0,0,0))
            self.clock.tick(90)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.loop()
        pygame.quit()

game = Game()
game.execute()


