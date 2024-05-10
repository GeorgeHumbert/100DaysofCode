# main.py

import pygame
import sys
from constants import WIDTH, HEIGHT, FPS
from paddle.py import Paddle
from ball import Ball
from utils import draw, handle_paddle_movement


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()

    paddle1 = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    paddle2 = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, paddle1, paddle2)

        ball.move()

        # Colisión de la bola con las paletas
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x *= -1

        draw(win, paddle1, paddle2, ball)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
