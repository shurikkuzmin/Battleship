import pygame
import pygame.draw

pygame.init()

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

box_size = 60
screen_width = box_size * 10
screen_height = box_size * 10
screen = pygame.display.set_mode((screen_width, screen_height))

def draw(field):
    for row in range(10):
        for column in range(10):
            if field[row][column] == 1:
                pygame.draw.rect(screen, (0,0,255),
                ((column*box_size, row*box_size),(box_size, box_size)))
            pygame.draw.rect(screen, (255,255,255),
            ((column*box_size, row*box_size),(box_size, box_size)),1)

draw(field)

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    pygame.display.update()

pygame.quit()



print(field[3])

print(field[2][2])