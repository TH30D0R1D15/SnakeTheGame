import pygame
import random
class Fruit:
    def __init__(self, x, y, width, height, color):
        self.x = random.randint(10, 800 - 15)
        self.y = random.randint(10, 600 - 15)
        self.width = width
        self.height = height
        self.color = color


    def generate(self):
        self.x = random.randint(10, 800 - 15)
        self.y = random.randint(10, 600 - 15)


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
