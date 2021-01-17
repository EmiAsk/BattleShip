import pygame
import config
import sqlite3

from secondary_functions import load_image
from class_for_buttons import Button

pygame.init()
size = width, height = config.SIZE_WINDOW
screen = pygame.display.set_mode(size)
image = load_image(config.IMAGE_BACKGROUND)
screen.blit(image, (0, 0))
pygame.display.flip()


class Table:
    pygame.font.init()
    font_header = pygame.font.Font(config.FONT, 70)
    font = pygame.font.Font(config.FONT, 28)

    def __init__(self):
        self.work = True
        self.button = Button(230, 50)
        self.draw()
        self.filling_table()

    def draw(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 745), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)
        self.header = self.font_header.render('Table of records', True, [0, 0, 0])
        screen.blit(self.header, (200, 40))

        self.button.draw(330, 700, ' < Back to menu >')

        for row in range(12):
            pygame.draw.rect(screen, 'black', (40, 180 + (row * 40), 820, 40), 2)
        for column in range(2, 6):
            pygame.draw.line(screen, 'black', (100 + 100 * column, 180), (100 + 100 * column, 660),
                             2)
            screen.blit(self.font.render(config.TABLE_HEADERS[column - 1], True, [0, 0, 0]),
                        (110 + column * 100, 180))
        screen.blit(self.font.render(config.TABLE_HEADERS[0], True, [0, 0, 0]), (110, 180))
        self.filling_table()

    def press(self):
        self.button.press(330, 700, self.to_greeting)

    def move(self):
        self.button.move(330, 700)

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

    def to_greeting(self):
        self.work = False


def main():
    table = Table()
    table.draw()
    table.work = True
    while table.work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                table.work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                table.press()
            if event.type == pygame.MOUSEMOTION:
                table.move()
        table.draw()
        pygame.display.flip()
