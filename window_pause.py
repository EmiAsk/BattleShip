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
image = load_image(config.IMAGE_BACKGROUND)
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


class Greeting:
    pygame.font.init()
    font = pygame.font.Font(config.FONT, 44)

    def __init__(self):
        self.buttons()
        self.text = self.font.render('The game is paused.', True, [0, 0, 0])
        pygame.draw.line(screen, 'black', (350, 150), (860, 150), 4)
        screen.blit(self.text, (350, 90))

    def buttons(self):
        self.button_login = Button()
        self.button_login.draw(500, 250, '< Return to game >', self.to_game)

        self.button_signin = Button()
        self.button_signin.draw(500, 370, '< Go to the menu >', self.to_menu)

        self.help_button = Button(55, 50)
        self.help_button.draw(10, 750, '?', self.help)

    def to_game(self):
        pass  # class Game

    def to_menu(self):
        pass  # class Menu

    def help(self):
        pass

if __name__ == '__main__':
    running = True
    Greeting()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                Greeting()
        pygame.display.flip()