import os
import flask
from utils import *


def main(host: str, port: int):
    app = flask.Flask(__name__, static_folder=os.getcwd())
    encoding_ = get_encoding()
    path_ = os.getcwd()

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

    app.run(
        host,
        port=port,
        debug=False
    )
