import pygame

def draw():
    num = 0
    pygame.font.init()
    loading_text = ['Loading', 'Loading.', 'Loading..', 'Loading...']
    while num != 100:
        num += 1
        screen.fill((0, 0, 0))
        font = pygame.font.Font('segoepr.ttf', 40)
        text_load = font.render(loading_text[num % 4], True, (255, 255, 255))

        pygame.draw.rect(screen, 'white', (220, 300, 300, 40), 1)
        pygame.draw.rect(screen, 'green', (220, 300, 3 * num, 40), 0)

        text = font.render(f'{num}%', True, (255, 255, 255))
        screen.blit(text, (530, 285))
        screen.blit(text_load, (300, 235))
        pygame.time.delay(70)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 700
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    clock = pygame.time.Clock()
    fps = 30
    running = True
    draw()
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

