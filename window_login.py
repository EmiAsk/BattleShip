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


class Login(UserData):
    def user_data(self):
        connect = sqlite3.connect('battleship.db')
        cursor = connect.cursor()
        self.usernames = cursor.execute('SELECT name FROM users').fetchall()
        self.usernames = [name[0] for name in self.usernames]
        if self.finally_name not in self.usernames:
            main_error()
        else:
            pygame.draw.rect(screen, (166, 120, 65), (705, 275, 40, 50), 0)
            pygame.draw.lines(screen, 'green', False, ((710, 280), (725, 320), (740, 280)),
                              width=5)
            user_password = cursor.execute('SELECT password FROM users WHERE name == ?',
                                           (self.finally_name,)).fetchone()[0]
            config.USER_NAME = self.finally_name
            connect.close()
            from hashlib import sha512
            self.password = sha512(self.finally_password.encode()).hexdigest()
            if self.password != user_password:
                main_error()
            else:
                pygame.draw.rect(screen, (166, 120, 65), (755, 385, 40, 50), 0)
                pygame.draw.lines(screen, 'green', False, ((755, 385), (765, 420), (785, 385)),
                                  width=5)

    def to_greeting(self):
        self.work = False


if __name__ == '__main__':
    login = Login()
    login.buttons()
    login.work = True
    while login.work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                login.work = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                login.buttons()
                login.input_flag(event)
            if event.type == pygame.KEYDOWN:
                login.input_text(event)
        pygame.display.flip()

