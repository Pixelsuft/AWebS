import pygame
try:
    import android
    from android.permissions import request_permissions, Permission
    is_android = True
except ImportError:
    is_android = False


force_fullscreen = pygame.FULLSCREEN if is_android else 0


def try_permissions() -> None:
    if not is_android:
        return
    request_permissions([
        Permission.READ_EXTERNAL_STORAGE,
        Permission.WRITE_EXTERNAL_STORAGE
    ])
