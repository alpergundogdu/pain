from .pen import Pen

DEFAULT_LINE_WIDTH = 5


class Eraser(Pen):

    def mouse_move(self, x: int, y: int):
        self.color = 'white'
        super.mouse_move(x, y)
