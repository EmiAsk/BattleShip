# import sys
import pygame
import config


def draw():
    screen.fill((200, 200, 200))
    start_button = pygame.draw.rect(screen, (180, 180, 180), (580, 750, 120, 60), width=8)
    register_button = pygame.draw.rect(screen, (180, 180, 180), (150, 750, 120, 60), width=8)
    font = pygame.font.Font(None, 35)
    text_s = font.render("Sing in", True, (0, 0, 0))
    text_r = font.render("Sing up", True, (0, 0, 0))
    text_hello = font.render(config.hello, True, (0, 0, 0))
    screen.blit(text_s, (600, 767))
    screen.blit(text_r, (165, 767))
    screen.blit(text_hello, (370, 450))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Battleship')
    size = width, height = 900, 900
    screen = pygame.display.set_mode(size)
    draw()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > 150:
                    if mouse_pos[1] > 750:
                        if mouse_pos[0] < 120 + 150:
                            if mouse_pos[1] < 60 + 750:
                                # проверка работы
                                print(2)

                if mouse_pos[0] > 580:
                    if mouse_pos[1] > 750:
                        if mouse_pos[0] < 120 + 580:
                            if mouse_pos[1] < 60 + 750:
                                # проверка работы
                                print(1)
            pygame.display.flip()
    if event.type == pygame.MOUSEBUTTONUP:
        running = True
    else:
        running = False
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()