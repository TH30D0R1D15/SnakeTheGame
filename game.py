import pygame
import random
from snakePart import SnakePart  # Importiere die externe Klasse SnakePart
from fruit import Fruit  # Importiere die externe Klasse Fruits

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    farbe = pygame.Color(255, 255, 255)

    fruchtX = random.randint(5, 1280 - 15)
    fruchtY = random.randint(5, 1280 - 15)



    # Erstelle ein Block-Objekt
    snake = [SnakePart(100, 100, 15, 15, (255, 0, 0))]
    frucht = Fruit(fruchtX, fruchtY, 15, 15, (0, 255, 0))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT]:
            dx = -5
            dy = 0  # Keine vertikale Bewegung

        if keys[pygame.K_RIGHT]:
            dx = 5
            dy = 0  # Keine vertikale Bewegung

        if keys[pygame.K_UP]:
            dy = -5
            dx = 0  # Keine horizontale Bewegung

        if keys[pygame.K_DOWN]:
            dy = 5
            dx = 0  # Keine horizontale Bewegung


        # Überprüfe, ob die Schlange die Frucht gegessen hat
        if snake[0].x == frucht.x and snake[0].y == frucht.y:
            # Die Schlange hat die Frucht gegessen, also generiere neue zufällige Koordinaten für die Frucht
            frucht.x = random.randint(5, 1280 - 15)
            frucht.y = random.randint(5, 720 - 15)


        # Bewegen und Zeichnen des Blocks
        for part in snake:

            part.move(dx, dy)
            part.draw(screen)

        pygame.display.flip()
        clock.tick(20)

        screen.fill((255,255,255))


    pygame.quit()

if __name__ == "__main__":
    main()