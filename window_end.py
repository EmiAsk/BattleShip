import pygame
import config

from class_for_buttons import Button
from secondary_functions import load_image, game_exit

pygame.init()
size = width, height = config.SIZE_WINDOW
screen = pygame.display.set_mode(size)
image = load_image(config.IMAGE_BACKGROUND)
screen.blit(image, (0, 0))
pygame.display.flip()


class ResultGame:
    def __init__(self):
        self.work = True
        self.stat = ['Your', 'Score', 'Level']
        self.font = pygame.font.Font(config.FONT, 40)
        self.font_header = pygame.font.Font(config.FONT, 70)

        self.button_table = Button(240, 50)
        self.button_to_menu = Button(240, 50)
        self.button_exit = Button(240, 50)
        self.draw()

    def draw(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 745), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)

        self.header = self.font_header.render('Game Over', True, [0, 0, 0])
        screen.blit(self.header, (280, 40))

        pygame.draw.line(screen, 'black', (100, 450), (800, 450), 4)

        data_title = ['You', 'Score', 'Level']
        data_result = [config.RESULT, config.SCORE, 'newbie (1)']
        y = 200

        for i in range(3):
            data_result[0] = 'lose' if config.RESULT == 'computer' else 'win'
            self.render_text(f'{data_title[i]}: {data_result[i]}', 100, y, 110)
            y += 70

    def buttons(self):
        self.button_table.draw(330, 500, ' < Table of records >')
        self.button_to_menu.draw(330, 570, ' < Back to menu >')
        self.button_exit.draw(330, 640, '       < Exit >')

    def press(self):
        self.button_table.press(330, 500, self.to_table_of_record())
        self.button_to_menu.press(330, 100, self.to_menu)
        self.button_exit.press(330, 710, self.game_exit)

    def move(self):
        self.button_table.move(330, 150)
        self.button_to_menu.move(330, 310)
        self.button_exit.move(330, 310)

    def render_text(self, text, x, y, fsize):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            screen.blit(self.font.render(line, True, [0, 0, 0]), (x, y + fsize * i))
            pygame.display.flip()

    def to_table_of_record(self):
        print(1)
        pass  # table_main()

    def to_menu(self):
        print(2)
        self.work = False

    def game_exit(self):
        print(3)
        game_exit()
        pygame.display.flip()


def main():
    result = ResultGame()
    result.draw()
    result.buttons()
    result.work = True
    while result.work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
                result.work = False
            if event.type == pygame.MOUSEMOTION:
                Button().move(event.pos[0], event.pos[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                result.buttons()
        pygame.display.flip()

main()
