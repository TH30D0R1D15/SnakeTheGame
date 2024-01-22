# Imports
import pygame
import random
from snakePart import SnakePart
from fruit import Fruit

#Hauptprogramm
def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    farbe = pygame.Color(255, 255, 255)


    #fruchtX = random.randint(5, 1280 - 15)
    #fruchtY = random.randint(5, 720 - 15)

    fruchtX = random.randint(5, 800 - 15)
    fruchtY = random.randint(5, 600 - 15)


    # Erstelle ein Snake-Objekt
    snake = [SnakePart(100, 100, 22.5, 22.5, (255, 0, 0))]

    # Erstelle ein Frucht-Objekt
#    frucht = Fruit(fruchtX, fruchtY, 10, 10, (0, 255, 0))
    frucht = Fruit(fruchtX, fruchtY, 10, 10, (0, 255, 0))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        # Tastatur-listening
        #-------------------
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT]:
            dx = -10
            dy = 0  # Keine vertikale Bewegung

        if keys[pygame.K_RIGHT]:
            dx = 10
            dy = 0  # Keine vertikale Bewegung

        if keys[pygame.K_UP]:
            dy = -10
            dx = 0  # Keine horizontale Bewegung

        if keys[pygame.K_DOWN]:
            dy = 10
            dx = 0  # Keine horizontale Bewegung


        # Überprüfe, ob die Schlange die Frucht gegessen hat
        if snake[0].x == frucht.x and snake[0].y == frucht.y:
            # Die Schlange hat die Frucht gegessen, also generiere neue zufällige Koordinaten für die Frucht
            frucht.generate()

        # Bewegen und Zeichnen des Snake-Blocks
        for part in snake:
            part.move(dx, dy)
            part.draw(screen)

        #  Zeichnen des Frucht-Blocks

        frucht.draw(screen)



        pygame.display.flip()
        clock.tick(20)

        screen.fill((255,255,255))


    pygame.quit()

if __name__ == "__main__":
    main()