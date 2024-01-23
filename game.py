# Imports
import pygame
import random
from snakePart import SnakePart
from fruit import Fruit

#Hauptprogramm
def main():
    # pygame setup
    pygame.init()

    pygame.display.set_caption('Snake THE Game')
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    farbe = pygame.Color(255, 255, 255)



    # Erstelle ein Snake-Objekt
    snake = [SnakePart(100, 100, 22.5, 22.5, (255, 0, 0))]

    # Erstelle ein Frucht-Objekt
    frucht = Fruit(0, 0, 22.5, 22.5, (0, 255, 0))

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

    #    if (frucht.x <= snake[0].x <= frucht.x + frucht.width) and (frucht.y <= snake[0].y <= frucht.y + frucht.height):
    #   if snake[0].x >= frucht.x and snake[0].y >= frucht.y:
    #    if (snake[0].x == frucht.x and snake[0].y == frucht.y) or (snake[0].x >= frucht.x and snake[0].y >= frucht.y):
    #    if (snake[0].x >= frucht.x + frucht.width) and (snake[0].y >= frucht.y + frucht.height):
    #    if (snake[0].x >= frucht.x) and (snake[0].y >= frucht.y):
        if snake[0].x >= frucht.x + frucht.width and snake[0].y >= frucht.y + frucht.height:
            print("Frucht wurde gegessen!")

            # Die Schlange hat die Frucht gegessen, also generiere neue zufällige Koordinaten für die Frucht
            frucht.generate()

        # Bewegen und Zeichnen des Snake-Blocks
        for part in snake:
            part.move(dx, dy)
            part.draw(screen)
        print("Neue Snakeposition:", snake[0].x, snake[0].y)

        #  Zeichnen des Frucht-Blocks
        frucht.draw(screen)
        print("Neue Fruchtposition:", frucht.x, frucht.y)



        pygame.display.flip()
        clock.tick(25)

        screen.fill((255,255,255))


    pygame.quit()



if __name__ == "__main__":
    main()