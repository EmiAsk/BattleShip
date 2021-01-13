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
        self.text = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text, (x, y))


class Greeting:
    pygame.font.init()
    font = pygame.font.Font(config.FONT, 20)
    font_header = pygame.font.Font(config.FONT, 110)

    def __init__(self):
        self.text = self.font_header.render('BattleShip', True, [0, 0, 0])
        self.text_2 = self.font_header.render('BattleShip', True, config.SILVER_COLOR)
        screen.blit(self.text_2, (373, 25))
        screen.blit(self.text, (370, 25))
        self.buttons()

    def buttons(self):
        self.button_login = Button()
        self.button_login.draw(500, 230, '< Log in >', self.login)

        self.button_signin = Button()
        self.button_signin.draw(500, 350, '< Sign in >', self.signin)

        self.button_gameinfo = Button()
        self.button_gameinfo.draw(500, 470, '< Game Info >', self.gameinfo)

        self.button_exit = Button()
        self.button_exit.draw(500, 590, '< Exit >', self.exit_game)

    def login(self):
        pass  # class Login

    def signin(self):
        pass  # class Signin

    def gameinfo(self):
        pass  # class Game Info

    def help(self):
        pass

    def exit_game(self):
        exit()


if __name__ == '__main__':
    running = True
    greeting = Greeting()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN:
                greeting.buttons()
        pygame.display.flip()
