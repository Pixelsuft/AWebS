import os
import json
import pygame
import socket
import subprocess
import ifconfig_show
import flask_server
import server
import simple_flask_server
import simple_server
from utils import *


port_filter = tuple(str(x) for x in range(10))
ip_filter = tuple(list(port_filter) + ['.'])


def get_default_ip() -> str:
    return config.get('host') or socket.gethostbyname(socket.gethostname())


def get_default_port() -> int:
    return config.get('port') or 8000


def parse_ip_info_windows(encoding_: str = get_encoding()) -> str:
    output = subprocess.check_output(
        'ipconfig',
        shell=True
    ).decode(encoding_, errors='replace').strip().split('\n')[1:]
    need_stop = False
    while not need_stop:
        need_stop = True
        for i_ in output.copy():
            i = i_.replace('\r', '')
            if not i.strip():
                output.remove(i_)
                need_stop = False
                break
    return '\n'.join(output)


def parse_ip_info_default(encoding_: str = get_encoding()) -> str:
    output = subprocess.check_output(
        'ifconfig',
        shell=True
    ).decode(encoding_, errors='replace').strip().split('\n')
    '''need_stop = False
    while not need_stop:
        need_stop = True
        for i_ in output.copy():
            i = i_.replace('\r', '')
            if not i.strip():
                output.remove(i_)
                need_stop = False
                break'''
    return '\n'.join(output).strip()


def parse_ip_info(encoding_: str = get_encoding()) -> str:
    return (parse_ip_info_windows if is_windows else parse_ip_info_default)(encoding_)


def show_ip_info(*args, **kwargs) -> None:
    ifconfig_show.main(*args, **kwargs)


def run_server(
        screen: pygame.Surface,
        host: str,
        port: int,
        use_flask: bool = False,
        run_simple_server: bool = False
) -> None:
    save_path = p('awebs.json')
    f = open(save_path, 'w')
    f.write(json.dumps({
        'host': host,
        'port': port,
        'encoding': get_encoding(),
        'flask': use_flask,
        'logger': not run_simple_server,
        'need_dir': get_need_dir()
    }))
    f.close()
    os.chdir(get_need_dir())
    if run_simple_server:
        if use_flask:
            simple_flask_server.main(host, port)
            os.chdir(app_path)
            return
        simple_server.main(host, port)
        os.chdir(app_path)
        return
    if use_flask:
        flask_server.main(screen, host, port)
        os.chdir(app_path)
        return
    server.main(screen, host, port)
    os.chdir(app_path)
    return
