import sqlite3

import pygame
from sys import exit
import config

from os import path


def load_image(name):
    if not path.isfile(path.join(name)):
        print(f"ERROR 01: '{path.join(name)}' not found.")
        exit()
    image = pygame.image.load(path.join(name))
    return image


pygame.init()
size = width, height = config.SIZE_WINDOW
screen = pygame.display.set_mode(size)
image = load_image('background.jpg')
screen.blit(image, (0, 0))
pygame.display.flip()
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


class Account:
    pygame.font.init()
    font_header = pygame.font.Font(config.FONT, 70)
    font = pygame.font.Font(config.FONT, 28)

    def __init__(self):
        self.system_labels()

    def system_labels(self):
        data = self.data_table()
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 745), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)
        self.header = self.font_header.render('Personal Account', True, [0, 0, 0])
        self.picture_user = load_image('user.png')
        screen.blit(self.header, (190, 40))
        #screen.blit(self.picture_user, (100, 200))

        self.name_text = self.font.render(f'Name: {data[0]}', True, [0, 0, 0])
        self.reg_text = self.font.render(f'Date of registration: {data[1]}', True, [0, 0, 0])
        pygame.draw.line(screen, 'black', (300, 250), (510, 250), 3)
        screen.blit(self.name_text, (300, 200))
        screen.blit(self.reg_text, (300, 270))

        self.stat_text = self.font.render('--- Information about games ---', True, [0, 0, 0])
        screen.blit(self.stat_text, (250, 380))

        self.status_text = self.font.render(f'Player level: {data[2]}', True, [0, 0, 0])
        screen.blit(self.status_text, (100, 450))

        self.games = self.font.render(f'All games: {data[4]}', True, [0, 0, 0])
        screen.blit(self.games, (100, 500))

        self.wins = self.font.render(f'Wins: {data[5]}', True, [0, 0, 0])
        screen.blit(self.wins, (100, 550))

        self.lose = self.font.render(f'Lose: {data[-1]}', True, [0, 0, 0])
        screen.blit(self.lose, (100, 600))

        pygame.draw.rect(screen, 'black', (80, 180, 750, 170), 2)

    def data_table(self, value=1):
        self.con = sqlite3.connect('battleship.db')
        self.cur = self.con.cursor()
        values = (value,)
        result = self.cur.execute('SELECT name, date_of_registration, player_level, all_games, wins, lose FROM users WHERE id = ?', values).fetchall()
        self.con.close()
        for elem in result:
            return elem

    def buttons(self):
        self.button = Button(230, 50)
        self.button.draw(330, 700, ' < Back to menu >', self.return_func)

    def return_func(self):
        pass


account = Account()
if __name__ == '__main__':
    running = True
    account.buttons()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                account.buttons()
        pygame.display.flip()