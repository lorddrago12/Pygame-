import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Sprite")

BLUE = (173, 216, 230)

# Load sprite
player_image = pygame.image.load("C:/Users/Hp/Downloads/Balloon.png").convert_alpha()

# Sprite position
player_x = 100
player_y = 100
player_speed = 0.8

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press detection
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    if player_x < 0:
        player_x = 0
    if player_y < 0:
        player_y = 0
    if player_x > 800 - player_image.get_width():
        player_x = 800 - player_image.get_width()
    if player_y > 600 - player_image.get_height():
        player_y = 600 - player_image.get_height()

    player_image = pygame.image.load("C:/Users/Hp/Downloads/Bullet.png").convert_alpha() 

    # Clear screen
    screen.fill(BLUE)

    # Draw sprite at UPDATED position
    screen.blit(player_image, (player_x, player_y))

    pygame.display.flip()

pygame.quit()
