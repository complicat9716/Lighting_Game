from random import *
import pygame

# Screen size
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# refresh rate
FRAME_PER_SEC = 120

# userevent constant for enemy
CREATE_ENEMY_EVENT = pygame.USEREVENT

# userevent constant for fire
FIRE_EVENT = pygame.USEREVENT + 1


# Game sprite class for reading image and give a speed
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1, X=0):

        super().__init__()

        # class initialization for sprites to loading the images
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.speed = speed

    def update(self):

        self.rect.y += self.speed


# Background class inheritant from sprite class
class Background(GameSprite):
    def __init__(self, is_alt=False):

        # pass the background image location to the sprites class
        super().__init__("./images/background.png")

        # put the second image on the top of the first image
        if is_alt:
            self.rect.y = -self.rect.height

    # rewrite the update method for the background sprites
    def update(self):

        # inheritant the update method
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


# Enemy class inheritant from sprite class
class Enemy(GameSprite):
    def __init__(self):
        # update the image address for enemy
        super().__init__("./images/enemy1.png", randint(1, 5),
                         randint(0, SCREEN_RECT.width - 57))
        self.rect.bottom = 0

    # rewrite the update method for enemy
    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            # print("out of screen!")

            # delete the enemy
            self.kill()

    # rewrite the delete method
    def __del__(self):
        #print("Enemy died! %s" % self.rect)
        pass


# Hero class inheritant from sprite class
class Hero(GameSprite):
    def __init__(self, speedy=0):
        # inheritant from parent (with zero speed)
        super().__init__('./images/me1.png', 0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.speedy = speedy

        # create a bullet group
        self.bullet_group = pygame.sprite.Group()

    def update(self):

        self.rect.x += self.speed
        self.rect.y += self.speedy

        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.y <= 0:
            self.rect.y = 0

        if self.rect.bottom >= SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):

        for i in (-4, -3, -2, -1, 0, 1, 2, 3, 4):
            # create a bullet
            b = Bullet()

            # specify the bullet location
            b.rect.bottom = self.rect.y - 20

            b.rect.centerx = self.rect.centerx + 20 * i

            # add the bullet to the bullet group
            self.bullet_group.add(b)


# Bullet class inheritant from sprite class
class Bullet(GameSprite):
    def __init__(self, speed_x=0):
        # inheritant from parent (with -1 speed)
        super().__init__('./images/bullet1.png', -1)

        self.speed_x = speed_x

    def update(self):
        super().update()

        self.rect.x += self.speed_x

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print('Bullet deleted.')
        pass