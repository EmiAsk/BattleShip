import pygame
import config

from class_for_buttons import Button
from secondary_functions import load_image


pygame.init()
size = width, height = config.SIZE_WINDOW
screen = pygame.display.set_mode(size)
image = load_image(config.IMAGE_BACKGROUND)
screen.blit(image, (0, 0))
pygame.display.flip()


class ResultGame:
    def head(self):
        self.render_text('Game over', 340, 70, 110)
        pygame.display.flip()

    def result(self):
        data_title = ['You', 'Score', 'Level']
        data_result = [config.result, config.SCORE, 'newbie (1)']
        y = 150
        pygame.draw.lines(screen, 'black', False, ((710, 280), (725, 320), (740, 280)),
                              width=5)
        for i in range(3):
            if config.RESULT == 'computer' and i == 2:
                pass
            else:
                self.render_text(f'{data_title[i]}: {data_result[i]}', 50, y, 110)
                y += 30

    def to_table_of_record(self):
        self.work = False

    def to_menu():
        self.work = False # ???


def main():
    result_game = ResultGame()
    result_game.head()
    result_game.work = True
    while result_game.work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                result_game.work = False
            if event.type == pygame.MOUSEMOTION:
                Button().move(event.pos[0], event.pos[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                result_game.buttons()
        pygame.display.flip()
