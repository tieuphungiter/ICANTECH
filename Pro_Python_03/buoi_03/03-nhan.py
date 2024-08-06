#Nhan
# buoi 1
"""
Buổi 1
1. Khởi tạo
2. Tạo con rắn
3. Tạo event chuyển động cho rắn
"""
import pygame, sys, random
from pygame.locals import QUIT

pygame.init()
scr_x = 400
scr_y = 300
screen = pygame.display.set_mode((scr_x, scr_y))
x_head=100 
y_head=200
x_ch=0
y_ch=0
snake_block = 10
clock = pygame.time.Clock()
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
CYAN = (0,255,255)
pygame.display.set_caption('Ran San Moi')

#vi tri con moi
rand_x_food = random.randint(0,scr_x-10)
sp_x_food = rand_x_food % 10
x_food = round(rand_x_food - sp_x_food)
rand_y_food = random.randint(0,scr_y-10)
sp_y_food = rand_y_food % 10
y_food = round(rand_y_food - sp_y_food)

snake_list = []
snake_length = 1

def snake(x,y):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block] )
    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x_ch=0
                y_ch=-10
            elif event.key == pygame.K_DOWN:
                x_ch=0
                y_ch=10
            elif event.key == pygame.K_LEFT:
                x_ch=-10
                y_ch=0
            elif event.key == pygame.K_RIGHT:
                x_ch=10
                y_ch=0
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED,[x_food, y_food, snake_block, snake_block])
    x_head+=x_ch
    y_head+=y_ch
    
    snake_head = []
    snake_head.append(x_head)
    snake_head.append(y_head)
    snake_list.append(snake_head)
    if (len(snake_list) > snake_length):
        del snake_list[0]
    snake(snake_block, snake_list)

    for x in snake_list[:-1]:
        if x == snake_head:
            game_close = True
    if x_head == x_food and y_head == y_food:
        rand_x_food = random.randint(0,scr_x-10)
        sp_x_food = rand_x_food % 10
        x_food = round(rand_x_food - sp_x_food)
        rand_y_food = random.randint(0,scr_y-10)
        sp_y_food = rand_y_food % 10
        y_food = round(rand_y_food - sp_y_food)
        snake_length += 1

    pygame.display.update()
    clock.tick(5)
    