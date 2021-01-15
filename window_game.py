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
        self.inactive_color = '#c0c0c0'
        self.active_color = '#a6a6a6'

    def draw(self, x, y, message, function=None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed(3)

        if x < self.mouse[0] < x + self.width and y < self.mouse[1] < y + self.heigth:
            pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.heigth))
            pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)
            if self.click[0] is True:
                pygame.mixer.Sound.play(Button.button_sound)
                pygame.time.delay(300)
                self.click_button(function)

        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.heigth))
            pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)
        self.print_text(message, x + 20, y + 10)

    def print_text(self, message, x, y):
        self.text = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text, (x, y))

    def click_button(self, function):
        if function is not None:
            function()


class GameBattleShip:
    pygame.font.init()
    font_header = pygame.font.Font('font.ttf', 70)
    font = pygame.font.Font('font.ttf', 24)

    def __init__(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 745), 0)
        self.text = self.font_header.render('Your board', True, [0, 0, 0])
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)

        screen.blit(self.text, (270, 40))
        self.board_draw()

    def board_draw(self):
        self.ship = []
        self.height = self.width = 50

        self.board_y = 167
        self.board_x = 155
        self.cell_x, self.cell_y = 140, 160
        for number in range(1, 11):
            self.board_y += 50
            self.number = self.font.render(str(number), True, [255, 255, 255])
            screen.blit(self.number, (150, self.board_y))

        for alpha in config.LETTERS_GAME:
            self.board_x += 50
            self.alpha = self.font.render(alpha, True, [255, 255, 255])
            screen.blit(self.alpha, (self.board_x, 160))

        for cell_x in range(1, 11):
            for cell_y in range(1, 11):
                pygame.draw.rect(screen, 'black', (self.cell_x + (50 * cell_x), self.cell_y + (50 * cell_y), 50, 50), width=5)

    def ship(self, x_mouse, y_mouse):
        pass


game = GameBattleShip()
if __name__ == '__main__':
    running = True
    game.board_draw()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                game.ship(x_mouse, y_mouse)
        pygame.display.flip()