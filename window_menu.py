import pygame
import config

from sys import exit
from os import path


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
clock = pygame.time.Clock()


class Button:
    pygame.init()
    button_sound = pygame.mixer.Sound(config.BUTTON_SOUND)
    font = pygame.font.Font(config.FONT, 22)

    def __init__(self, width=350, height=50):
        self.width = width
        self.heigth = height
        self.inactive_color = config.SILVER_COLOR
        self.active_color = config.DARK_SILVER_COLOR

    def draw(self, x, y, message, function=None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed(3)

        if x < self.mouse[0] < x + self.width and y < self.mouse[1] < y + self.heigth:
            pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.heigth))
            pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)
            if self.click[0] is True:
                pygame.mixer.Sound.play(Button.button_sound)
                pygame.time.delay(300)
                self.click_button(function)

        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.heigth))
            pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)
        self.print_text(message, x + 20, y + 10)

    def print_text(self, message, x, y):
        self.text = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text, (x, y))

    def click_button(self, function):
        if function is not None:
            function()


class Menu:
    pygame.font.init()
    font = pygame.font.Font('font.ttf', 42)

    def __init__(self):
        self.system_labels()
        self.buttons()

    def system_labels(self):
        pygame.draw.rect(screen, config.SILVER_COLOR, (0, 20, width, 80))
        self.text = self.font.render('MAIN MENU', True, [0, 0, 0])
        screen.blit(self.text, (300, 35))

    def buttons(self):
        self.button_size = (260, 60)
        self.account_button = Button()
        self.account_button.draw(width - (self.button_size[0] + self.button_size[0] // 2), 200,
                                 '< Personal Account >', self.opening_an_account)

        self.game_button = Button()
        self.game_button.draw(width - (self.button_size[0] + self.button_size[0] // 2), 300,
                              '< New Game >', self.turning_on_the_game)
        self.setting_button = Button()
        self.setting_button.draw(width - (self.button_size[0] + self.button_size[0] // 2), 400,
                                 '< Settings >', self.opening_setting)

        self.high_score_table_button = Button()
        self.high_score_table_button.draw(width - (self.button_size[0] + self.button_size[0] // 2),
                                          500,
                                          '< Table of Records >', self.high_score_table)

        self.logout_button = Button()
        self.logout_button.draw(width - (self.button_size[0] + self.button_size[0] // 2), 600,
                                '< Logout >', self.logout)

        self.help_button = Button(55, 50)
        self.help_button.draw(10, 750, '?', self.help)

    def opening_an_account(self):
        pass  # class Account

    def turning_on_the_game(self):
        pass  # class game BattleShip

    def opening_setting(self):
        pass  # class Settings

    def high_score_table(self):
        pass  # class High Score Table

    def logout(self):
        pass  # class Greeting

    def help(self):
        pass  # open help


if __name__ == '__main__':
    running = True
    menu = Menu()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                menu.buttons()
        pygame.display.flip()
