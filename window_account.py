import sqlite3

import pygame
from sys import exit
import config

from os import path
from button_class import Button

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

class Account:
    pygame.font.init()
    font_header = pygame.font.Font(config.FONT, 70)
    font = pygame.font.Font(config.FONT, 28)

    def __init__(self):
        self.system_labels()

    def draw(self):
        self.button = Button(230, 50)
        data = self.data_table()
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 745), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)
        self.header = self.font_header.render('Personal Account', True, [0, 0, 0])
        self.picture_user = load_image('user.png')
        screen.blit(self.header, (190, 40))
        screen.blit(self.picture_user, (120, 200))

        self.name_text = self.font.render(f'Name: {config.USER_NAME}', True, [0, 0, 0])
        pygame.draw.line(screen, 'black', (300, 250), (510, 250), 3)
        screen.blit(self.name_text, (300, 200))

        try:
            self.stat_text = self.font.render('--- Information about games ---', True, [0, 0, 0])
            screen.blit(self.stat_text, (250, 380))

            self.status_text = self.font.render(f'Player level: {data[0]}', True, [0, 0, 0])
            screen.blit(self.status_text, (100, 450))

            self.games = self.font.render(f'All games: {data[1]}', True, [0, 0, 0])
            screen.blit(self.games, (100, 500))

            self.wins = self.font.render(f'Wins: {data[2]}', True, [0, 0, 0])
            screen.blit(self.wins, (100, 550))

            self.lose = self.font.render(f'Lose: {data[-1]}', True, [0, 0, 0])
            screen.blit(self.lose, (100, 600))
        except TypeError:
            print('ERROR 02: Incorrect data entered.')

        pygame.draw.rect(screen, 'black', (80, 180, 750, 170), 2)

    def data_table(self):
        self.con = sqlite3.connect('battleship.db')
        self.cur = self.con.cursor()
        try:
            result = self.cur.execute(
                'SELECT player_level, all_games, wins, lose FROM users WHERE name = ?',
                (config.USER_NAME,)).fetchall()
            self.con.close()
            for elem in result:
                return elem
        except TypeError:
            print('ERROR 02: Incorrect data entered.')

    def press(self):
        self.button.press(330, 700, ' < Back to menu >', self.to_menu)

    def move(self):
        self.button.move(330, 700)

    def to_menu(self):
        global work
        work = False


def main():
    global work
    work = True
    account = Account()
    account.draw()
    while work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                account.press()
            if event.type == pygame.MOUSEMOTION:
                account.move()
        account.draw()
        pygame.display.flip()
