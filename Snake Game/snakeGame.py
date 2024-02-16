import pygame
import random
import sys


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

BLOCK_SIZE = 15

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Snake Game by Amir")

font = pygame.font.SysFont(None, 25)


def display_text(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(
            screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])


def action():

    snake_list = []
    snake_length = 1
    x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
    snake_list.append([x, y])

    food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    direction = "right"

    game_over = False

    clock = pygame.time.Clock()

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"
                elif event.key == pygame.K_UP and direction != "down":
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"

        if direction == "right":
            x += BLOCK_SIZE
        elif direction == "left":
            x -= BLOCK_SIZE
        elif direction == "up":
            y -= BLOCK_SIZE
        elif direction == "down":
            y += BLOCK_SIZE

        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_over = True

        for block in snake_list[1:]:
            if x == block[0] and y == block[1]:
                game_over = True

        if x == food_x and y == food_y:
            # Generate a new food location
            food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(
                0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

            snake_length += 1

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        screen.fill(WHITE)

        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        draw_snake(snake_list)

        score = snake_length - 1
        score_text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(score_text, [0, 0])

        pygame.display.update()

        clock.tick(10)

    display_text("Game Over", RED)
    pygame.display.update()

    pygame.time.wait(2000)

    pygame.quit()


def display_text(text, color):

    font = pygame.font.SysFont("Arial", 50)

    text_obj = font.render(text, True, color)

    text_rect = text_obj.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)

    screen.blit(text_obj, text_rect)

    font = pygame.font.SysFont("Arial", 25)
    text_obj = font.render("Press R to restart or Q to quit", True, BLACK)
    text_rect = text_obj.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    screen.blit(text_obj, text_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    action()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


action()
