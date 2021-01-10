import pygame
import sqlite3
from os import path
import sys



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

size = width, height = 800, 700
screen = pygame.display.set_mode(size)
image = load_image('test_fon_line.jpg')
screen.blit(image, (0, 0))

class Registration_User():

    pygame.font.init()
    font = pygame.font.Font('20008.ttf', 35)
    font_header = pygame.font.Font('20008.ttf', 65)


    #image = load_image('test_fon_line.jpg')
    #screen.blit(image, (0, 0))

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

        pygame.draw.rect(screen, '#a6caf0', (280, 500, 240, 50))
        self.button_text = self.font.render('Continue', True, (0, 0, 0))
        screen.blit(self.button_text, (305, 505))

    def input_name(self, message):
        self.text_name = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text_name, (270, 220))
        self.finally_name = message  # for database

    def input_password(self, password):
        self.text_password = self.font.render(password, True, [0, 0, 0])
        screen.blit(self.text_password, (160, 320))
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


if __name__ == '__main__':

    Registration_User()
    pygame.display.update()
    running = True
    need_input_name = False
    need_input_password = False
    input_name = ''
    input_password = ''

    while running:
        pygame.init()

        clock = pygame.time.Clock()
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
                            Registration_User().add_data()
                    elif event.key == pygame.K_BACKSPACE:
                        input_name = input_name[:-1]
                    else:
                        if len(input_name) < 16:
                            input_name += event.unicode
                Registration_User().input_name(input_name)
                pygame.display.flip()

            if need_input_password:
                need_input_name = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        need_input_password = False
                        if input_name != '':
                            Registration_User().add_data()
                    elif event.key == pygame.K_BACKSPACE:
                        input_password = input_password[:-1]
                    else:
                        input_password += event.unicode
                Registration_User().input_password(input_password)
