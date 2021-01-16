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
pygame.display.flip()
clock = pygame.time.Clock()


class Login(UserData):
    def user_data(self):
        connect = sqlite3.connect('battleship.db')
        cursor = connect.cursor()
        self.usernames = cursor.execute('SELECT name FROM users').fetchall()
        self.finally_name not in self.usernames
        self.usernames = [name[0] for name in self.usernames]
        if self.finally_name not in self.usernames:
            print('ERROR 02: Incorrect data entered')
            pygame.draw.rect(screen, (166, 120, 65), (705, 275, 40, 50), 0)
            pygame.draw.line(screen, 'red', (710, 280), (740, 320), 5)
            pygame.draw.line(screen, 'red', (740, 280), (710, 320), 5)

        else:
            pygame.draw.rect(screen, (166, 120, 65), (705, 275, 40, 50), 0)
            pygame.draw.lines(screen, 'green', False, ((710, 280), (725, 320), (740, 280)),
                              width=5)
            user_password = cursor.execute('SELECT password FROM users WHERE name == ?',
                                           (self.finally_name,)).fetchone()[0]
            config.USER_NAME = self.finally_name
            connect.close()
            from hashlib import sha512
            #  password = sha512(self.finally_password.encode()).hexdigest()
            if self.finally_name != user_password:
                print('ERROR 02: Incorrect data entered.')
            else:
                return True


def main():
    global work
    work = True
    login = Login()
    login.buttons()
    while work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                login.buttons()
                login.input_flag(event)
            if event.type == pygame.KEYDOWN:
                login.input_text(event)
            pygame.display.flip()
