import pygame
from player import Player
from constants import *

def main():
    pygame.init()

    #FPS
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Drawing the player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    #Exit using x button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    #Filling the screen and drawing the player
        screen.fill((0,0,0))
        player.draw(screen)

        player.update(dt)

    




    #Refreshes the page
        pygame.display.flip()



    # Cap at 60 fps
        player.update(dt)
        delta = clock.tick(60)

        dt = delta / 1000



if __name__ == "__main__":
    main()
