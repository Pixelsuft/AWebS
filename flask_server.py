import os
import sys
import flask
import pygame
import time
from threading import Thread
from utils import *


def main(screen: pygame.Surface, host: str, port: int):
    width, height = screen.get_size()
    app = flask.Flask(__name__, static_folder=os.getcwd())
    encoding_ = get_encoding()
    path_ = os.getcwd()
    line_height = 16
    half_line_height = round(line_height / 4)
    max_size = round(height / line_height) + 1
    font = pygame.font.Font(p('fonts', 'segoeuib.ttf'), 15)
    buffer = []

    def fast_read(fn: str) -> str:
        f_ = open(fn, 'rb')
        result = f_.read()
        f_.close()
        return result.decode(encoding_, errors='replace')

    def error404() -> any:
        error404_path = os.path.join(path_, '404.html')
        if file_exists(error404_path):
            return fast_read('404.html'), 404
        return 'Error 404'

    def get_path_from_url(url_: str) -> str:
        return '/'.join(url_.split('/')[3:])

    def file_exists(fn: str) -> bool:
        return os.access(fn, os.F_OK) and not os.path.isdir(fn)

    def try_render(fn: str) -> tuple:
        full_path = os.path.join(path_, fn)
        if file_exists(full_path):
            return fast_read(full_path), 200
        return error404()

    @app.errorhandler(404)
    def get_page(*args, **kwargs) -> any:
        url = flask.request.url
        path = get_path_from_url(url)
        if not path:
            return try_render('index.html')
        ext = url.split('.')[-1].lower().strip()
        if ext in ('html', 'htm'):
            return try_render(path)
        if file_exists(os.path.join(path_, path)):
            return app.send_static_file(path), 200
        return try_render(get_path_from_url(url + 'index.html'))

    def write_handle(*args, please_do_not_use_this_arg__: tuple = (255, 255, 255), **kwargs):
        pygame.event.get()
        for l_ in bytes(*args).decode(encoding_, errors='replace').split('\n')\
                if type(*args) == bytes else str(*args).split('\n'):
            buffer.append(font.render(
                l_,
                aa,
                please_do_not_use_this_arg__
            ))
        while len(buffer) > max_size:
            buffer.pop(0)
        screen.fill((0, 0, 0))
        for line_num, line_ in enumerate(buffer):
            screen.blit(line_, (0, line_num * line_height - half_line_height))
        pygame.display.flip()

    sys.stdout.write = write_handle
    sys.stderr.write = lambda *args, **kwargs: write_handle(*args, **kwargs, please_do_not_use_this_arg__=(255, 0, 0))
    print('Welcome to the AWebS log console!')

    Thread(target=app.run(
        host,
        port=port,
        debug=False
    )).start()

    while True:
        pygame.event.get()
        time.sleep(1)
