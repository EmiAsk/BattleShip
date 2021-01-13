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
    font = pygame.font.Font('font.ttf', 22)

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
            if self.click[0] is True and  function is not None:
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


class GameInfo:
    pygame.font.init()
    font_header = pygame.font.Font('font.ttf', 70)
    font = pygame.font.Font('font.ttf', 24)

    def __init__(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 745), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)
        self.text = self.font_header.render('Goal of the game', True, [0, 0, 0])
        screen.blit(self.text, (170, 40))

        self.pages = [self.goal, self.arrange, self.walk]
        self.page = 0
        self.pages[self.page]()

    def buttons(self):
        self.button_back = Button(60, 50)
        self.button_back.draw(40, 710, '<-', self.back)

        self.button_further = Button(60, 50)
        self.button_further.draw(795, 710, '->', self.further)

        self.button_to_menu = Button(240, 50)
        self.button_to_menu.draw(330, 710, '  < Back to menu >', self.to_menu)

    def to_menu(self):
        pass  # class Menu

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
        self.board = load_image('board_1.jpg')

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


game = GameInfo()
if __name__ == '__main__':
    running = True
    game.buttons()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                game.buttons()
        pygame.display.flip()
