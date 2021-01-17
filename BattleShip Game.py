import pygame
import config

from class_for_buttons import Button

from window_gameinfo import main as info_main
from window_login import main as login_main
from window_signin import main as signin_main
from secondary_functions import load_image, load_music, game_exit

pygame.init()
size = width, height = config.SIZE_WINDOW
screen = pygame.display.set_mode(size)
image = load_image(config.IMAGE_BACKGROUND)
screen.blit(image, (0, 0))
pygame.display.flip()


class Greeting:
    music = load_music()

    def __init__(self):
        self.work = True
        self.button_login = Button()
        self.button_signin = Button()
        self.button_gameinfo = Button()
        self.button_exit = Button()
        self.font = pygame.font.Font(config.FONT, 20)
        self.font_header = pygame.font.Font(config.FONT, 110)
        self.draw()

    def press(self):
        self.button_login.press(500, 230, self.login)
        self.button_signin.press(500, 350, self.signin)
        self.button_gameinfo.press(500, 470, self.gameinfo)
        self.button_exit.press(500, 590, self.exit_game)

    def move(self):
        self.button_login.move(500, 230)
        self.button_signin.move(500, 350)
        self.button_gameinfo.move(500, 470)
        self.button_exit.move(500, 590)

    def draw(self):
        screen.blit(image, (0, 0))
        self.header = self.font_header.render('BattleShip', True, [0, 0, 0])
        self.shadow_header = self.font_header.render('BattleShip', True, config.SILVER_COLOR)
        screen.blit(self.shadow_header, (373, 25))
        screen.blit(self.header, (370, 25))

        self.button_login.draw(500, 230, '< Log in >')
        self.button_signin.draw(500, 350, '< Sign in >')
        self.button_gameinfo.draw(500, 470, '< Game Info >')
        self.button_exit.draw(500, 590, '< Exit >')

    def login(self):
        login_main()

    def signin(self):
        signin_main()

    def gameinfo(self):
        info_main()

    def exit_game(self):
        game_exit()


def main():
    greeting = Greeting()
    greeting.draw()
    while greeting.work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
                greeting.work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                greeting.press()
            if event.type == pygame.MOUSEMOTION:
                greeting.move()
        greeting.draw()
        pygame.display.flip()


main()
