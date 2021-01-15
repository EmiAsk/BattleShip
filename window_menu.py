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
            if self.click[0] is True and function is not None:
                pygame.mixer.Sound.play(Button.button_sound)
                pygame.time.delay(300)
                function()

        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.heigth))
            pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)
        self.print_text(message, x + 20, y + 10)

    def print_text(self, message, x, y):
        self.text = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text, (x, y))


class Menu:
    pygame.font.init()
    font = pygame.font.Font('font.ttf', 42)
    font_header = pygame.font.Font(config.FONT, 110)

    def __init__(self):
        self.system_labels()
        self.buttons()

    def system_labels(self):
        self.text = self.font_header.render('MENU', True, [0, 0, 0])
        self.text_2 = self.font_header.render('MENU', True, config.SILVER_COLOR)

        screen.blit(self.text_2, (503, 25))
        screen.blit(self.text, (500, 25))

    def buttons(self):
        self.account_button = Button()
        self.account_button.draw(500, 230,
                                 '< Personal Account >', self.opening_an_account)

        self.game_button = Button()
        self.game_button.draw(500, 350, '< New Game >', self.turning_on_the_game)

        self.high_score_table_button = Button()
        self.high_score_table_button.draw(500, 470, '< Table of Records >', self.high_score_table)

        self.logout_button = Button()
        self.logout_button.draw(500, 590, '< Logout >', self.logout)

    def opening_an_account(self):
        pass  # class Account

    def turning_on_the_game(self):
        pass  # class game BattleShip

    def high_score_table(self):
        pass  # class High Score Table

    def logout(self):
        pass  # class Greeting

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
