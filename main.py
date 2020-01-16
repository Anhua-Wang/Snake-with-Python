import pygame
import random
from food import Food
from snake import Snake

pygame.init()

# Utilities
grid_size = 20
(width, height) = (1000, 600)

# Initiate the move
move_x = grid_size
move_y = 0

# Initiating the game window
background_colour = (0, 0, 0)
screen = pygame.display.set_mode((width, height))
screen.fill(background_colour)

var = 20
while var != 1000:
    pygame.draw.line(screen, (0, 0, 100), [var, 0], [var, 600], 1)
    pygame.draw.line(screen, (0, 0, 100), [0, var], [1000, var], 1)
    var += 20


# Drawing Snake
snake = Snake(500,300)

# Drawing Food
food = Food()

running = True
direction = "right"
while running:
    pygame.time.wait(250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                move_x = 0
                move_y = -grid_size
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                move_x = 0
                move_y = grid_size
                direction = "down"
            if event.key == pygame.K_LEFT and direction != "right":
                move_x = -grid_size
                move_y = 0
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                move_x = grid_size
                move_y = 0
                direction = "right"

    #screen.fill(background_colour)
    snake.move(move_x, move_y)
    head = snake.head

    for i in range(snake.length):
        body_part = pygame.Rect(head.x, head.y, grid_size, grid_size)
        pygame.draw.rect(screen, snake.color, body_part)
        head = head.next

    if snake.head.x == food.x and snake.head.y == food.y:
        snake.length += 1
        food = Food()
        

    pygame.draw.rect(screen, snake.color, food.rect)

    pygame.display.flip()