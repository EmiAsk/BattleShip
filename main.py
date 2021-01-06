from os import path
from enum import Enum

import pygame
import sys
import sqlite3


def load_image(name, colorkey=None):
    fullname = path.join(name)
    if not path.isfile(fullname):
        print(f"ОШИБКА: Файл '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


pygame.init()
pygame.mixer.init()
size = width, height = 800, 700
screen = pygame.display.set_mode(size)
image = load_image('fon.jpg')
screen.blit(image, (0, 0))
pygame.display.flip()
clock = pygame.time.Clock()
fps = 30
running = True


class State(Enum):
    GREETING = 1
    LOGIN = 2
    SIGNIN = 3
    GAMEINFO = 4
    DEVELOPERS = 5
    SETTINGS = 6
    GAME = 7
    ACCOUNT = 8
    TABLE_RECORDS = 9
    PAUSE = 10
    QUIT = 11


class GameState:
    def __init__(self):
        self.state = State.GREETING

    def change(self, state):
        self.state = state

    def check(self, state):
        if self.state == state:
            return True
        return False


class Game:
    def __init__(self):
        self.game_state = GameState()

    def start(self):
        # while True:
            #print(self.game_state.change(State.GREETING))
            if self.game_state.check(State.GREETING):
                ProgramGreeting()
            elif self.game_state.check(State.LOGIN):
                Registration_User()
            elif self.game_state.check(State.SIGNIN):
                pass
            elif self.game_state.check(State.DEVELOPERS):
                pass
            elif self.game_state.check(State.SETTINGS):
                pass
            elif self.game_state.check(State.GAME):
                pass
            elif self.game_state.check(State.ACCOUNT):
                pass
            elif self.game_state.check(State.TABLE_RECORDS):
                pass
            elif self.game_state.check(State.PAUSE):
                pass
            elif self.game_state.check(State.QUIT):
                print('ex')
                exit()

class Button:
    pygame.init()
    button_sound = pygame.mixer.Sound('click_button.wav')
    font = pygame.font.Font('20008.ttf', 30)

    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        self.active_color = '#a6caf0'
        self.inactive_color = '#79afe8'

    def draw(self, x, y, message, function=None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed(3)

        if x < self.mouse[0] < x + self.width and y < self.mouse[1] < y + self.heigth:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.heigth))

            if self.click[0] is True:
                pygame.mixer.Sound.play(Button.button_sound)
                pygame.time.delay(300)
                if function is not None:
                    if function == quit():
                        pygame.quit()
                        quit()
                    else:
                        function()
                else:
                    return True
        else:
            pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.heigth))
        pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)
        self.print_text(message, x + 5, y + 5)

    def print_text(self, message, x, y):
        self.text = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text, (x, y))


class ProgramGreeting:
    pygame.font.init()
    font = pygame.font.Font('20008.ttf', 20)
    font_header = pygame.font.Font('20008.ttf', 70)

    def __init__(self):
        self.game_state = GameState()
        self.text = self.font_header.render('BattleShip', True, [0, 0, 0])
        self.line = pygame.draw.line(screen, 'black', (150, 150), (640, 150), 3)
        screen.blit(self.text, (170, 60))

        self.button_size = (240, 50)

        self.button_login = Button(*self.button_size)
        if self.button_login.draw(65, 350, '       Log in', None):
            self.game_state.change(State.LOGIN)
            return

        self.button_signin = Button(*self.button_size)
        if self.button_signin.draw(505, 350, '       Sign in', None):
            self.game_state.change(State.SIGNIN)
            return

        self.button_gameinfo = Button(*self.button_size)
        if self.button_gameinfo.draw(65, 500, '   Game Info', None):
            self.game_state.change(State.GAMEINFO)
            return

        self.button_developers = Button(*self.button_size)
        if self.button_developers.draw(505, 500, '  Developers', None):
            self.game_state.change(State.DEVELOPERS)
            return

        self.button_exit = Button(*self.button_size)
        if self.button_exit.draw(285, 600, '         Exit', None):
            self.game_state.change(State.QUIT)
        pygame.display.flip()


class Registration_User():
    pygame.font.init()
    font = pygame.font.Font('20008.ttf', 35)
    font_header = pygame.font.Font('20008.ttf', 65)

    screen = pygame.display.set_mode((800, 700))
    image = load_image('test_fon_line.jpg')
    screen.blit(image, (0, 0))

    def __init__(self):
        self.system_labels()
        self.finally_name = None
        self.finally_password = None

    def system_labels(self):
        self.text_login = self.font_header.render('Account Login', True, (0, 0, 0))
        self.text_name = self.font.render('Name:', True, (0, 0, 0))
        pygame.draw.rect(screen, ('#a6caf0'), (80, 210, 600, 60))
        pygame.draw.rect(screen, ('#a6caf0'), (80, 370, 600, 60))

        pygame.draw.rect(screen, 'black', (260, 220, 400, 40), 1)
        self.text_password = self.font.render('Password:', True, (0, 0, 0))
        pygame.draw.rect(screen, 'black', (330, 380, 330, 40), 1)

        screen.blit(self.text_login, (120, 10))
        screen.blit(self.text_name, (100, 220))
        screen.blit(self.text_password, (100, 380))

        pygame.draw.rect(self.screen, '#a6caf0', (280, 500, 240, 50))
        self.button_text = self.font.render('Continue', True, (0, 0, 0))
        self.screen.blit(self.button_text, (305, 505))

    def input_name(self, message):
        self.text_name = self.font.render(message, True, [0, 0, 0])
        self.screen.blit(self.text_name, (270, 220))
        self.finally_name = message  # for database

    def input_password(self, password):
        self.text_password = self.font.render(password, True, [0, 0, 0])
        self.screen.blit(self.text_password, (160, 320))
        self.finally_password = password  # for database

    def add_data(self):
        self.connect = sqlite3.connect('battleship.db')
        self.cursor = self.connect.cursor()
        try:
            self.result = self.cursor.execute(f'''INSERT INTO
users(name, password, all_games, wins, lose)
VALUES("{self.finally_name}", "{self.finally_password}", "0", "0", "0") ''')
            self.connect.commit()
        except sqlite3.IntegrityError:
            pass
        self.connect.close()

    def working_class(self):
        running = True
        need_input_name = False
        need_input_password = False
        input_name = ''
        input_password = ''

        while running:
            pygame.init()
            clock = pygame.time.Clock()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                    if event.pos[0] in range(260, 660) and event.pos[1] in range(220, 250):
                        need_input_password = False
                        need_input_name = True
                    if event.pos[0] in range(160, 360) and event.pos[1] in range(180, 210):
                        need_input_name = False
                        need_input_password = True
                        # input_text = '|'

                if need_input_name:
                    need_input_password = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            need_input_name = False
                            if input_password != '':
                                self.add_data()
                        elif event.key == pygame.K_BACKSPACE:
                            input_name = input_name[:-1]
                        else:
                            if len(input_name) < 16:
                                input_name += event.unicode
                    self.input_name(input_name)
                    pygame.display.flip()

                if need_input_password:
                    need_input_name = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            need_input_password = False
                            if input_name != '':
                                self.add_data()
                        elif event.key == pygame.K_BACKSPACE:
                            input_password = input_password[:-1]
                        else:
                            input_password += event.unicode
                    self.input_password(input_password)
                    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    size = width, height = 800, 700
    screen = pygame.display.set_mode(size)
    image = load_image('fon.jpg')
    screen.blit(image, (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    running = True
    while running:
        Game().start()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()
