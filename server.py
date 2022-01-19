import os
import sys
import time
import pygame
import contextlib
import socket
import http.server as hs
from functools import partial
from threading import Thread
from utils import *


def main(screen: pygame.Surface, host: str, port: int):
    width, height = screen.get_size()
    encoding_ = get_encoding()
    path_ = os.getcwd()
    line_height = 16
    half_line_height = round(line_height / 4)
    max_size = round(height / line_height) + 1
    font = pygame.font.Font(p('fonts', 'segoeuib.ttf'), 15)
    buffer = []

    handler_class = partial(
        hs.SimpleHTTPRequestHandler,
        directory=os.getcwd()
    )

    class DualStackServer(hs.ThreadingHTTPServer):
        def server_bind(self):
            with contextlib.suppress(Exception):
                self.socket.setsockopt(
                    socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
            return super().server_bind()

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

    Thread(target=lambda: hs.test(
        HandlerClass=handler_class,
        ServerClass=DualStackServer,
        port=port,
        bind=host,
    )).start()

    while True:
        pygame.event.get()
        time.sleep(0.25)
