# Impoting and Initializing pygame

import pygame
pygame.init()

# Initializing gameWindow

screenX,screeeY=450,450
gameWindow=pygame.display.set_mode((screenX,screeeY))
pygame.display.set_caption("Sudoku Solver")
clock=pygame.time.Clock()

# Game variables
exit_game=False

# Return Position of rectangle

def drawRect(pos):
    x=pos[0]//50
    y=pos[1]//50
    return (x,y) 

#  Rendering Text

def textRender(text,color,x,y,size):
    font=pygame.font.SysFont(None,size)
    screenText=font.render(text,True,color)
    gameWindow.blit(screenText,(x,y))

# Taking input

def fillSpace():
    global key
    global selected
    if key!=None and selected==True and key!=0:
        cubes[sel_pos[1]][sel_pos[0]]=str(key)
        board[sel_pos[1]][sel_pos[0]]=key
        selected=False
        key=None
    elif key==0:
        cubes[sel_pos[1]][sel_pos[0]]=' '
        board[sel_pos[1]][sel_pos[0]]=0
        selected=False
        key=None

# Resetting board

def resetBoard():
    global board
    global cubes
    board=[[0 for i in range(9)]for j in range(9)]
    cubes=[[' ' for i in range(9)] for j in range(9)]

# Finding empty cell

def findEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (i,j)
    return None

# Checing validity of the position

def checkValid(board,num,pos):
    # To check the number in row
    for i in range(9):
        if board[pos[0]][i]==num:
            return False
    
    # To check the number in column
    for j in range(9):
        if board[j][pos[1]]==num:
            return False

    # To check the 3*3 box

    # First make them 9 parts
    pos_x = pos[0]//3
    pos_y = pos[1]//3

    for i in range(pos_x*3,pos_x*3+3):
        for j in range(pos_y*3,pos_y*3+3):
            if board[i][j]==num:
                return False

    return True

# Solving the SUDOKU

def solve(bo):
    find=findEmpty(bo)
    if not find:
        return True
    else:
        row,col=find
    
    for i in range(1,10):
        if checkValid(bo,i,(row,col)):
            bo[row][col]=i
            
            if solve(board):
                return True
            else:
                bo[row][col]=0

    return False

# Filing solved board

def fillSolved():
    global board
    global cubes
    for i in range(9):
        for j in range(9):
            cubes[i][j]=str(board[i][j])

def welcome():
    global exit_game
    while not exit_game:
        if exit_game==True:
            break
        pygame.Surface.fill(gameWindow,(255,255,255))
        textRender("Welcome to Sudoku Solver",(0,0,0),80,70,35)
        textRender("By",(0,0,0),210,100,25)
        textRender("MRPNH",(255,0,0),170,130,40)
        textRender("-: Instructions :-",(0,0,0),150,180,25)
        textRender("Backspace : Delete",(0,0,255),138,220,25)
        textRender("Escape : Clear",(0,0,255),155,260,25)
        textRender("Space : Solve",(0,0,255),157,300,25)
        textRender("Press Space Bar To Start",(0,0,0),135,400,20)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameLoop()                    
        pygame.display.update()
        clock.tick(60)
   


def gameLoop():
    global exit_game
    global key
    global solved
    global selected
    global cubes
    global board
    global sel_pos
    # Board Initialization
    board=[[0 for i in range(9)]for j in range(9)]
    cubes=[[' ' for i in range(9)] for j in range(9)]
    solved=False
    key=None
    selected=False
    while not exit_game:
        gameWindow.fill((255,255,255))
        for event in pygame.event.get():
             if event.type==pygame.QUIT:
                  exit_game=True

             if event.type==pygame.MOUSEBUTTONDOWN:
                 pos=pygame.mouse.get_pos()
                 selected=True
                 sel_pos=drawRect(pos)
        
             if event.type==pygame.KEYDOWN:
                   if event.key==pygame.K_1:
                       key=1
                   if event.key==pygame.K_2:
                       key=2
                   if event.key==pygame.K_3:
                       key=3
                   if event.key==pygame.K_4:
                       key=4
                   if event.key==pygame.K_5:
                       key=5
                   if event.key==pygame.K_6:
                       key=6
                   if event.key==pygame.K_7:
                        key=7
                   if event.key==pygame.K_8:
                        key=8
                   if event.key==pygame.K_9:
                         key=9
                   if event.key==pygame.K_KP1:
                         key=1
                   if event.key==pygame.K_KP2:
                         key=2
                   if event.key==pygame.K_KP3:
                         key=3
                   if event.key==pygame.K_KP4:
                         key=4
                   if event.key==pygame.K_KP5:
                         key=5
                   if event.key==pygame.K_KP6:
                         key=6
                   if event.key==pygame.K_KP7:
                         key=7
                   if event.key==pygame.K_KP8:
                         key=8
                   if event.key==pygame.K_KP9:
                         key=9
                   if event.key==pygame.K_BACKSPACE:
                         key=0
                   if event.key==pygame.K_SPACE:
                         solved=solve(board)
                         fillSolved()
                   if event.key==pygame.K_ESCAPE:
                         resetBoard()

        fillSpace()
        for i in range(screenX):
            if i%50==0 and i!=0:
                 pygame.draw.line(gameWindow,(0,0,0),(i,0),(i,screenX),1)
                 pygame.draw.line(gameWindow,(0,0,0),(0,i),(screenX,i),1)
            if i%150==0:
                 pygame.draw.line(gameWindow,(0,0,0),(i,0),(i,screenX),3)
                 pygame.draw.line(gameWindow,(0,0,0),(0,i),(screenX,i),3)
            pygame.draw.rect(gameWindow,(0,0,0),(0,screenX,500,50))

        for i in range(len(board)):
            for j in range(len(board[i])):
                textRender(cubes[i][j],(0,0,0),20+(j*50),20+(i*50),30)
    
        if selected==True and pos[1]<450:
            pygame.draw.rect(gameWindow, (255,0,0),(sel_pos[0]*50,sel_pos[1]*50,50,50),3)
    
    

        pygame.display.flip()
        clock.tick(50)
    
if __name__ == '__main__':
    welcome()