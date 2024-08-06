#Minh-7/16/24
import pygame,sys
import random
pygame.init()

screen=pygame.display.set_mode((600,400))
RED=(255,0,0)
BLACK=(0,0,0)
BLUE=(0,0,255)
WHITE=(255,255,255)

#snake
block=10
x=300
y=200
x_change=0
y_change=0
clock=pygame.time.Clock()
foodX=random.randrange(0,590,10)
foodY=random.randrange(0,390,10)
#location for snake parts
snake_list=[]
snake_length=1

def showsnake(block,snake_list):
  for i in snake_list:
    pygame.draw.rect(screen,RED,[i[0],i[1],block,block])
    
running= True
while running:
  for event in pygame.event.get():
        if event.type==pygame.QUIT:
          running=False
          pygame.quit()
          sys.exit()
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_LEFT:
            x_change= -10
            y_change=0
          elif event.key==pygame.K_RIGHT:
            x_change=10
            y_change=0
          elif event.key==pygame.K_UP:
            x_change=0
            y_change=-10
          elif event.key==pygame.K_DOWN:
            x_change=0
            y_change=10
            
  screen.fill(BLACK)
  food=pygame.draw.rect(screen,BLUE,[foodX,foodY,block,block])
  
  # snake=pygame.draw.rect(screen,RED,[x,y,block,block])
  

  x+=x_change
  y+=y_change

  head=[]
  head.append(x)
  head.append(y)
  snake_list.append(head)
  
  if len(snake_list)>snake_length:
    del snake_list[0]
  
  showsnake(block,snake_list)
  for i in snake_list[:-1]:
    if i==head:
      running=False
      screen.fill(WHITE)
      
  if x==foodX and y==foodY:
    snake_length+=1
    foodX=random.randrange(0,590,10)
    foodY=random.randrange(0,390,10)



  
  clock.tick(8)
  pygame.display.update()
    