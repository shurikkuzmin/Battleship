import pygame
import pygame.draw
import pygame.time
import random

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
            if not isEnemy:
                if field[row][column] == 1:
                    color = (0, 0, 255)
            if field[row][column] == 2:
                color = (255,0,0)
            if field[row][column] == 3:
                color = (255,255,255)    
            pygame.draw.rect(screen, color,
            ((shift + column*box_size, row*box_size),(box_size, box_size)))
            pygame.draw.rect(screen, (255,255,255),
            ((shift + column*box_size, row*box_size),(box_size, box_size)),1)

def check(field):
    for row in field:
        for elem in row:
            if elem == 1:
                return False

    return True

def checkGameOver():
    iWon = check(field_enemy)
    computerWon = check(field)

    if computerWon:
        textMessage = "You lost"
    if iWon:
        textMessage = "You won" 

    if iWon or computerWon:
        font = pygame.font.Font('freesansbold.ttf', 200)
        text = font.render(textMessage, True, (0, 255, 0))
        rect = text.get_rect()
        rect.center = (screen_width/2, screen_height/2)
        screen.blit(text,rect) 
        return True
    return False

def chooseComputerCoordinates(iOld, jOld):
    i = -1
    j = -1
    moveSuccessful = False
    if iOld != -1 and jOld != -1:
        if iOld < 9:
            if field[iOld+1][jOld] < 2:
                i = iOld + 1
                j = jOld
                moveSuccessful = True
        elif iOld > 0:
            if field[iOld-1][jOld] < 2:
                i = iOld - 1
                j = jOld
                moveSuccessful = True
        elif jOld > 0:
            if field[iOld][jOld-1] < 2:
                i = iOld
                j = jOld - 1
                moveSuccessful = True
        elif jOld < 9:
            if field[iOld][jOld+1] < 2:
                i = iOld
                j = jOld + 1
                moveSuccessful = True
    
    if not moveSuccessful:
        while True:
            i = random.randint(0,9)
            j = random.randint(0,9)
            if field[i][j] == 0 or field[i][j] == 1:
                break
    return i, j

def chooseMyCoordinates(x, y):
    j = int((x - 12*box_size) / box_size)
    i = int(y / box_size)
    return i,j


myTurn = True
computerTurn = False
isRunning = True
buttonClicked = False
gameOver = False
iOld = -1
jOld = -1
while isRunning:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            buttonClicked = True
 
    if gameOver and buttonClicked:
        isRunning = False
        continue

    if gameOver:
        continue

    if buttonClicked and myTurn:

        i,j = chooseMyCoordinates(x, y)
        if j >= 0:
            if field_enemy[i][j] == 1:
                field_enemy[i][j] = 2
            if field_enemy[i][j] == 0:
                field_enemy[i][j] = 3
                myTurn = False
                computerTurn = True

        buttonClicked = False

    elif computerTurn:
        i,j = chooseComputerCoordinates(iOld, jOld)
        if field[i][j] == 1:
            field[i][j] = 2
            iOld = i
            jOld = j

        if field[i][j] == 0:
            iOld = -1
            jOld = -1
            field[i][j] = 3
            myTurn = True
            computerTurn = False 
        pygame.time.delay(700)       

    draw(field, False)
    draw(field_enemy, True)

    if not gameOver:
        gameOver = checkGameOver()
    
    pygame.display.update()

pygame.quit()



print(field[3])

print(field[2][2])