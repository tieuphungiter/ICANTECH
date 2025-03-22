#Du an gam lat anh
import pygame,random
#Khởi tạo
pygame.init()
#Màn hình
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("game lật")
#màu 
PINK = (255,0,255)
BACKGROUND_COLOR = (255,255,255)
TILE_COLOR = (0,0,0)
#phông chữ
font = pygame.font.SysFont(None,48)
images = []
for i in range (1,9):
  image = pygame.image.load(f"img/img{i}.png")
  images.append(image)
  images.append(image)

random.shuffle(images)
TILE_SIZE = 64
GRID_WIDTH = 4
GRID_HEIHT = 4 
PADDING = 20
grid_x = (SCREEN_WIDTH-GRID_WIDTH * (TILE_SIZE + PADDING)  +PADDING) //2
grid_y = (SCREEN_HEIGHT-GRID_HEIHT * (TILE_SIZE + PADDING)  +PADDING) //2
tiles = []
for row in range (GRID_HEIHT):
  for col in range (GRID_WIDTH):
    image = images.pop()
    x = grid_x + col * (TILE_SIZE + PADDING)
    #y = grid_y + col * (TILE_SIZE + PADDING)
    y = grid_y + row * (TILE_SIZE + PADDING)
    tile = (x,y,TILE_SIZE,TILE_SIZE, image,False)
    tiles.append(tile)

score = 0
flips_tiles = []
running = True 
while running :
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      for i, tile in enumerate(tiles):
        if tile[0] < pos[0] < tile[0] + TILE_SIZE and \
           tile[1] < pos[1] < tile[1] + TILE_SIZE and \
           not tile[5]:
          tile = tile[:5] + (True,)
          tiles[i] = tile 
          flips_tiles.append(i)
          if len(flips_tiles) == 2 :
            if tiles[flips_tiles[0]][4] == tiles[flips_tiles[1]][4]:
              score +=1
              flips_tiles = []
            else:
              pygame.time.wait(1000)
              for i in flips_tiles:
                #tile = tiles[1][:5] = (False,)
                tile = tiles[i][:5] + (False,)
                tiles[i] = tile
              flips_tiles = []
    screen.fill(BACKGROUND_COLOR)
    for tile in tiles:
      pygame.draw.rect(screen, TILE_COLOR, tile[:4])
      if tile[5]:
        screen.blit(tile[4],tile[:2])

    score_text = font.render(f"Score : {score}", True , TILE_COLOR)
    screen.blit(score_text , (20,20))

    pygame.display.flip()
    win = False 
    if score == 8 :
      win = True
    if win :
      text = font.render("HOW CAN YOU DO THIS" , True, PINK)
      text_rect = text.get_render(center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2))  
      screen.blit(text,text_rect)
      pygame.display.flip()

pygame.quit()
        