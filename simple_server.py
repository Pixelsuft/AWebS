import os
import contextlib
import socket
import http.server as hs
from functools import partial
from utils import *


def main(host: str, port: int):
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

    hs.test(
        HandlerClass=handler_class,
        ServerClass=DualStackServer,
        port=port,
        bind=host,
    )
