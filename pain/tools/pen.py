from tkinter import HORIZONTAL, ROUND, TOP, TRUE, Frame, Scale, Widget

from .tool import Tool

DEFAULT_LINE_WIDTH = 5


class Pen(Tool):
    def __init__(self):
        self.line_width = DEFAULT_LINE_WIDTH
        self.old_x = None
        self.old_y = None

    def create_tool_options_widget(self, root: Widget):
        frame = Frame(root)
        frame.pack()
        choose_size_button = Scale(
            frame, from_=1, to=100, orient=HORIZONTAL, command=self.set_line_width)
        choose_size_button.pack(side=TOP)
        choose_size_button.set(self.line_width)

    def set_line_width(self, line_width: int):
        self.line_width = line_width

    def mouse_down(self, x: int, y: int):
        self.old_x = x
        self.old_y = y

    def mouse_move(self, x: int, y: int):
        self.canvas.create_line(self.old_x, self.old_y, x, y,
                                width=self.line_width, fill=self.color,
                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = x
        self.old_y = y
