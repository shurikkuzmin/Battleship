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

field_enemy = [[0,0,1,0,0,0,0,0,1,1],
               [0,0,0,0,0,0,0,0,0,0],
               [1,1,0,1,0,0,0,0,0,0],
               [0,0,0,1,0,0,0,1,0,0],
               [0,0,0,1,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,1,1,1,0,1,1,1,1,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,1,0,0,0,0,0,0,0,0],
               [0,0,0,1,0,0,1,0,0,0]]

box_size = 60
screen_width = box_size * 22
screen_height = box_size * 10
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fps = 120

def draw(field, isEnemy):
    shift = 0
    if isEnemy:
        shift = 12 * box_size
    
    for row in range(10):
        for column in range(10):
            color = (0,0,0)
            if field[row][column] == 1 and not isEnemy:
                color = (0, 0, 255)
            if isEnemy:
                if field[row][column] == 2:
                    color = (255,0,0)
                if field[row][column] == 3:
                    color = (255,255,255)    
            pygame.draw.rect(screen, color,
            ((shift + column*box_size, row*box_size),(box_size, box_size)))
            pygame.draw.rect(screen, (255,255,255),
            ((shift + column*box_size, row*box_size),(box_size, box_size)),1)


isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            j = int((x - 12*box_size) / box_size)
            i = int(y / box_size)
            if j >= 0:
                if field_enemy[i][j] == 1:
                    field_enemy[i][j] = 2
                if field_enemy[i][j] == 0:
                    field_enemy[i][j] = 3

    draw(field, False)
    draw(field_enemy, True)

    clock.tick(fps)
    pygame.display.update()

pygame.quit()



print(field[3])

print(field[2][2])