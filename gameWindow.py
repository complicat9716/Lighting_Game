import pygame
from plane_sprites import *

##############################################################
'''Game initialize'''
pygame.init()

# 480*700
# set_mode(resolution=(0,0), flags=0, depth=0) -> surface
screen = pygame.display.set_mode((480, 700))

# Background
background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))

# Hero
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))

# Update images
pygame.display.update()

# refresh rate set up
clock = pygame.time.Clock()

# hero location
hero_rect = pygame.Rect(150, 500, 102, 126)

# creat enemy
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2, 200)

# enemy group
enemy_group = pygame.sprite.Group(enemy, enemy1)

##############################################################
'''Gaming loop'''
while True:
    # code for windows system
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quitting game....")
            pygame.quit()
            quit()

    # gaming loop code
    clock.tick(120)

    # get event
    # event_list = pygame.event.get()
    # if len(event_list) > 0:
    #     print(event_list)

    # Update background
    screen.blit(background, (0, 0))

    # Update the hero location
    hero_rect.y -= 1
    if hero_rect.y < -126:
        hero_rect.y = 700
    screen.blit(hero, hero_rect)

    # enemy methods
    enemy_group.update()
    enemy_group.draw(screen)

    # Update screen
    pygame.display.update()

pygame.quit()