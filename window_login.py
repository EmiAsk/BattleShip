import pygame
from sys import exit
import config
import sqlite3

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


class Login:
    pygame.font.init()
    font_header = pygame.font.Font(config.FONT, 70)
    font = pygame.font.Font(config.FONT, 28)
    font_input = pygame.font.Font(config.FONT, 28)

    def __init__(self):
        self.system_labels()
        self.buttons()
        self.finally_name = None
        self.finally_password = None
        self.entered_name = ''
        self.entered_password = ''

    def system_labels(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 745), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)

        pygame.draw.rect(screen, 'black', (200, 280, 500, 40), 1)
        pygame.draw.rect(screen, 'black', (240, 380, 500, 40), 1)

        self.text = self.font_header.render('LOGIN', True, [0, 0, 0])
        self.text_name = self.font.render('Name:', True, (0, 0, 0))
        self.text_password = self.font.render('Password:', True, (0, 0, 0))

        screen.blit(self.text, (360, 40))
        screen.blit(self.text_name, (90, 280))
        screen.blit(self.text_password, (90, 380))

        self.render_text(
            'Registering in the app will allow you to be a regular member.\n\n   To create an account, fill in both fields and click  "continue"',
            60, 160, 22)

    def data_checking(self):
        connect = sqlite3.connect('battleship.db')
        cursor = connect.cursor()
        self.usernames = cursor.execute('SELECT name FROM users').fetchall()
        self.usernames = [name[0] for name in self.usernames]
        if self.finally_name not in self.usernames:
            print('ERROR 02: Incorrect data entered')
            pygame.draw.line(screen, 'red', (710, 280), (740, 320), 5)
            pygame.draw.line(screen, 'red', (740, 280), (710, 320), 5)

        else:
            pygame.draw.lines(screen, 'green', False, ((710, 280), (725, 320), (740, 280)),
                              width=5)
            pygame.draw.lines(screen, 'green', False, ((710, 280), (725, 320), (740, 280)),
                              width=5)
            user_password = cursor.execute('SELECT password FROM users WHERE name == ?',
                                           (self.finally_name,)).fetchone()[0]
            connect.close()
            from hashlib import sha512
            password = sha512(self.finally_password.encode()).hexdigest()
            if password != user_password:
                print('ERROR 02: Incorrect data entered.')

    def buttons(self):
        self.continue_button = Button(230, 50)
        self.continue_button.draw(330, 450, '    < Continue >', self.data_checking)

        self.button = Button(230, 50)
        self.button.draw(330, 700, ' < Back to menu >', self.return_func)

    def render_text(self, text, x, y, fsize):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            screen.blit(self.font.render(line, True, [0, 0, 0]), (x, y + fsize * i))

    def name_input(self, event):
        global flag_input_name
        if flag_input_name:
            if event.key == pygame.K_BACKSPACE:
                self.entered_name = self.entered_name[:-1]
                pygame.draw.rect(screen, (166, 120, 65), (201, 281, 498, 38), 0)
            else:
                if event.unicode != '':
                    if len(self.entered_name) < 15:
                        self.entered_name += event.unicode
            self.finally_name = self.entered_name
            self.nickname = self.font_input.render(self.entered_name, True, [0, 0, 0])
            screen.blit(self.nickname, (210, 277))
            pygame.display.flip()

    def password_input(self, event):
        global flag_input_password
        if flag_input_password:
            if event.key == pygame.K_BACKSPACE:
                self.entered_password = self.entered_password[:-1]
                pygame.draw.rect(screen, (166, 120, 65), (241, 381, 498, 38), 0)
            else:
                if event.unicode != '':
                    if len(self.entered_password) < 15:
                        self.entered_password += event.unicode
            self.finally_password = self.entered_password
            self.password = self.font_input.render(self.entered_password, True, [0, 0, 0])
            screen.blit(self.password, (245, 380))
            pygame.display.flip()

    def return_func(self):
        pass


flag_input_name = False
flag_input_password = False
def main():
    flag_input_name = False
    flag_input_password = False
    running = True
    login = Login()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(200, 700) and event.pos[1] in range(280, 320):
                    flag_input_name = True
                    flag_input_password = False
                elif event.pos[0] in range(240, 740) and event.pos[1] in range(380, 420):
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
main()