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


class GameInfo:
    pygame.font.init()
    font_header = pygame.font.Font(config.FONT, 70)
    font = pygame.font.Font(config.FONT, 24)

    def __init__(self):
        self.work = True
        self.pages = [self.goal, self.arrange, self.walk]
        self.page = 0
        self.button_back = Button(60, 50)
        self.button_further = Button(60, 50)
        self.button_to_menu = Button(240, 50)
        self.draw()

    def draw(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 745), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)
        self.pages[self.page]()

        self.button_back.draw(40, 710, '<-')
        self.button_further.draw(795, 710, '->')
        self.button_to_menu.draw(330, 710, '  < Back to menu >')

    def press(self):
        self.button_back.press(40, 710, self.back)
        self.button_further.press(795, 710, self.further)
        self.button_to_menu.press(330, 710, self.to_greeting)

    def move(self):
        self.button_back.move(40, 710)
        self.button_further.move(795, 710)
        self.button_to_menu.move(330, 710)

    def to_greeting(self):
        self.work = False

    def further(self):
        if self.page < len(self.pages) - 1:
            self.page += 1
        else:
            self.page = 0
        self.pages[self.page]()

    def back(self):
        if self.page > 0:
            self.page -= 1
        else:
            self.page = len((self.pages)) - 1
        self.pages[self.page]()

    def render_text(self, text, x, y, fsize):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            screen.blit(self.font.render(line, True, [0, 0, 0]), (x, y + fsize * i))

    def goal(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 680), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)
        self.header = self.font_header.render(config.HEAD_INFO_GAME[0], True, [0, 0, 0])
        self.render_text(config.TEXT_INFO_GAME[config.HEAD_INFO_GAME[0]], 60, 180, 40)
        self.board = load_image('additional_files/board.jpg')

        screen.blit(self.header, (170, 40))
        screen.blit(self.board, (500, 270))

    def arrange(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 680), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)
        self.header = self.font_header.render(config.HEAD_INFO_GAME[1], True, [0, 0, 0])
        screen.blit(self.header, (100, 40))
        self.render_text(config.TEXT_INFO_GAME[config.HEAD_INFO_GAME[1]], 60, 180, 40)

    def walk(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 680), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)
        self.header = self.font_header.render(config.HEAD_INFO_GAME[2], True, [0, 0, 0])
        screen.blit(self.header, (230, 40))
        self.render_text(config.TEXT_INFO_GAME[config.HEAD_INFO_GAME[2]], 60, 180, 40)


def main():
    gameinfo = GameInfo()
    while gameinfo.work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameinfo.work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameinfo.press()
            if event.type == pygame.MOUSEMOTION:
                gameinfo.move()
        gameinfo.draw()
        pygame.display.flip()
