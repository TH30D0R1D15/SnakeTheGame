import pygame
import random
class Fruit:
    def __init__(self, x, y, width, height, color):
        self.x = random.randint(1, 1280 - 15)
        self.y = random.randint(1, 720 - 15)
        self.width = width
        self.height = height
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
