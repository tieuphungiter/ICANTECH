#buoi 02
"""
========= Buổi 1 ======
1. Khởi tạo màn hình game
2. Tạo con rắn
3. Tạo chuyển động cho con rắn

========= Buổi 2 ======
1. Tạo con mồi
2. Tăng độ dài cho con rắn sau khi ăn mồi

========= Buổi 3 ======
1. Sự kiến rắn đâm vào biên + thông báo
2. Sự kiện rắn cắn vào bản thân + thông báo
3. Ghi nhận điểm số 
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
#kích thước khởi tạo của đầu con rắn
snake_block = 10

#tạo độ khởi tạo của đầu con rắn
x_head = 300
y_head = 200
x_head_change = 0
y_head_change = 0
clock = pygame.time.Clock()

#Khai báo Font chữ
arialFont = pygame.font.SysFont("Arial",30)
    
#Khai bao cho con moi
randFoodX = random.randrange(0, screen_width - 10)
surplusFoodX = randFoodX % 10
foodx = round(randFoodX - surplusFoodX)
randFoodY = random.randrange (0, screen_height - 10)
surplusFoodY = randFoodY % 10
foody = round(randFoodY - surplusFoodY)
#kiểm tra lại tọa độ con mồi
print('foodx, foody', foodx, foody)
"""
Khai báo một danh sách snake_list để lưu tạo độ các khúc cấu thành con rắn.
Biến snake_length lưu độ dài của con rắn, mặc định là 1
"""
snake_list = []
snake_length = 1
"""hàm show_snake() để vẽ con rắn lên màn hình và cập nhật độ dài sau khi con rắn ăn mồi 
thay cho câu lệnh vẽ thông thường
"""
#Khai bao cac DEF
def show_snake(snake_block, snake_list): 
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])

#=====Snack 03======
def message(msg,color):
    mesg = arialFont.render(msg, True, color)
    textRect = mesg.get_rect()
    textRect.center = (300,300)
    screen.blit(mesg,textRect)

"""
Đối số đầu tiên là một chuỗi một dòng, đối số thứ hai biểu diễn antialias. 
Nếu được đặt thành False, hình ảnh được hiển thị là hình ảnh 8 bit và 24 bit nếu là true. 
Cũng có thể sử dụng đối số màu nền tùy chọn.
""" 
def show_score(score):
    value = arialFont.render("Score: "+str(score), True, BLACK)
    screen.blit(value,[0,0])
    
game_close = False

while True:
    #===== START Snack 03======
    while game_close == True:  
        screen.fill(BLUE)
        message("Thua roi! Bam phim cach de choi lai", RED)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_close = False
                    snake_list = []
                    snake_length = 1
                    x_head = 300
                    y_head = 200           
    # Kiểm tra va trạm
    if (x_head >= screen_width) or (x_head < 0) or (y_head >= screen_height) or ( y_head < 0):
        game_close = True 
    
    #===== END Snack 03======
                 
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
    #pygame.draw.rect(screen,BLACK,[x_head,y_head,snake_block,snake_block])
    """
    vì ở đây chúng ta gọi lại hàm show_snake để hiện thị con rắn nên câu lệnh vẽ con rắn ở trên không còn cần thiết
    """
    show_snake(snake_block, snake_list)
    #Tạo cục mồi
    pygame.draw.rect(screen,BLUE,[foodx,foody,snake_block,snake_block])
    #Cập nhật tọa độ đầu cho con rắn
    x_head += x_head_change
    y_head += y_head_change
    
    #phần cấu hình tăng độ dài cho rắn
    snake_head = []
    snake_head.append(x_head)
    snake_head.append(y_head)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    
    # goi lai ham ve bang diem
    show_score(snake_length - 1)
    
    for x in snake_list[:-1]:
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
    
    #cấu hình FPS và update display
    pygame.display.update()
    clock.tick(8)
    