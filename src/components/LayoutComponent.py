from .AbstractComponent import AbstractComponent


class GridComponent(AbstractComponent):
    def __init__(self):
        super().__init__()
        self.rows = 0
        self.cols = 0


class FrameComponent(AbstractComponent):
    def __init__(self):
        super().__init__()
