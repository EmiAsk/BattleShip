import pygame
import config

from class_for_buttons import Button

pygame.init()
size = width, height = config.SIZE_WINDOW
screen = pygame.display.set_mode(size)


class UserData:
    def __init__(self):
        self.work = True
        self.button_continue = Button(230, 50)
        self.button_greeting = Button(230, 50)
        self.header_font = pygame.font.Font(config.FONT, 38)
        self.text_font = pygame.font.Font(config.FONT, 28)
        pygame.display.flip()

        self.finally_name = None
        self.finally_password = None
        self.entered_name = ''
        self.entered_password = ''
        self.draw()

    def buttons(self):
        self.button_continue.press(330, 450, self.user_data)
        self.button_greeting.press(330, 700, self.to_greeting)

    def draw(self):
        pygame.draw.rect(screen, (166, 120, 65), (30, 30, 840, 745), 0)
        pygame.draw.line(screen, 'black', (30, 150), (867, 150), 4)

        pygame.draw.rect(screen, 'black', (200, 220, 500, 40), 1)
        pygame.draw.rect(screen, 'black', (240, 320, 500, 40), 1)

        self.text_name = self.text_font.render('Name:', True, (0, 0, 0))
        self.text_password = self.text_font.render('Password:', True, (0, 0, 0))

        screen.blit(self.text_name, (100, 220))
        screen.blit(self.text_password, (100, 320))

        self.render_text(
            'Enter your account details to start the game', 60, 70, 110)

        self.button_continue.draw(330, 400, '< Start the game >')
        self.button_greeting.draw(330, 490, ' < Back to menu >')

    def render_text(self, text, x, y, fsize):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            screen.blit(self.header_font.render(line, True, [0, 0, 0]), (x, y + fsize * i))

    def input_flag(self, event):
        self.flag_nickname = False
        self.flag_password = False

        if 200 <= event.pos[0] <= 700 and 280 <= event.pos[1] <= 320:
            self.flag_nickname = True
            self.flag_password = False
        elif 240 <= event.pos[0] <= 740 and 380 <= event.pos[1] <= 420:
            self.flag_nickname = False
            self.flag_password = True

    def input_text(self, event):
        if self.flag_nickname:
            if event.key == pygame.K_BACKSPACE:
                self.entered_name = self.entered_name[:-1]
                pygame.draw.rect(screen, (166, 120, 65), (201, 281, 498, 38), 0)
            else:
                if event.unicode != '':
                    if len(self.entered_name) < 15:
                        self.entered_name += event.unicode
            self.finally_name = self.entered_name
            self.nickname = self.text_font.render(self.entered_name, True, [0, 0, 0])
            screen.blit(self.nickname, (210, 277))

        if self.flag_password:
            if event.key == pygame.K_BACKSPACE:
                self.entered_password = self.entered_password[:-1]
                pygame.draw.rect(screen, (166, 120, 65), (241, 381, 498, 38), 0)
            else:
                if event.unicode != '':
                    if len(self.entered_password) < 15:
                        self.entered_password += event.unicode
            self.finally_password = self.entered_password
            self.password = self.text_font.render(self.entered_password, True, [0, 0, 0])
            screen.blit(self.password, (245, 380))
        pygame.display.flip()
