import random
import pygame

class Food:
    # Food() produces a food particle that the Snake enjoy to eat
    # __init__: None -> Food
    def __init__(self):
        self.x = random.randint(0, 1000-20) // 20 * 20
        self.y = random.randint(0, 600-20) // 20 * 20
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = (0, 0, 255)
