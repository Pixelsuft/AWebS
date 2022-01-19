import pygame
import ip_tools
from fps_clock import FPS
from utils import *


def main(screen: pygame.Surface) -> None:
    width, height = screen.get_size()
    margin: int = 5

    title_render: dict = {
        'font': pygame.font.Font(p('fonts', 'segoescb.ttf'), 30),
        'pos': (0, 0),
        'size': (0, 0),
        'surface': screen
    }
    title_render['surface'] = title_render.get('font').render(
        'AWebS by Pixelsuft',
        aa,
        (0, 255, 0)
    )
    title_render['size'] = title_render.get('surface').get_size()
    title_render['pos'] = (round(width / 2 - title_render.get('size')[0] / 2), margin)

    host_input: dict = {
        'value': ip_tools.get_default_ip(),
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 20),
        'pos': (margin, margin * 2 + title_render.get('size')[1]),
        'size': (width - margin - margin, 20),
        'input': False
    }

    port_input: dict = {
        'value': str(ip_tools.get_default_port()),
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 20),
        'pos': (margin, host_input.get('pos')[1] + host_input.get('size')[1] + margin),
        'size': (width - margin - margin, 20),
        'input': False
    }

    encoding_input: dict = {
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 20),
        'pos': (margin, port_input.get('pos')[1] + port_input.get('size')[1] + margin),
        'size': (width - margin - margin, 20),
        'input': False
    }

    use_flask_check: dict = {
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 20),
        'pos': (0, 0),
        'size': (width - margin - margin, 20),
        'surface': screen,
        'checked': bool(config.get('flask'))
    }
    use_flask_check.get('checked')
    use_flask_check['surface'] = use_flask_check.get('font').render(
        '    Use flask instead of http.server',
        aa,
        (0, 0, 0)
    )
    use_flask_check['pos'] = (
        margin,
        encoding_input.get('pos')[1] + encoding_input.get('size')[1] + margin
    )

    show_logs: dict = {
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 20),
        'pos': (0, 0),
        'size': (width - margin - margin, 20),
        'surface': screen,
        'checked': bool(config.get('logger'))
    }
    show_logs.get('checked')
    show_logs['surface'] = show_logs.get('font').render(
        '    Show logs (Beta)',
        aa,
        (0, 0, 0)
    )
    show_logs['pos'] = (
        margin,
        use_flask_check.get('pos')[1] + use_flask_check.get('size')[1] + margin
    )

    ipconfig_button: dict = {
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 30),
        'pos': (0, 0),
        'size': (0, 0),
        'pos1': (0, 0),
        'size1': (0, 40),
        'surface': screen
    }
    ipconfig_button['surface'] = ipconfig_button.get('font').render(
        'Show Net Info',
        aa,
        (0, 255, 0)
    )
    ipconfig_button['size'] = ipconfig_button.get('surface').get_size()
    ipconfig_button['size1'] = (width - margin - margin, ipconfig_button.get('size')[1])
    ipconfig_button['pos'] = (
        round(width / 2 - ipconfig_button.get('size')[0] / 2),
        show_logs.get('pos')[1] + show_logs.get('size')[1] + margin + margin
    )
    ipconfig_button['pos1'] = (
        margin,
        ipconfig_button.get('pos')[1]
    )

    change_dir_button: dict = {
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 30),
        'pos': (0, 0),
        'size': (0, 0),
        'pos1': (0, 0),
        'size1': (0, 40),
        'surface': screen
    }
    change_dir_button['surface'] = change_dir_button.get('font').render(
        'Change Location',
        aa,
        (0, 255, 0)
    )
    change_dir_button['size'] = change_dir_button.get('surface').get_size()
    change_dir_button['size1'] = (width - margin - margin, change_dir_button.get('size')[1])
    change_dir_button['pos'] = (
        round(width / 2 - change_dir_button.get('size')[0] / 2),
        ipconfig_button.get('pos')[1] + ipconfig_button.get('size')[1] + margin + margin
    )
    change_dir_button['pos1'] = (
        margin,
        change_dir_button.get('pos')[1]
    )

    run_server_button: dict = {
        'font': pygame.font.Font(p('fonts', 'segoeuib.ttf'), 30),
        'pos': (0, 0),
        'size': (0, 0),
        'pos1': (0, 0),
        'size1': (0, 40),
        'surface': screen
    }
    run_server_button['surface'] = run_server_button.get('font').render(
        'Run Server!',
        aa,
        (0, 255, 0)
    )
    run_server_button['size'] = run_server_button.get('surface').get_size()
    run_server_button['size1'] = (width - margin - margin, run_server_button.get('size')[1])
    run_server_button['pos'] = (
        round(width / 2 - run_server_button.get('size')[0] / 2),
        change_dir_button.get('pos')[1] + change_dir_button.get('size')[1] + margin + margin
    )
    run_server_button['pos1'] = (
        margin,
        run_server_button.get('pos')[1]
    )

    clock = FPS(default_fps)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if is_c(
                        (x, y),
                        (*host_input.get('pos'), *host_input.get('size'))
                ):
                    port_input['input'] = False
                    encoding_input['input'] = False
                    host_input['input'] = True
                    pygame.key.start_text_input()
                    continue
                if is_c(
                        (x, y),
                        (*port_input.get('pos'), *port_input.get('size'))
                ):
                    host_input['input'] = False
                    encoding_input['input'] = False
                    port_input['input'] = True
                    pygame.key.start_text_input()
                    continue
                if is_c(
                        (x, y),
                        (*encoding_input.get('pos'), *encoding_input.get('size'))
                ):
                    host_input['input'] = False
                    port_input['input'] = False
                    encoding_input['input'] = True
                    pygame.key.start_text_input()
                    continue
                if host_input.get('input') or port_input.get('input') or encoding_input.get('input'):
                    host_input['input'] = False
                    port_input['input'] = False
                    encoding_input['input'] = False
                    pygame.key.stop_text_input()
                if is_c(
                        (x, y),
                        (*use_flask_check.get('pos'), *use_flask_check.get('size'))
                ):
                    use_flask_check['checked'] = not use_flask_check.get('checked')
                    continue
                if is_c(
                        (x, y),
                        (*show_logs.get('pos'), *show_logs.get('size'))
                ):
                    show_logs['checked'] = not show_logs.get('checked')
                    continue
                if is_c(
                        (x, y),
                        (*ipconfig_button.get('pos1'), *ipconfig_button.get('size1'))
                ):
                    ip_tools.show_ip_info(screen)
                    continue
                if is_c(
                        (x, y),
                        (*change_dir_button.get('pos1'), *change_dir_button.get('size1'))
                ):
                    change_location(screen)
                    continue
                if is_c(
                        (x, y),
                        (*run_server_button.get('pos1'), *run_server_button.get('size1'))
                ):
                    ip_tools.run_server(
                        screen,
                        host_input.get('value'),
                        int(port_input.get('value') or ip_tools.get_default_port()),
                        use_flask_check.get('checked'),
                        not show_logs.get('checked')
                    )
                    continue
            elif event.type == pygame.KEYDOWN:
                is_backspace = event.key == pygame.K_BACKSPACE
                if host_input.get('input'):
                    if is_backspace:
                        if len(host_input.get('value')) > 0:
                            host_input['value'] = host_input.get('value')[:-1]
                        continue
                    if event.unicode in ip_tools.ip_filter:
                        host_input['value'] += event.unicode
                    continue
                if port_input.get('input'):
                    if is_backspace:
                        if len(port_input.get('value')) > 0:
                            port_input['value'] = port_input.get('value')[:-1]
                        continue
                    if event.unicode in ip_tools.port_filter:
                        port_input['value'] += event.unicode
                    continue
                if encoding_input.get('input'):
                    if is_backspace:
                        if len(get_encoding()) > 0:
                            set_encoding(get_encoding()[:-1])
                        continue
                    if event.unicode:
                        set_encoding(get_encoding() + event.unicode)
                    continue
        if not clock.try_tick():
            continue

        screen.fill((192, 192, 192))
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                title_render['pos'][0],
                title_render['pos'][1],
                title_render['size'][0],
                title_render['size'][1]
            ),
            0,
            10
        )
        screen.blit(title_render['surface'], title_render['pos'])

        screen.blit(
            host_input['font'].render(
                f'IP Address: {host_input["value"]}{"|" if host_input.get("input") else ""}',
                aa,
                (0, 0, 0)
            ),
            host_input['pos']
        )

        screen.blit(
            port_input['font'].render(
                f'Port: {port_input["value"]}{"|" if port_input.get("input") else ""}',
                aa,
                (0, 0, 0)
            ),
            port_input['pos']
        )

        screen.blit(
            encoding_input['font'].render(
                f'Encoding: {get_encoding()}{"|" if encoding_input.get("input") else ""}',
                aa,
                (0, 0, 0)
            ),
            encoding_input['pos']
        )

        screen.blit(use_flask_check['surface'], use_flask_check['pos'])
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                use_flask_check['pos'][0],
                use_flask_check['pos'][1] + 5,
                20,
                20
            ),
            0,
            2
        )
        if use_flask_check['checked']:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (
                    use_flask_check['pos'][0] + 2,
                    use_flask_check['pos'][1] + 7,
                    16,
                    16
                ),
                0,
                4
            )

        screen.blit(show_logs['surface'], show_logs['pos'])
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                show_logs['pos'][0],
                show_logs['pos'][1] + 5,
                20,
                20
            ),
            0,
            2
        )
        if show_logs['checked']:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (
                    show_logs['pos'][0] + 2,
                    show_logs['pos'][1] + 7,
                    16,
                    16
                ),
                0,
                4
            )

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                ipconfig_button['pos1'][0],
                ipconfig_button['pos1'][1],
                ipconfig_button['size1'][0],
                ipconfig_button['size1'][1]
            ),
            0,
            5
        )
        screen.blit(ipconfig_button['surface'], ipconfig_button['pos'])

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                change_dir_button['pos1'][0],
                change_dir_button['pos1'][1],
                change_dir_button['size1'][0],
                change_dir_button['size1'][1]
            ),
            0,
            5
        )
        screen.blit(change_dir_button['surface'], change_dir_button['pos'])

        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                run_server_button['pos1'][0],
                run_server_button['pos1'][1],
                run_server_button['size1'][0],
                run_server_button['size1'][1]
            ),
            0,
            5
        )
        screen.blit(run_server_button['surface'], run_server_button['pos'])

        pygame.display.flip()
