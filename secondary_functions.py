import pygame
import config
from os import path
from error import ErrorForm

screen = pygame.display.set_mode(config.SIZE_WINDOW)

pygame.display.set_caption('BattleShip')
pygame.display.set_icon(pygame.image.load(config.IMAGE_ICON))
screen.blit(pygame.image.load(config.IMAGE_BACKGROUND), (0, 0))
pygame.display.flip()


def load_image(name):
    if not path.isfile(path.join(name)):
        ErrorForm().show()
    else:
        image = pygame.image.load(path.join(name))
        return image

def load_music():
    pygame.mixer.init()
    music = pygame.mixer.Sound('additional_files/music.mp3')
    pygame.mixer.Sound.play(music)

def game_exit():
    coordinate_y = screen.get_height()
    while coordinate_y > 10:
        pygame.display.set_mode((config.SIZE_WINDOW[0], coordinate_y))
        coordinate_y -= 1
    pygame.quit()
    quit()
