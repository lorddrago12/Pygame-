import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Sprite")

BLUE = (173, 216, 230)

# Load sprites
player_image = pygame.image.load("C:/Users/Hp/Downloads/Balloon.png").convert_alpha()
enemy_image = pygame.image.load("C:/Users/Hp/Downloads/Bullet.png").convert_alpha()
jet_image = pygame.image.load("C:/Users/Hp/Downloads/Jet.png").convert_alpha()   # third sprite

# Player position
player_x = 100
player_y = 100
player_speed = 0.5

# Enemy (falls from below)
enemy_x = random.randint(0, 800 - enemy_image.get_width())
enemy_y = 650
enemy_speed = 0.5

# Jet (chasing enemy)
jet_x = 600
jet_y = 100
jet_speed = 0.2

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_RIGHT]: player_x += player_speed
    if keys[pygame.K_LEFT]: player_x -= player_speed
    if keys[pygame.K_UP]: player_y -= player_speed
    if keys[pygame.K_DOWN]: player_y += player_speed

    # Player boundary
    player_x = max(0, min(player_x, 800 - player_image.get_width()))
    player_y = max(0, min(player_y, 600 - player_image.get_height()))

    # Enemy from bottom
    enemy_y -= enemy_speed
    if enemy_y < -enemy_image.get_height():
        enemy_y = 650
        enemy_x = random.randint(0, 800 - enemy_image.get_width())

    # Jet FOLLOWING player
    if jet_x < player_x: jet_x += jet_speed
    if jet_x > player_x: jet_x -= jet_speed
    if jet_y < player_y: jet_y += jet_speed
    if jet_y > player_y: jet_y -= jet_speed

    # Draw
    screen.fill(BLUE)
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))
    screen.blit(jet_image, (jet_x, jet_y))

    pygame.display.flip()

pygame.quit()
