import pygame
import config
import sqlite3

from error import main as main_error
from user_data_class import UserData
from secondary_functions import load_image

pygame.init()
size = width, height = config.SIZE_WINDOW
screen = pygame.display.set_mode(size)
image = load_image(config.IMAGE_BACKGROUND)
screen.blit(image, (0, 0))
pygame.display.flip()


class Signin(UserData):
    def user_data(self):
        connect = sqlite3.connect('battleship.db')
        cursor = connect.cursor()
        self.usernames = cursor.execute('SELECT name FROM users').fetchall()
        self.usernames = [name[0] for name in self.usernames]
        if self.finally_name in self.usernames:
            main_error()
        else:
            pygame.draw.rect(screen, (166, 120, 65), (705, 275, 40, 50), 0)
            pygame.draw.lines(screen, 'green', False, ((710, 280), (725, 320), (740, 280)),
                              width=5)
            try:
                from hashlib import sha512
                self.finally_password = sha512(self.finally_password.encode())
                self.request = cursor.execute(f'''INSERT INTO
                users(name, password, all_games, wins, lose)
                VALUES("{self.finally_name}", "{self.finally_password}", "0", "0", "0") ''')
                connect.commit()
                config.USER_NAME = self.finally_name
            except sqlite3.IntegrityError:
                pass
            except AttributeError:
                pass
            connect.close()
        self.to_greeting()

    def to_greeting(self):
        self.work = False


def main():
    signin = Signin()
    signin.buttons()
    signin.work = True
    while signin.work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                signin.work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                signin.buttons()
                signin.input_flag(event)
            if event.type == pygame.KEYDOWN:
                signin.input_text(event)
        pygame.display.flip()
