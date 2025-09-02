import pygame
import sys
from const import *




def main() :
    pygame.init()

    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps = pygame.time.Clock()

    running = True

    while running :

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        surface.fill(BLACK)

        start_x = SCREEN_WIDTH / 2 - (26 * 9) / 2
        start_y = SCREEN_HEIGHT / 2 - (26 * 9) / 2

        size = int(SCREEN_HEIGHT / 9)

        for y in range(9) :
            for x in range(9) :
                rect = (start_x + x * size, start_y + y * size, size + 1, size + 1)
                pygame.draw.rect(surface, WHITE, rect, 1)

        pygame.display.flip()

        fps.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()