import pygame
import config
import sqlite3

from class_for_buttons import Button
from error import main as main_error
from window_game import main as game_main
from user_data_class import UserData

pygame.init()
size = width, height = config.SIZE_WINDOW
screen = pygame.display.set_mode(size)

class Login(UserData):
    def head(self):
        self.render_text('Enter your account details to start the game', 60, 70, 110)
        pygame.display.flip()

    def user_data(self):
        connect = sqlite3.connect('battleship.db')
        cursor = connect.cursor()
        self.usernames = cursor.execute('SELECT name FROM users').fetchall()
        self.usernames = [name[0] for name in self.usernames]
        if self.finally_name not in self.usernames:
            main_error()
        else:
            pygame.draw.rect(screen, config.SCREEN_COLOR, (705, 275, 40, 50), 0)
            pygame.draw.lines(screen, 'green', False, ((710, 280), (725, 320), (740, 280)),
                              width=5)
            user_password = cursor.execute('SELECT password FROM users WHERE name == ?',
                                           (self.finally_name,)).fetchone()[0]
            config.USER_NAME = self.finally_name
            connect.close()
            from hashlib import sha512
            self.finally_password = 'testing'
            self.password = sha512(self.finally_password.encode()).hexdigest()
            print(self.password == user_password)
            if self.password != user_password:
                main_error()
            else:
                pygame.draw.rect(screen, config.SCREEN_COLOR, (755, 385, 40, 50), 0)
                pygame.draw.lines(screen, 'green', False, ((755, 385), (765, 420), (785, 385)),
                                  width=5)
                self.to_game()

    def to_greeting(self):
        self.work = False

    def to_game(self):
        game_main()


def main():
    login = Login()
    login.head()
    login.work = True
    while login.work:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                login.work = False
            if event.type == pygame.MOUSEMOTION:
                Button().move(event.pos[0], event.pos[1])
            if event.type == pygame.MOUSEBUTTONDOWN:
                login.buttons()
                login.input_flag(event)
            if event.type == pygame.KEYDOWN:
                login.input_text(event)
        pygame.display.flip()
