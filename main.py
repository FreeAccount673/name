import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('igra')

def gameLoop():
    game_over = False
    game_close = False

    x = dis_width//2
    y = dis_height//2
    x_change = 0.5
    y_change = 0



    while not game_over:
        #dis.fill(black)
        #pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= x_change
        elif keys[pygame.K_RIGHT]:
            x += x_change

        dis.fill(white)
        pygame.draw.rect(dis, blue, (x, y, 10, 20))
        pygame.display.update()

    pygame.quit()
    quit()

gameLoop()