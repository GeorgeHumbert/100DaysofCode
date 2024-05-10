# ball.py

import pygame
from constants import BALL_RADIUS, BALL_SPEED_X, BALL_SPEED_Y, WIDTH, HEIGHT, WHITE


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.rect.center = (x, y)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def draw(self, win):
        pygame.draw.ellipse(win, WHITE, self.rect)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Colisión con las paredes superior e inferior
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

        # Colisión con las paredes izquierda y derecha (reseteo de la bola)
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.rect.center = (WIDTH // 2, HEIGHT // 2)
            self.speed_x *= -1
