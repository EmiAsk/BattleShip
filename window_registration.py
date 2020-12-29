import pygame
import sqlite3


class Registration_User():
    pygame.font.init()
    font = pygame.font.Font('Gabriola.ttf', 30)

    def __init__(self, screen):
        self.screen = screen
        self.system_labels()
        self.finally_name = None
        self.finally_password = None

    def system_labels(self):
        self.text_login = self.font.render('Вход в аккаунт', True, (0, 0, 0))
        self.text_name = self.font.render('Имя:', True, (0, 0, 0))
        pygame.draw.rect(screen, 'black', (160, 80, 200, 30), 1)
        self.text_password = self.font.render('Пароль:', True, (0, 0, 0))
        pygame.draw.rect(screen, 'black', (160, 180, 200, 30), 1)

        screen.blit(self.text_login, (180, 10))
        screen.blit(self.text_name, (60, 82))
        screen.blit(self.text_password, (60, 180))

    def input_name(self, message):
        self.text_name = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text_name, (165, 80))
        self.finally_name = message  # for database

    def input_password(self, password):
        self.text_password = self.font.render(password, True, [0, 0, 0])
        screen.blit(self.text_password, (160, 180))
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
    screen = pygame.display.set_mode((500, 300))
    screen.fill((225, 210, 225))
    register = Registration_User(screen)
    running = True

    need_input_name = False
    need_input_password = False
    input_name = ''
    input_password = ''

    while running:
        pygame.init()
        clock = pygame.time.Clock()
        Registration_User(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(160, 360) and event.pos[1] in range(80, 110):
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
                            register.add_data()
                    elif event.key == pygame.K_BACKSPACE:
                        pygame.draw.rect(screen, (225, 210, 225), (160, 80, 200, 30), 0)
                        input_name = input_name[:-1]
                    else:
                        if len(input_name) < 16:
                            input_name += event.unicode
                register.input_name(input_name)
                pygame.display.flip()

            if need_input_password:
                need_input_name = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        need_input_password = False
                        if input_name != '':
                            register.add_data()
                    elif event.key == pygame.K_BACKSPACE:
                        pygame.draw.rect(screen, (225, 210, 225), (160, 180, 200, 30), 0)
                        input_password = input_password[:-1]
                    else:
                        if len(input_password) < 16:
                            input_password += event.unicode
                register.input_password(input_password)
                pygame.display.flip()
