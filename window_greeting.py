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


class ProgramGreeting:
    pygame.font.init()
    font = pygame.font.Font('segoepr.ttf', 70)

    def __init__(self):
        self.system_labels()

    def system_labels(self):
        self.text = self.font.render('BattleShip', True, [0, 0, 0])
        screen.blit(self.text, (190, 20))

        self.button_size = (240, 50)

        self.button_login = Button(*self.button_size)
        self.button_login.draw(70, 350, '        Log in')

        self.button_signin = Button(*self.button_size)
        self.button_signin.draw(500, 350, '        Sign in')

        self.button_gameinfo = Button(*self.button_size)
        self.button_gameinfo.draw(70, 500, '      Game Info')

        self.button_developers = Button(*self.button_size)
        self.button_developers.draw(500, 500, '       Developers')

        self.button_exit = Button(*self.button_size)
        self.button_exit.draw(280, 600, '         Exit')


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