import pygame
SIZE = WIDTH, HEIGHT = 900, 800


def program_quit():
    coordinate_y = HEIGHT
    while coordinate_y > 10:
        pygame.display.set_mode((WIDTH, coordinate_y))
        coordinate_y -= 1
    pygame.quit()

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('BattleShip')
pygame.display.set_icon(pygame.image.load("icon.png"))
music = pygame.mixer.Sound('music.mp3')
pygame.mixer.Sound.play(music)
pygame.mouse.set_visible(False)
image = pygame.image.load('cur.png')

work = True
while work:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_quit()
            work = False
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            screen.fill(pygame.Color(166, 120, 65))
            if pygame.mouse.get_focused():
                screen.blit(image, (event.pos))
            pygame.display.flip()

