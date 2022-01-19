import os
import sys
import ctypes
import json
from android_utils import *


app_path = os.getcwd()
encoding = sys.getdefaultencoding() or 'utf-8'
is_windows = hasattr(ctypes, 'windll')
aa = True
default_fps = 10
need_dir = os.getcwd()


def read_cfg() -> dict:
    if not file_exists(p('awebs.json')):
        return {}
    f = open(p('awebs.json'), 'rb')
    result_ = json.loads(f.read().decode(get_encoding(), errors='replace'))
    f.close()
    return result_


def file_exists(fn: str) -> bool:
    return os.access(fn, os.F_OK) and not os.path.isdir(fn)


def get_need_dir() -> str:
    return need_dir


def change_location(*args, **kwargs) -> None:
    import location_changer
    global need_dir
    os.chdir(need_dir)
    location_changer.main(*args, **kwargs)
    need_dir = os.getcwd()
    os.chdir(app_path)
    return


def p(*path) -> str:
    return os.path.join(app_path, *path)


def set_encoding(new_encoding: str) -> None:
    global encoding
    encoding = new_encoding


def get_encoding() -> str:
    return encoding


def is_rect_c(xy: tuple, ltrb: tuple) -> bool:
    return ltrb[2] > xy[0] >= ltrb[0] and ltrb[3] > xy[1] >= ltrb[1]


def is_c(xy: tuple, ltwh: tuple, y_offset: int = 4) -> bool:
    return ltwh[2] + ltwh[0] > xy[0] >= ltwh[0] and ltwh[3] + ltwh[1] + y_offset > xy[1] >= ltwh[1] + y_offset


config = read_cfg()
set_encoding(config.get('encoding') or encoding)
need_dir = config.get('need_dir') or need_dir
