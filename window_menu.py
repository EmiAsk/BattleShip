import pygame
import config

from sys import exit
from os import path

from button_class import Button
from window_account import main as main_account


def load_image(name):
    if not path.isfile(path.join(name)):
        print(f"ERROR 01: '{path.join(name)}' not found.")
        exit()
    image = pygame.image.load(path.join(name))
    return image


pygame.init()
size = width, height = config.SIZE_WINDOW
image = load_image(config.IMAGE_BACKGROUND)
screen = pygame.display.set_mode(size)
screen.blit(image, (0, 0))


class Menu:
    def __init__(self):
        self.account_button = Button()
        self.game_button = Button()
        self.high_score_table_button = Button()
        self.logout_button = Button()
        self.font = pygame.font.Font(config.FONT, 42)
        self.header_font = pygame.font.Font(config.FONT, 110)
        self.draw()

    def press(self):
        self.account_button.press(500, 230, self.opening_an_account)
        self.game_button.press(500, 350, self.turning_on_the_game)
        self.high_score_table_button.press(500, 470, self.high_score_table)
        self.logout_button.press(500, 590, self.logout)

    def move(self):
        self.account_button.move(500, 230)
        self.game_button.move(500, 350)
        self.high_score_table_button.move(500, 470)
        self.logout_button.move(500, 590)

    def draw(self):
        screen.blit(image, (0, 0))
        self.header = self.header_font.render('MENU', True, [0, 0, 0])
        self.shadow_header = self.header_font.render('MENU', True, config.SILVER_COLOR)

        screen.blit(self.shadow_header, (503, 25))
        screen.blit(self.header, (500, 25))

        self.account_button.draw(500, 230,
                                 '< Personal Account >', self.opening_an_account)
        self.game_button.draw(500, 350, '< New Game >', self.turning_on_the_game)
        self.high_score_table_button.draw(500, 470, '< Table of Records >', self.high_score_table)
        self.logout_button.draw(500, 590, '< Logout >', self.logout)

    def opening_an_account(self):
        main_account()

    def turning_on_the_game(self):
        pass  # class game BattleShip

    def high_score_table(self):
        pass  # class High Score Table

    def logout(self):
        global work
        work = False


def main():
    work = True
    menu = Menu()
    while work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu.press()
            if event.type == pygame.MOUSEMOTION:
                menu.move()
        menu.draw()
        pygame.display.flip()
