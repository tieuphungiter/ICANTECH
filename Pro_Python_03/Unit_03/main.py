
"""
Đã fix lỗi kiểm tra va chạm
#Viet Duc
"""

import pygame, sys, random 

#pygame.init()

WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

screen_width = 600
screen_height = 400
title = 'Rắn săn mồi check'
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)

snake_block = 10

x_head = 300
y_head = 200

x_head_change = 0
y_head_change = 0

clock = pygame.time.Clock()

arialFont = pygame.font. SysFont("Arial", 30)

def message(msg, color):
    mesg = arialFont.render(msg, True, color)
    textRect = mesg.get_rect()
    textRect.center = (300, 200)
    screen.blit(mesg, textRect)


randFoodX = random.randrange(0, screen_width - 10)
surplusFoodX = randFoodX % 10
foodx = round(randFoodX - surplusFoodX)
randFoodY = random.randrange (0, screen_height - 10)
surplusFoodY = randFoodY % 10
foody = round(randFoodY - surplusFoodY)
print('foodx, foody', foodx, foody)

snake_list = []
snake_length = 5
#snake_length = 1
def show_snake(snake_block, snake_list): 
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])

def show_score(score):
    value = arialFont.render("Score: " + str(score), True, BLACK)
    screen.blit(value, [0, 0])


game_close = False
while True:
    while game_close == True:
        screen.fill(BLUE)
        message("Thua rui! Bam phim cach choi lai", RED)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_close = False
                    snake_list = []
                    snake_length = 5
                    x_head = 300
                    y_head = 200
                    
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_head_change = -10
                y_head_change = 0
            elif event.key == pygame.K_RIGHT:
                x_head_change = 10
                y_head_change = 0
            elif event.key == pygame.K_UP:
                y_head_change = -10
                x_head_change = 0
            elif event.key == pygame.K_DOWN:
                y_head_change = 10
                x_head_change = 0

    if (x_head >= screen_width) or (x_head < 0) or (y_head >= screen_height) or (y_head < 0):
        game_close = True

    screen.fill(WHITE)

    x_head += x_head_change
    y_head += y_head_change
    
    #Tạo con rắn
    pygame.draw.rect(screen,BLACK,[x_head,y_head,snake_block,snake_block])
  
    #Tạo cục mồi
    pygame.draw.rect(screen,BLUE,[foodx,foody,snake_block,snake_block])

    snake_head = []
    snake_head.append(x_head)
    snake_head.append(y_head)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]
        show_snake(snake_block,snake_list)
    # =====
    # =
    # vì em khởi tạo snake_head = 5 nên khi kiểm tra phải mặc định snake_list đã có 5 giá trị
    for x in snake_list[:-5]:
        if x == snake_head:
            game_close = True

    if x_head == foodx and y_head == foody:
        randFoodX = random.randrange(0,screen_width - 10)
        surplusFoodX = randFoodX % 10
        foodx = round(randFoodX - surplusFoodX)
        randFoodY = random.randrange(0, screen_height - 10)
        surplusFoodY = randFoodY % 10
        foody = round(randFoodY - surplusFoodY)
        snake_length += 1

    show_score(snake_length - 1)
    pygame.display.update()
    clock.tick(8)
