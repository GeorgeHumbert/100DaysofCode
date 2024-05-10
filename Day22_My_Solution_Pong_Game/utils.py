# utils.py

import pygame
from constants import BLACK

def draw(win, paddle1, paddle2, ball):
    win.fill(BLACK)
    paddle1.draw(win)
    paddle2.draw(win)
    ball.draw(win)
    pygame.display.update()

def handle_paddle_movement(keys, paddle1, paddle2):
    if keys[pygame.K_w]:
        paddle1.move(up=True)
    if keys[pygame.K_s]:
        paddle1.move(up=False)
    if keys[pygame.K_UP]:
        paddle2.move(up=True)
    if keys[pygame.K_DOWN]:
        paddle2.move(up=False)
