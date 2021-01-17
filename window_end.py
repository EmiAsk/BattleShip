import pygame
import config

from class_for_buttons import Button
from secondary_functions import load_image, game_exit

from window_table import main as table_main

screen = pygame.display.set_mode(config.SIZE_WINDOW)
image = load_image(config.IMAGE_BACKGROUND)
screen.blit(image, (0, 0))
pygame.display.flip()


class GameEnd:
    pygame.font.init()
    font_header = pygame.font.Font(config.FONT, 70)
    font = pygame.font.Font(config.FONT, 38)

    def __init__(self):
        self.work = True
        self.button_table = Button(240, 50)
        self.button_to_menu = Button(240, 50)
        self.button_exit = Button(240, 50)
        self.draw()

    def draw(self):
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)

        self.header = self.font_header.render('Game Over', True, [0, 0, 0])

        pygame.draw.rect(screen, (166, 120, 65), (20, 30, 850, 745), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)

        self.button_table.draw(320, 500, '< Table of records >')
        self.button_exit.draw(320, 640, '       < Exit >')

        screen.blit(self.header, (280, 40))

        data_title = ['You', 'Score', 'Level']
        data_result = [config.RESULT, config.SCORE, 'newbie (1)']
        y = 200

        for i in range(3):
            data_result[0] = 'lose' if config.RESULT == 'computer' else 'win'
            self.text = self.font.render(f'{data_title[i]}: {data_result[i]}', True, [0, 0, 0])
            screen.blit(self.text, (100, y))
            y += 70

    def press(self):
        self.button_table.press(320, 500, self.to_table)
        self.button_exit.press(320, 640, game_exit)

    def move(self):
        self.button_table.move(320, 500)
        self.button_exit.move(320, 640)

    def to_greeting(self):
        self.work = False

    def to_table(self):
        table_main()

    def play_again(self):
        self.work = False

    def render_text(self, text, x, y, fsize):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            screen.blit(self.font.render(line, True, [0, 0, 0]), (x, y + fsize * i))


def main():
    gameend = GameEnd()
    GameEnd()
    pygame.display.flip()
    while gameend.work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
                gameend.work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameend.press()
            if event.type == pygame.MOUSEMOTION:
                gameend.move()
        gameend.draw()
        pygame.display.flip()
