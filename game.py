import pygame

# 設定螢幕尺寸
screen = pygame.display.set_mode((900, 500))

# Title and Icon
pygame.display.set_caption("My game")
icon = pygame.image.load("01__Block.png")
pygame.display.set_icon(icon)

# 玩家圖片
playerImg = pygame.image.load("01__Block.png")
# 改變大小
playerImg = pygame.transform.scale(playerImg, (50, 50))

playerx = 0
playery = 0
playerychange = 0


def player():
    screen.blit(playerImg, (playerx, playery))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerychange -= 0.5
            if event.key == pygame.K_DOWN:
                playerychange += 0.5
        if event.type == pygame.KEYUP:
            playerychange = 0

    screen.fill((0, 255, 0))
    player()
    playery += playerychange

    pygame.display.update()

print(event)
