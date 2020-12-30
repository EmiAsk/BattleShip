import pygame
import sys

from os import path


def load_image(name, colorkey=None):
    fullname = path.join(name)
    if not path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Button:
    pygame.init()
    button_sound = pygame.mixer.Sound('click_button.wav')
    font = pygame.font.Font('segoepr.ttf', 22)
    def __init__(self, width=240, height=50):
        self.width = width
        self.heigth = height
        self.inactive_color = (100, 149, 237)
        self.active_color = (50, 50, 255)

    def draw(self, x, y, message, function=None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed(3)

        if x < self.mouse[0] < x + self.width and y < self.mouse[1] < y + self.heigth:
            pygame.draw.rect(screen, self.active_color, (x, y, self.width, self.heigth))
            pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)

            if self.click[0] is True:
                pygame.mixer.Sound.play(Button.button_sound)
                pygame.time.delay(300)

            if function is not None:
                self.function()
        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.heigth))
            pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)
        self.print_text(message, x + 5, y + 5)

    def print_text(self, message, x, y):
        self.text = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text, (x, y))

    def function(self):
        pass


class Menu:
    pygame.font.init()
    font = pygame.font.Font('segoepr.ttf', 42)
    def __init__(self):
        self.system_labels()
        self.buttons()

    def system_labels(self):
        pygame.draw.rect(screen, (100, 149, 237), (0, 20, width, 80))
        self.text = self.font.render('MAIN MENU', True, [0, 0, 0])
        screen.blit(self.text, (270, 25))

    def buttons(self):
        self.button_size = (240, 50)
        self.button_account = Button(self.button_size[0], self.button_size[1])
        self.button_account.draw((width / 2) - (self.button_size[0] / 2), 200, '  Personal Account')

        self.button_game = Button()
        self.button_game.draw((width / 2) - (self.button_size[0] / 2), 300, '      New Game')

        self.button_settings = Button()
        self.button_settings.draw((width / 2) - (self.button_size[0] / 2), 400, '        Settings')

        self.button_records = Button()
        self.button_records.draw((width / 2) - (self.button_size[0] / 2), 500, '   Table of Records')

        self.button_exit = Button()
        self.button_exit.draw((width / 2) - (self.button_size[0] / 2), 600, '        Logout')


if __name__ == '__main__':
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

    while running:
        Menu()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()
