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

class Helper:
    def __init__(self):
        self.previousRow = -1
        self.previousColumn = -1
        self.mouseX = -1
        self.mouseY = -1
        self.mouseButton = False
        self.gameOver = False
    def mouseButtonClicked(self, event):
        self.mouseButton = True
        self.mouseX, self.mouseY = event.pos
    
    def toStop(self):
        if self.gameOver and self.mouseButton:
            return True
        return False
    

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

def chooseComputerCoordinates(helper):
    i = -1
    j = -1
    moveSuccessful = False
    if helper.previousRow != -1 and helper.previousColumn != -1:
        if helper.previousRow < 9:
            if field[helper.previousRow+1][helper.previousColumn] < 2:
                i = helper.previousRow + 1
                j = helper.previousColumn
                moveSuccessful = True
        elif helper.previousRow > 0:
            if field[helper.previousRow-1][helper.previousColumn] < 2:
                i = helper.previousRow - 1
                j = helper.previousColumn
                moveSuccessful = True
        elif helper.previousColumn > 0:
            if field[helper.previousRow][helper.previousColumn-1] < 2:
                i = helper.previousRow
                j = helper.previousColumn - 1
                moveSuccessful = True
        elif helper.previousColumn < 9:
            if field[helper.previousRow][helper.previousColumn+1] < 2:
                i = helper.previousRow
                j = helper.previousColumn + 1
                moveSuccessful = True
    
    if not moveSuccessful:
        while True:
            i = random.randint(0,9)
            j = random.randint(0,9)
            if field[i][j] == 0 or field[i][j] == 1:
                break
    return i, j

def chooseMyCoordinates(helper):
    j = -1
    if helper.mouseX >= 12*box_size:
        j = int((helper.mouseX - 12*box_size) / box_size)
    i = int(helper.mouseY / box_size)
    return i,j

def chooseCoordinates(turn, helper):
    i = -1
    j = -1
    helper.mouseButton = False
    if turn:
        i,j = chooseMyCoordinates(helper)
    else:
        i,j = chooseComputerCoordinates(helper)
    return i,j

def makeMyMove(i,j):
    if j >= 0:
        if field_enemy[i][j] == 1:
            field_enemy[i][j] = 2
            return True

        if field_enemy[i][j] == 0:
            field_enemy[i][j] = 3
            return False

    return True

def makeComputerMove(i,j, helper):
    localTurn = False
    if field[i][j] == 1:
        field[i][j] = 2
        helper.previousRow = i
        helper.previousColumn = j

    if field[i][j] == 0:
        helper.previousRow = -1
        helper.previousColumn = -1
        field[i][j] = 3
        localTurn = True
 
    pygame.time.delay(700)
    return localTurn

def makeMove(turn, helper, i, j):
    localTurn = False
    if turn:
        localTurn = makeMyMove(i, j)
    else:
        localTurn = makeComputerMove(i, j, helper)
    
    return localTurn

def checkNonEmpty(arr, i, j):
    for indRow in range(-1,2):
        if (i + indRow > 9) or (i + indRow < 0):
            continue
        for indColumn in range(-1,2):
            if (j + indColumn > 9) or (j + indColumn < 0):
                continue
            if arr[i+indRow][j+indColumn] != 0:
                return True
    
    return False

def generateFieldEnemy():
    arr = [[0,0,0,0,0,0,0,0,0,0] for x in range(10)]
    for size in range(4,0,-1):
        for numShips in range(5-size):
            
            success = False
            while not success:
                isVertical = random.choice([True, False])
                i = random.randint(0, 9)
                j = random.randint(0, 9)

                allZeros = True
                if isVertical:
                    deltaRow = 1
                    deltaColumn = 0
                else:
                    deltaRow = 0
                    deltaColumn = 1
                if (i + deltaRow*size >= 10) or (j + deltaColumn*size >= 10):
                    continue 

                for ind in range(size):
                    if checkNonEmpty(arr, i+deltaRow*ind, j+deltaColumn*ind):
                        allZeros = False
                
                if allZeros:
                    success = True
                    for ind in range(size):
                        arr[i+deltaRow*ind][j+deltaColumn*ind] = 1
                    
    return arr

isRunning = True
turn = True

field_enemy = generateFieldEnemy()
for i in range(10):
    print(field_enemy[i])

helper = Helper()
while isRunning:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            helper.mouseButtonClicked(event)
 
    if helper.toStop():
        isRunning = False
        continue

    if helper.gameOver:
        continue

    i,j = chooseCoordinates(turn, helper)
    turn = makeMove(turn, helper, i, j)
               
    draw(field, False)
    draw(field_enemy, True)

    if not helper.gameOver:
        helper.gameOver = checkGameOver()
    
    pygame.display.update()

pygame.quit()
