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
    def __init__(self, width, height):
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
    def __init__(self, screen):
        self.system_labels()

    def system_labels(self):
        pygame.draw.rect(screen, (100, 149, 237), (0, 20, width, 80))
        self.text = self.font.render('MAIN MENU', True, [0, 0, 0])
        screen.blit(self.text, (270, 25))


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
        Menu(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        button_size = (240, 50)
        button_account = Button(button_size[0], button_size[1])
        button_account.draw((height / 2) - (button_size[0] / 4) - 10, 200, '  Personal Account')

        button_game = Button(240, 50)
        button_account.draw((height / 2) - (button_size[0] / 4) - 10, 300, '      New Game')

        button_settings = Button(240, 50)
        button_account.draw((height / 2) - (button_size[0] / 4) - 10, 400, '        Settings')

        button_records = Button(240, 50)
        button_account.draw((height / 2) - (button_size[0] / 4) - 10, 500, '   Table of Records')

        button_exit = Button(200, 50)
        button_account.draw((height / 2) - (button_size[0] / 4) - 10, 600, '        Logout')
    pygame.display.flip()
