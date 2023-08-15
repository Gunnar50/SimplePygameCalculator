import pygame
from settings import *
from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.buttons = [
            Button(50, 200, 7),
            Button(150, 200, 8),
            Button(250, 200, 9),
            Button(350, 200, "/"),
            Button(50, 300, 4),
            Button(150, 300, 5),
            Button(250, 300, 6),
            Button(350, 300, "x"),
            Button(50, 400, 1),
            Button(150, 400, 2),
            Button(250, 400, 3),
            Button(350, 400, "-"),
            Button(50, 500, "."),
            Button(150, 500, 0),
            Button(250, 500, "="),
            Button(350, 500, "+"),
            Button(50, 600, "CLEAR", width=380),
        ]
        self.clock = pygame.time.Clock()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BGCOLOUR)
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.is_mouse_in(mx, my):
                        button.on_click()


game = Game()
game.run()
