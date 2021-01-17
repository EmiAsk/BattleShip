import pygame
import config

pygame.init()
size = width, height = config.SIZE_WINDOW
screen = pygame.display.set_mode(size)


class Button:
    pygame.init()
    button_sound = pygame.mixer.Sound(config.BUTTON_SOUND)
    font = pygame.font.Font(config.FONT, 22)

    def __init__(self, width=350, height=50):
        self.width = width
        self.heigth = height
        self.color = config.SILVER_COLOR

    def move(self, x, y):
        mouse = pygame.mouse.get_pos()
        if (x < mouse[0] < x + self.width) and (y < mouse[1] < y + self.heigth):
            self.color = config.DARK_SILVER_COLOR
        else:
            self.color = config.SILVER_COLOR

    def press(self, x, y, function):
        click = pygame.mouse.get_pressed(3)
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.heigth:
            if click[0] is True:
                if function is not None:
                    pygame.mixer.Sound.play(Button.button_sound)
                    pygame.time.delay(300)
                    function()
                else:
                    return False

    def draw(self, x, y, message, function=None):
        pygame.draw.rect(screen, self.color, (x, y, self.width, self.heigth))
        pygame.draw.rect(screen, 'black', (x, y, self.width, self.heigth), 1)
        self.print_text(message, x + 20, y + 10)

    def print_text(self, message, x, y):
        self.text = self.font.render(message, True, [0, 0, 0])
        screen.blit(self.text, (x, y))
