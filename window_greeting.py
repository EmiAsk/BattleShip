import pygame
import sys

from os import path


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


class Button:
    pygame.init()
    button_sound = pygame.mixer.Sound('click_button.wav')
    font = pygame.font.Font('20008.ttf', 30)

    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        self.inactive_color = (100, 149, 237)
        self.active_color = (50, 50, 255)

    def draw(self, x, y, message, function=None):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed(3)
        self.image = load_image('button_inactive.jpg')
        self.image_two = load_image('button_active.jpg')

        if x < self.mouse[0] < x + self.width and y < self.mouse[1] < y + self.heigth:
            screen.blit(self.image, (x, y))
            pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)

            if self.click[0] is True and function is not None:
                pygame.mixer.Sound.play(Button.button_sound)
                pygame.time.delay(300)
                function()
        else:
            screen.blit(self.image_two, (x, y))
            pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)
        self.print_text(message, x + 5, y + 5)

    def print_text(self, message, x, y):
        self.text = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text, (x, y))

    def function(self):
        pass


class ProgramGreeting:
    pygame.font.init()
    font = pygame.font.Font('20008.ttf', 20)
    font_header = pygame.font.Font('20008.ttf', 70)

    def __init__(self):
        self.system_labels()

    def system_labels(self):
        self.text = self.font_header.render('BattleShip', True, [0, 0, 0])
        self.line = pygame.draw.line(screen, 'black', (150, 150), (640, 150), 3)
        screen.blit(self.text, (170, 60))

        self.button_size = (240, 50)

        self.button_login = Button(*self.button_size)
        self.button_login.draw(65, 350, '       Log in')

        self.button_signin = Button(*self.button_size)
        self.button_signin.draw(505, 350, '       Sign in')

        self.button_gameinfo = Button(*self.button_size)
        self.button_gameinfo.draw(65, 500, '   Game Info')

        self.button_developers = Button(*self.button_size)
        self.button_developers.draw(505, 500, '  Developers')

        self.button_exit = Button(*self.button_size)
        self.button_exit.draw(285, 600, '         Exit', self.button_exit_click)

    def button_exit_click(self):
        exit()


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
        ProgramGreeting()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()
