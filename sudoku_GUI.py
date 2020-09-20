import pygame

pygame.init()

screenX,screeeY=450,450

gameWindow=pygame.display.set_mode((screenX,screeeY))

pygame.display.set_caption("Sudoku Solver")


board=[
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]

key=None
selected=False
cubes=[[' ' for i in range(9)] for j in range(9)]


def drawRect(pos):
    x=pos[0]//50
    y=pos[1]//50
    return (x,y) 

def textRender(text,color,x,y,size):
    font=pygame.font.SysFont(None,size)
    screenText=font.render(text,True,color)
    gameWindow.blit(screenText,(x,y))

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

exit_game=False

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
                pass

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
