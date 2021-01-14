import pygame
from sys import exit
import config
import sqlite3

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
        self.text = Button.font.render(message, True, [0, 0, 0])
        screen.blit(self.text, (x, y))


class Table:
    pygame.font.init()
    font_header = pygame.font.Font(config.FONT, 70)
    font = pygame.font.Font(config.FONT, 28)

    def __init__(self):
        self.draw()
        self.filling_table()

    def draw(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 745), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)
        self.header = self.font_header.render('Table of records', True, [0, 0, 0])
        screen.blit(self.header, (200, 40))

        for row in range(12):
            pygame.draw.rect(screen, 'black', (40, 180 + (row * 40), 820, 40), 2)
        for column in range(2, 6):
            pygame.draw.line(screen, 'black', (100 + 100 * column, 180), (100 + 100 * column, 660),
                             2)
            screen.blit(self.font.render(config.TABLE_HEADERS[column - 1], True, [0, 0, 0]),
                        (110 + column * 100, 180))
        screen.blit(self.font.render(config.TABLE_HEADERS[0], True, [0, 0, 0]), (110, 180))

    def filling_table(self):
        connect = sqlite3.connect('battleship.db')
        cursor = connect.cursor()
        self.request = cursor.execute('SELECT * FROM users').fetchall()
        self.table_data = sorted(self.request[:10], key=lambda x: x[4], reverse=True)

        for x in self.table_data:
            self.coefficient = self.table_data.index(x)
            screen.blit(self.font.render(x[1], True, [0, 0, 0]), (50, 220 + 40 * self.coefficient))

            for number in range(3, 8):
                if number == 7:
                    continue
                else:
                    screen.blit(self.font.render(str(x[number]), True, [0, 0, 0]),
                                (10 + 100 * number, 220 + 40 * self.coefficient))
        connect.close()

    def buttons(self):
        self.button = Button(230, 50)
        self.button.draw(330, 700, ' < Back to menu >', self.return_func)

    def return_func(self):
        window_menu.main()


def main():
    table = Table()
    work = True
    table.draw()
    while work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                work = False
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
                table.buttons()
        pygame.display.flip()
