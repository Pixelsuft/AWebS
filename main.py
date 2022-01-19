import pygame
import main_menu
from utils import *


if __name__ == '__main__':
    try_permissions()
    pygame.init()
    screen = pygame.display.set_mode(
        (800, 480),
        force_fullscreen
    )
    pygame.display.set_caption('AWebS')
    pygame.display.set_icon(pygame.image.load(p('images', 'logo.png')))
    main_menu.main(screen)
    pygame.quit()
