
from constants import *
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    x = 5
    black = (0,0,0)
    while x != 0 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(black)
        pygame.display.flip()
        dt = time.tick(60)/1000
        print(dt)
        
    


if __name__ == "__main__":
    main()