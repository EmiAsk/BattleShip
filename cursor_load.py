import pygame

SIZE = WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode(SIZE)

if __name__ == "__main__":
    pygame.display.set_caption('Свой курсор мыши')
    image = pygame.image.load('cur.png')

    running = True
    pygame.mouse.set_visible(False)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                screen.fill(pygame.Color(166, 120, 65))
                if pygame.mouse.get_focused():
                    screen.blit(image, (event.pos))
                pygame.display.update()

    pygame.display.flip()
    pygame.quit()