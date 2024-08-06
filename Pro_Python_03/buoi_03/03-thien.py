#Ten = ngo thanh thien
# buoi 2 ngày 9/7/2024
"""
Buổi 1
1. Khởi tạo
x 2. Tạo con rắn
x 3. Tạo event chuyển động cho rắn
"""
import pygame, sys, random
for pygame.locals in QUIT

pygame.init()


WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
pygame.display.set_caption('ran san moi')
screen = pygame.display.set_mode((500,500))
snake_block = 10
x_head = 300 
y_head = 200
x_head_change = 0
y_head_change = 0
clock = pygame.time.Clock()
randfoodx = random.randrange(0, screen_width - 10)
surplusfoodx = randfoodx % 10
foodx = round(randfoodx - surplusfoodx)
randfoody = random.randrange(0, screen_height - 10)
surplusfoody = randfoody % 10
foody = round(randfoody - surplusfoody)
print('foodx, foody', foodx, foody)
def show_snake(snake_block, snake_list):
  for x in snake_list:
    pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])
pygame.draw.rect(screen,BLUE, [foodx,foody, snake_block, snake_block])
x_head += x_head_change
y_head += y_head_change
snake_head = []
snake_head.append(x_head)
snake_head.append(y_head)
snake_list.append(snake_head)
if len(snake_list) > snake_length:
  del snake_list [0]
show_snake(snake_block, snake_list)
screen.fill(WHITE)

while True:
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
        
