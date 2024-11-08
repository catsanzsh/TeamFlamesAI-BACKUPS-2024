import tkinter as tk
import pygame
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
SNAKE_COLOR = (255, 0, 0)  # Red
FOOD_COLOR = (255, 250, 205) # Beige
BACKGROUND_COLOR = (0,0,0)

# Initialize Pygame display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)


# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = "Right"

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "Right":
            new_head = (head_x + CELL_SIZE, head_y)
        elif self.direction == "Left":
            new_head = (head_x - CELL_SIZE, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - CELL_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + CELL_SIZE)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        head_x, head_y = self.body[0]
        if self.direction == "Right":
            new_head = (head_x + CELL_SIZE, head_y)
        elif self.direction == "Left":
            new_head = (head_x - CELL_SIZE, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - CELL_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + CELL_SIZE)
        self.body.insert(0, new_head)

    def check_collision(self):
        head = self.body[0]
        if (head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in self.body[1:]):
            return True
        return False


# Game functions
def generate_food():
    return (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)

def draw_snake(snake):
    for segment in snake.body:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, FOOD_COLOR, (food[0], food[1], CELL_SIZE, CELL_SIZE))

def display_score(score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def game_over_screen(score):
    screen.fill(BACKGROUND_COLOR)
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    text_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
    score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
    screen.blit(game_over_text, text_rect)
    screen.blit(score_text, score_rect)
    pygame.display.update()
    pygame.time.delay(3000) # Wait for 3 seconds
    pygame.quit()


# Game loop
def game_loop():
    snake = Snake()
    food = generate_food()
    clock = pygame.time.Clock()
    game_over = False
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.direction != "Right":
                    snake.direction = "Left"
                elif event.key == pygame.K_RIGHT and snake.direction != "Left":
                    snake.direction = "Right"
                elif event.key == pygame.K_UP and snake.direction != "Down":
                    snake.direction = "Up"
                elif event.key == pygame.K_DOWN and snake.direction != "Up":
                    snake.direction = "Down"

        snake.move()
        if snake.check_collision():
            game_over_screen(score)
            game_over = True

        if snake.body[0] == food:
            snake.grow()
            food = generate_food()
            score += 1

        screen.fill(BACKGROUND_COLOR)  # Black background
        draw_snake(snake)
        draw_food(food)
        display_score(score)
        pygame.display.update()
        clock.tick(10)  # Adjust speed here

game_loop()
## [C] Team Flames GROUP. N  CO 2024-2025
