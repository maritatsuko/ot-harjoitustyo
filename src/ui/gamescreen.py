import pygame
#from repositories.gameplay import MemoryGame

class GameScreen:
    def __init__(self):
        self.window = pygame.display.set_mode((1080,1080))
        self.font = pygame.font.SysFont("Comic sans", 30)
        pygame.display.set_caption("Mochi")
    
    def draw_screen(self):
        self.window.fill((244,194,194))
        text = self.font.render("Testi", True, (0,0,0))
        self.window.blit(text, (50,50))
        pygame.display.flip()