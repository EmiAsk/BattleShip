import pygame
import config
import sqlite3

from error import main as main_error
from user_data_class import UserData
from window_game import main as game_main
from class_for_buttons import Button

pygame.init()
size = width, height = config.SIZE_WINDOW
screen = pygame.display.set_mode(size)


class Signin(UserData):
    def head(self):
        self.render_text('Enter information  to create your account', 70, 70, 110)
        pygame.display.flip()

    def user_data(self):
        connect = sqlite3.connect('battleship.db')
        cursor = connect.cursor()
        self.usernames = cursor.execute('SELECT name FROM users').fetchall()
        self.usernames = [name[0] for name in self.usernames]
        if self.finally_name in self.usernames:
            main_error()
        else:
            config.USER_NAME = self.finally_name
            pygame.draw.rect(screen, (166, 120, 65), (705, 275, 40, 50), 0)
            pygame.draw.lines(screen, 'green', False, ((710, 280), (725, 320), (740, 280)),
                              width=5)
            try:
                from hashlib import sha512
                self.finally_password = sha512(self.finally_password.encode()).hexdigest()

                self.request = cursor.execute(f'''INSERT INTO
                users(name, password, all_games, wins, lose)
                VALUES("{self.finally_name}", "{self.finally_password}", "0", "0", "0") ''')

                self.second_request = cursor.execute(f'''INSERT INTO
                games(user, result, score)
                VALUES("{config.USER_NAME}", "0", "0")''')

                connect.commit()
                config.USER_NAME = self.finally_name
            except sqlite3.IntegrityError:
                pass
            except AttributeError:
                pass
            connect.close()
            self.to_game()

    def to_greeting(self):
        self.work = False

    def to_game(self):
        game_main()


def main():
    signin = Signin()
    signin.head()
    signin.work = True
    while signin.work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                signin.work = False
            if event.type == pygame.MOUSEMOTION:
                Button().move(event.pos[0], event.pos[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                signin.buttons()
                signin.input_flag(event)
            if event.type == pygame.KEYDOWN:
                signin.input_text(event)
        pygame.display.flip()
