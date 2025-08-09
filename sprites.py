import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Let's Add Sprites")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_size = 50
player_x = (SCREEN_WIDTH - player_size) // 2
player_y = (SCREEN_HEIGHT - player_size) // 2
player_speed = 5


enemy_size = 70
enemy_x = 100
enemy_y = 100

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed


    player_x = max(0, min(player_x, SCREEN_WIDTH - player_size))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - player_size))
    screen.fill(WHITE)

    
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, BLUE, (enemy_x, enemy_y, enemy_size, enemy_size))

    pygame.display.flip()

pygame.quit()