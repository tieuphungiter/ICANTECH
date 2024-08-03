#buoi 01
"""
========= Buổi 1 ======
1. Khởi tạo màn hình game
2. Tạo con rắn
3. Tạo chuyển động cho con rắn

"""
#import các thư viện
import pygame, sys, random 
#gọi câu lệnh khởi tạo
pygame.init()
#Khai báo các giá trị màu
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
#Khởi tạo kích thước khung hình
screen_width = 600
screen_height = 400
title = "Rắn săn mồi"
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)
#kích thước khởi tạo của đầu con rắn hình vuông
snake_block = 10
#tạo độ khởi tạo của đầu con rắn
x_head = 300
y_head = 200
#Khai báo 2 biến xác định sự thay đổi tọa độ của rắn
x_head_change = 0
y_head_change = 0

clock = pygame.time.Clock()

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
                elif event.key == pygame.K_UP:
                    y_head_change = -10
                    x_head_change = 0
                elif event.key == pygame.K_DOWN:
                    y_head_change = 10
                    x_head_change = 0
                    
    #===== Khung vực vẽ đối tượng lên khung hình
    #tạo nền cho khung hình
    screen.fill(WHITE)
    #Tạo con rắn
    pygame.draw.rect(screen,BLACK,[x_head,y_head,snake_block,snake_block])
    #Cập nhật tọa độ đầu cho con rắn
    x_head += x_head_change
    y_head += y_head_change
    
    #cấu hình FPS và update display
    pygame.display.update()
    clock.tick(8)
    