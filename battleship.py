import pygame
import pygame.draw

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    pygame.draw.circle(screen,(255,0,0),(100,100), 20.0)
    pygame.display.update()

pygame.quit()

field = [[0,0,0,0,1,0,0,0,1,0],
         [0,0,1,0,0,0,0,0,0,0],
         [0,0,0,0,0,1,0,1,0,1],
         [0,0,0,0,0,1,0,1,0,0],
         [0,0,0,0,0,1,0,1,0,0],
         [0,0,0,0,0,1,0,0,0,0],
         [0,1,1,1,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,1,1,0,0,1,1,0,1,0],
         [0,0,0,0,0,0,0,0,1,0]]

print(field[3])

print(field[2][2])