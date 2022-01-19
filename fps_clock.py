import time


class FPS:
    def __init__(
            self,
            fps: any
            ) -> None:
        self.fps = float(fps)
        self.fps_time = 1 / fps
        self.delta = self.fps_time
        self.last_tick = time.time()

    def try_tick(self) -> bool:
        now = time.time()
        if now < self.last_tick + self.fps_time:
            return False
        self.delta = now - self.last_tick
        self.last_tick = now
        return True

    def get_fps(self) -> float:
        try:
            return 1 / self.delta
        except ZeroDivisionError:
            return self.fps

    def get_fps_int(self) -> int:
        return round(self.get_fps())
