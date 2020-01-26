import pygame
from plane_sprites import *


class PlaneGame(object):
    # game main

    def __init__(self):
        # Initialize the game
        print("Game Initializing...")

        # create the screen
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # create the clock (for refresh rate)
        self.clock = pygame.time.Clock()

        # create the background
        self.__create_sprites()

        # set the timer for enemy
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 500)

        # set the timer for fire
        pygame.time.set_timer(FIRE_EVENT, 100)

    def __create_sprites(self):
        # create backgroud sprites
        background1 = Background()
        background2 = Background(True)

        # create a hero sprites (setup for global usage)
        self.hero = Hero()

        # update as a background group
        self.background_group = pygame.sprite.Group(background1, background2)

        # create an enemy group
        self.enemy_group = pygame.sprite.Group()

        # create a hero group
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("Game Started.")

        while True:
            # refresh rate
            self.clock.tick(FRAME_PER_SEC)

            # events
            self.__event_handler()

            # collision
            self.__check_collision()

            # sprites
            self.__update_sprites()

            # Update screen
            pygame.display.update()

    def __event_handler(self):
        # Handle the quit event
        for event in pygame.event.get():

            # whether the user press the quit botton (mandantory for windows system)
            if event.type == pygame.QUIT:
                print("Quitting game....")
                self.__game_over()

            # whether the time equal the time for create enemy
            elif event.type == CREATE_ENEMY_EVENT:
                # print("Enemy showed up!")

                # add enemy to the enemy group
                self.enemy_group.add(Enemy())

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     while event.type != pygame.KEYUP: (!!!!!!!!!!!!!! infinite loop)
            #         print('hero move right.')

            # whether the time equal the time for fire
            elif event.type == FIRE_EVENT:

                # call the fire function in the hero
                self.hero.fire()

        # keyborad module
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2

        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2

        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speedy = 2

        elif keys_pressed[pygame.K_UP]:
            self.hero.speedy = -2

        else:
            self.hero.speed = 0
            self.hero.speedy = 0

    def __check_collision(self):
        # Check for the collision

        # bullet destroy enemy
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group,
                                   True, True)

        # enemy destroy hero
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group,
                                              True)

        if len(enemies) > 0:
            self.hero.kill()
            print("Quitting game....")
            self.__game_over()

    def __update_sprites(self):
        # update the sprites group on the screen
        self.background_group.update()
        self.background_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        # game over method
        print("Game Over!")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # set the file as main
    game = PlaneGame()
    game.start_game()