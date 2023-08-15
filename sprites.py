import pygame
from settings import *


class Text:
    def __init__(self, x, y, text, size, colour):
        self.x, self.y = x, y
        self.text = text
        self.size = size
        self.colour = colour

    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 30)
        text_render = font.render(str(self.text), True, BLACK)
        screen.blit()

class Button:
    def __init__(self, x, y, text, width=80, height=80, command=None):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.text = text
        self.command = command

    def draw(self, screen):
        font = pygame.font.SysFont("Consolas", 30)
        text_render = font.render(str(self.text), True, BLACK)
        draw_x = self.x + (self.width / 2 - text_render.get_width() / 2)
        draw_y = self.y + (self.height / 2 - text_render.get_height() / 2)
        pygame.draw.rect(screen, LIGHTGREY, (self.x, self.y, self.width, self.height))
        screen.blit(text_render, (draw_x, draw_y))

    def is_mouse_in(self, mx, my):
        return self.x <= mx < self.x + self.width and self.y <= my < self.y + self.width

    def on_click(self):
        if self.command is None:
            return self.text
        else:
            self.command()


