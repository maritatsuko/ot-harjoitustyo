import pygame
#from ui.gamescreen import GameScreen

class MemoryGame:
    def __init__(self):
        #self.GameScreen = GameScreen
        pygame.init()

        self.window = pygame.display.set_mode((1080,1080))
        self.font = pygame.font.SysFont("Comic sans", 30)
        pygame.display.set_caption("Mochi")

        self.loop()

    def loop(self):
        while True:
            self.events()
            self.draw_screen()

    def draw_screen(self): #this should be in gamescreen but i can't get the import from another file to work
        self.window.fill((244,194,194))
        text = self.font.render("Testi", True, (0,0,0))
        self.window.blit(text, (50,50))
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def get_board(self):
        icons = [("oval",(60,60,100)), ("oval", (255,255,255))] * 2
        board = []
        for X in range(2):
            column = []
            for Y in range(2):
                column.append(icons[Y])
            board.append(column)
        return board

if __name__ == "__main__":
    MemoryGame()
