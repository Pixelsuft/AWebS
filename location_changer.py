import os
import pygame
from fps_clock import FPS
from utils import *


def main(screen: pygame.Surface) -> None:
    width, height = screen.get_size()
    margin: int = 5

    path_input: dict = {
        'value': os.getcwd(),
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 20),
        'pos': (margin, margin + 20),
        'size': (width - margin - margin, 20),
        'input': False
    }

    go_button: dict = {
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 30),
        'pos': (0, 0),
        'size': (0, 0),
        'pos1': (0, 0),
        'size1': (0, 40),
        'surface': screen
    }
    go_button['surface'] = go_button.get('font').render(
        'Go!',
        aa,
        (0, 255, 0)
    )
    go_button['size'] = go_button.get('surface').get_size()
    go_button['size1'] = (round(width / 2 - margin / 2 - margin), go_button.get('size')[1])
    go_button['pos'] = (
        round(width / 4 - go_button.get('size')[0] / 2),
        path_input.get('pos')[1] + path_input.get('size')[1] + margin + margin
    )
    go_button['pos1'] = (
        margin,
        go_button.get('pos')[1]
    )

    ok_button: dict = {
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 30),
        'pos': (0, 0),
        'size': (0, 0),
        'pos1': (0, 0),
        'size1': (0, 40),
        'surface': screen
    }
    ok_button['surface'] = ok_button.get('font').render(
        'Ok!',
        aa,
        (0, 255, 0)
    )
    ok_button['size'] = ok_button.get('surface').get_size()
    ok_button['size1'] = (round(width / 2 - margin / 2 - margin), ok_button.get('size')[1])
    ok_button['pos'] = (
        round(width / 4 * 3 - ok_button.get('size')[0] / 2),
        path_input.get('pos')[1] + path_input.get('size')[1] + margin + margin
    )
    ok_button['pos1'] = (
        round(width / 2 + margin / 2),
        ok_button.get('pos')[1]
    )

    down_button: dict = {
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 30),
        'pos': (0, 0),
        'size': (0, 0),
        'pos1': (0, 0),
        'size1': (0, 40),
        'surface': screen
    }
    down_button['surface'] = down_button.get('font').render(
        'Down',
        aa,
        (0, 255, 0)
    )
    down_button['size'] = down_button.get('surface').get_size()
    down_button['size1'] = (round(width / 2 - margin / 2 - margin), down_button.get('size')[1])
    down_button['pos'] = (
        round(width / 4 - down_button.get('size')[0] / 2),
        go_button.get('pos')[1] + go_button.get('size')[1] + margin + margin
    )
    down_button['pos1'] = (
        margin,
        down_button.get('pos')[1]
    )

    up_button: dict = {
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 30),
        'pos': (0, 0),
        'size': (0, 0),
        'pos1': (0, 0),
        'size1': (0, 40),
        'surface': screen
    }
    up_button['surface'] = up_button.get('font').render(
        'Up',
        aa,
        (0, 255, 0)
    )
    up_button['size'] = up_button.get('surface').get_size()
    up_button['size1'] = (round(width / 2 - margin / 2 - margin), up_button.get('size')[1])
    up_button['pos'] = (
        round(width / 4 * 3 - up_button.get('size')[0] / 2),
        ok_button.get('pos')[1] + ok_button.get('size')[1] + margin + margin
    )
    up_button['pos1'] = (
        round(width / 2 + margin / 2),
        up_button.get('pos')[1]
    )

    offset = 0
    step = 5
    line_height = 16
    need_pos = down_button.get('pos1')[1] + down_button.get('size1')[1] + margin
    max_size = int(height - need_pos - margin)
    font = pygame.font.Font(p('fonts', 'segoeuib.ttf'), 15)
    dirs = []

    def rescan_dirs() -> None:
        dirs.clear()
        try:
            dirs.append((
                '..',
                font.render(
                    'Go Back',
                    aa,
                    (0, 0, 0)
                )
            ))
            for dir_ in os.listdir(os.getcwd()):
                try:
                    if not os.path.isdir(dir_):
                        continue
                    dirs.append((
                        dir_,
                        font.render(
                            dir_,
                            aa,
                            (0, 0, 0)
                        )
                    ))
                except Exception as err__:
                    if err__:
                        continue
        except Exception as err__:
            dirs.clear()
            dirs.append('..')
            if err__:
                'continue'
    rescan_dirs()

    clock = FPS(default_fps)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if is_c(
                        (x, y),
                        (*path_input.get('pos'), *path_input.get('size'))
                ):
                    path_input['input'] = True
                    pygame.key.start_text_input()
                    continue
                if path_input.get('input'):
                    path_input['input'] = False
                    pygame.key.stop_text_input()
                if is_c((x, y), (*go_button.get('pos1'), *go_button.get('size1'), 0)):
                    try:
                        os.chdir(path_input.get('value'))
                        rescan_dirs()
                    except Exception as err_:
                        path_input['value'] = os.getcwd()
                        if err_:
                            continue
                    continue
                if is_c((x, y), (*ok_button.get('pos1'), *ok_button.get('size1'), 0)):
                    try:
                        os.chdir(path_input.get('value'))
                    except Exception as err_:
                        path_input['value'] = os.getcwd()
                        if err_:
                            continue
                    return
                if is_c((x, y), (*down_button.get('pos1'), *down_button.get('size1'), 0)):
                    offset += step
                    continue
                if is_c((x, y), (*up_button.get('pos1'), *up_button.get('size1'), 0)):
                    if offset > 0:
                        offset -= step
                    continue
                if not (height - margin > y > need_pos):
                    continue
                try:
                    need_to_change = dirs[round((y + 4 - need_pos) / line_height) - 1][0]
                except IndexError:
                    continue
                try:
                    os.chdir(os.path.join(os.getcwd(), need_to_change))
                    path_input['value'] = os.getcwd()
                    rescan_dirs()
                except Exception as err___:
                    if err___ or True:
                        path_input['value'] = os.getcwd()
            elif event.type == pygame.KEYDOWN:
                is_backspace = event.key == pygame.K_BACKSPACE
                if path_input.get('input'):
                    if is_backspace:
                        if len(path_input.get('value')) > 0:
                            path_input['value'] = path_input.get('value')[:-1]
                        continue
                    if event.unicode:
                        path_input['value'] += event.unicode
                    continue

        if not clock.try_tick():
            continue

        screen.fill((192, 192, 192))

        screen.blit(
            path_input['font'].render(
                f'{path_input["value"]}{"|" if path_input.get("input") else ""}',
                aa,
                (0, 0, 0)
            ),
            path_input['pos']
        )

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                go_button['pos1'][0],
                go_button['pos1'][1],
                go_button['size1'][0],
                go_button['size1'][1]
            ),
            0,
            5
        )
        screen.blit(go_button['surface'], go_button['pos'])

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                ok_button['pos1'][0],
                ok_button['pos1'][1],
                ok_button['size1'][0],
                ok_button['size1'][1]
            ),
            0,
            5
        )
        screen.blit(ok_button['surface'], ok_button['pos'])

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                down_button['pos1'][0],
                down_button['pos1'][1],
                down_button['size1'][0],
                down_button['size1'][1]
            ),
            0,
            5
        )
        screen.blit(down_button['surface'], down_button['pos'])

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                up_button['pos1'][0],
                up_button['pos1'][1],
                up_button['size1'][0],
                up_button['size1'][1]
            ),
            0,
            5
        )
        screen.blit(up_button['surface'], up_button['pos'])

        for line_num, line in enumerate(dirs[offset:] if offset > 0 else dirs):
            screen.blit(line[1], (margin, need_pos + line_num * line_height))

        pygame.display.flip()
