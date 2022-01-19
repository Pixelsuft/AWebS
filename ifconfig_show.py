import pygame
import ip_tools
from utils import *


def main(screen: pygame.Surface) -> None:
    width, height = screen.get_size()
    margin: int = 5
    ifconfig_text = ip_tools.parse_ip_info(get_encoding()).split('\n')
    line_height = 16
    font = pygame.font.Font(p('fonts', 'segoeuib.ttf'), 15)
    elements = []
    offset = 0
    step = 5

    back_button = {
        'pos': (margin, margin),
        'size': (line_height * 2, line_height * 2)
    }

    for line in ifconfig_text:
        elements.append(font.render(
            line,
            aa,
            (255, 255, 255)
        ))

    def draw_():
        screen.fill((0, 0, 0))
        for line_num, line_ in enumerate(elements):
            screen.blit(
                line_,
                (0, line_height * (offset + line_num))
            )
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (*back_button['pos'], *back_button['size']),
            0,
            2
        )
        pygame.display.flip()

    draw_()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if is_c((x, y), (*back_button['pos'], *back_button['size']), 0):
                    return
                offset += -step if y > round(height / 2) else step
                draw_()
