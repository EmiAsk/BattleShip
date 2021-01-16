import pygame
from sys import exit
import config
import sqlite3

from os import path

from user_data_class import UserData


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


class Signin(UserData):
    def user_data(self):
        connect = sqlite3.connect('battleship.db')
        cursor = connect.cursor()
        self.usernames = cursor.execute('SELECT name FROM users').fetchall()
        self.usernames = [name[0] for name in self.usernames]
        if self.finally_name in self.usernames:
            print('ERROR 02: Incorrect data entered')
            pygame.draw.rect(screen, (166, 120, 65), (705, 275, 40, 50), 0)
            pygame.draw.line(screen, 'red', (710, 280), (740, 320), 5)
            pygame.draw.line(screen, 'red', (740, 280), (710, 320), 5)

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
            return True

def main():
    global work
    work = True
    signin = Signin()
    signin.buttons()
    while work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                signin.buttons()
                signin.input_flag(event)
            if event.type == pygame.KEYDOWN:
                signin.input_text(event)
            pygame.display.flip()
    return