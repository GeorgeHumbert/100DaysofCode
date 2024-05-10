# paddle.py

import pygame
from constants import PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, HEIGHT, WHITE


class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def draw(self, win):
        pygame.draw.rect(win, WHITE, self.rect)

    def move(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        elif not up and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED
