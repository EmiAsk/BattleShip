import pygame
import sqlite3
import config

from os import path
from sys import exit


class DataError(Exception):
    pass


def load_image(name):
    if not path.isfile(path.join(name)):
        print(f"ERROR 01: '{path.join(name)}' not found.")
        exit()
    image = pygame.image.load(path.join(name))
    return image


pygame.init()
size = width, height = config.SIZE_WINDOW
image = load_image(config.IMAGE_BACKGROUND)
screen = pygame.display.set_mode(size)
screen.blit(image, (0, 0))
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
        self.print_text(message, x + 5, y + 10)

    def print_text(self, message, x, y):
        self.text = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text, (x, y))

    def click_button(self, function):
        if function is not None:
            function()


class Login():
    pygame.font.init()
    font = pygame.font.Font(config.FONT, 35)
    font_input = pygame.font.Font(config.FONT, 30)
    font_header = pygame.font.Font(config.FONT, 42)

    def __init__(self):
        self.system_labels()
        self.buttons()
        self.finally_name = None
        self.finally_password = None
        self.entered_name = ''
        self.entered_password = ''

    def system_labels(self):
        pygame.draw.rect(screen, '#c0c0c0', (0, 20, width, 80))
        pygame.draw.rect(screen, ('#c0c0c0'), (40, 210, 820, 60))
        pygame.draw.rect(screen, ('#c0c0c0'), (40, 390, 820, 60))
        pygame.draw.rect(screen, 'black', (330, 220, 500, 40), 1)
        pygame.draw.rect(screen, 'black', (330, 400, 500, 40), 1)

        self.text = self.font_header.render('LOGIN', True, [0, 0, 0])
        self.text_name = self.font.render('Name:', True, (0, 0, 0))
        self.text_password = self.font.render('Password:', True, (0, 0, 0))

        screen.blit(self.text, (375, 35))
        screen.blit(self.text_name, (190, 220))
        screen.blit(self.text_password, (90, 400))

    def buttons(self):
        self.continue_button = Button(240, 50)
        self.continue_button.draw(330, 500, '         Continue', self.data_checking)

        self.help_button = Button(50, 50)
        self.help_button.draw(10, 750, '  ?', self.help)

    def data_checking(self):
        connect = sqlite3.connect('battleship.db')
        cursor = connect.cursor()
        self.usernames = cursor.execute('SELECT name FROM users').fetchall()
        self.usernames = [name[0] for name in self.usernames]
        if self.finally_name not in self.usernames:
            print('ERROR 02: Incorrect data entered')
        else:
            user_password = cursor.execute('SELECT password FROM users WHERE name == ?',
                                           (self.finally_name,)).fetchone()[0]
            connect.close()
            from hashlib import sha512
            password = sha512(self.finally_password.encode()).hexdigest()
            if password != user_password:
                print('ERROR 02: Incorrect data entered.')

    def help(self):
        pass

    def name_input(self, event):
        if flag_input_name:
            if event.key == pygame.K_BACKSPACE:
                self.entered_name = self.entered_name[:-1]
                pygame.draw.rect(screen, ('#c0c0c0'), (331, 221, 498, 38), 0)
            else:
                if event.unicode != '':
                    if len(self.entered_name) < 15:
                        self.entered_name += event.unicode
            self.finally_name = self.entered_name
            self.nickname = self.font_input.render(self.entered_name, True, [0, 0, 0])
            screen.blit(self.nickname, (335, 220))
            pygame.display.flip()

    def password_input(self, event):
        if flag_input_password:
            if event.key == pygame.K_BACKSPACE:
                self.entered_password = self.entered_password[:-1]
                pygame.draw.rect(screen, ('#c0c0c0'), (331, 401, 498, 38), 0)
            else:
                if event.unicode != '':
                    if len(self.entered_password) < 15:
                        self.entered_password += event.unicode
            self.finally_password = self.entered_password
            self.password = self.font_input.render(self.entered_password, True, [0, 0, 0])
            screen.blit(self.password, (335, 400))
            pygame.display.flip()


if __name__ == '__main__':
    running = True
    flag_input_name = False
    flag_input_password = False
    login = Login()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(330, 830) and event.pos[1] in range(220, 260):
                    flag_input_name = True
                    flag_input_password = False
                elif event.pos[0] in range(330, 830) and event.pos[1] in range(400, 440):
                    flag_input_password = True
                    flag_input_name = False
                login.buttons()
            if event.type == pygame.MOUSEMOTION:
                login.buttons()
            if event.type == pygame.KEYDOWN:
                if flag_input_name:
                    login.name_input(event)
                elif flag_input_password:
                    login.password_input(event)
            pygame.display.flip()
