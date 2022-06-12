import pygame
import random
pygame.init()
start=False
screen=pygame.display.set_mode((800,400))

iX1=random.randint(100,750)
iY1=random.randint(50,350)
pygame.draw.rect(screen,(255,255,255),pygame.Rect(iX1,iY1,15,15))
iX=random.randint(100,750)
iY=random.randint(50,350)
pygame.draw.rect(screen,(255,0,0),pygame.Rect(iX,iY,15,15))
font=pygame.font.Font('Hey Comic.ttf',32)
screen.blit((font.render("press and arrow key to get started in that direction",True,(0,255,0))),(10,10))

class body:
    def __init__(self,x,y):
        self.x=x
        self.y=y
xVel=0;
yVel=0;
bdx=0;
bdy=0;

def main():
    global iX1
    global iY1
    global iX
    global iY
    global xVel
    global yVel
    global bdx
    global bdy
    global start
    bd=[]
    oldX=[]
    oldY=[]
    length=1
    score=0
    HighScore=0
    run=True
    clock=pygame.time.Clock()
    touched=False
    while run: 
        for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    start=True
                    if(event.key == pygame.K_RETURN):
                        touched=False
                        score=0
                        bd=[]
                        oldX=[]
                        oldY=[]
                        length=1
                        screen.fill((0,0,0))
                        iX1=random.randint(100,750)
                        iY1=random.randint(50,350)
                        pygame.draw.rect(screen,(255,255,255),pygame.Rect(iX1,iY1,15,15))
                        iX=random.randint(100,750)
                        iY=random.randint(50,350)
                        pygame.draw.rect(screen,(255,0,0),pygame.Rect(iX,iY,15,15))
                        screen.blit((font.render("press and arrow key to get started in that direction",True,(0,255,0))),(10,10))
                        start=False
                    
                if event.type==pygame.QUIT:
                    run=False
        if(start):
            bdx=xVel
            bdy=yVel
            clock.tick(30)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run =False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xVel=-10
                    yVel=0
                elif event.key == pygame.K_RIGHT:
                    xVel=10
                    yVel=0
                elif event.key == pygame.K_UP:
                    yVel=-10
                    xVel=0
                elif event.key == pygame.K_DOWN:
                    yVel=10
                    xVel=0
            if((abs(iX-iX1)<=20)and(abs(iY-iY1)<=20)):
                length+=1
                bd.append(body(iX1,iY1))
                score=score+1
                iX=random.randint(100,750)
                iY=random.randint(50,350)

            screen.fill((0,0,0))
            oldX.append(iX1)
            oldY.append(iY1)
            if(len(oldX)>length):
                del oldX[0]
            if(len(oldY)>length):
                del oldY[0]
            iX1+=xVel
            iY1+=yVel
            for i in range(len(bd)):
                bd[i].x=oldX[i]
                bd[i].y=oldY[i]
                
            font=pygame.font.Font('Hey Comic.ttf',32)
            screen.blit((font.render("Score"+str(score),True,(0,255,0))),(10,10))
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(iX,iY,15,15))
            pygame.draw.rect(screen,(255,255,255),pygame.Rect(iX1,iY1,15,15))

            for part in bd:
                
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(part.x,part.y,15,15))
                if((abs(part.x-iX1)<=5)and(abs(part.y-iY1)<=5)):
                    touched=True
            if(((iX1>799)or(iX1<1))or((iY1>399)or(iY1<1))or(touched)):
                font=pygame.font.Font('Hey Comic.ttf',32)
                if(score>HighScore):
                    HighScore=score
                screen.fill((0,0,0))
                screen.blit((font.render("Game Over \nFinal Score: "+str(score),True,(0,255,0))),(10,10))
                screen.blit((font.render("High Score"+str(HighScore),True,(0,255,0))),(10,40))
                screen.blit((font.render("press enter to restart",True,(0,255,0))),(10,70))
                start=False
                
        
        
        
        
        
        pygame.display.update()
    pygame.quit()
if __name__=="__main__":
    main()