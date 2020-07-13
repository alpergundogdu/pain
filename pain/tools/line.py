from tkinter import HORIZONTAL, ROUND, TOP, TRUE, Frame, Scale, Widget

from .tool import Tool

DEFAULT_LINE_WIDTH = 5


class Line(Tool):
    def __init__(self):
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.line_width = DEFAULT_LINE_WIDTH

    def create_tool_options_widget(self, root: Widget):
        frame = Frame(root)
        frame.pack()
        choose_size_button = Scale(
            frame, from_=1, to=10, orient=HORIZONTAL, command=self.set_line_width)
        choose_size_button.pack(side=TOP)
        choose_size_button.set(self.line_width)

    def set_line_width(self, line_width: int):
        self.line_width = line_width

    def mouse_down(self, x, y):
        self.start_x = x
        self.start_y = y

    def mouse_move(self, x, y):
        self.end_x = x
        self.end_y = y

    def mouse_up(self):
        self.canvas.create_line(self.start_x, self.start_y, self.end_x, self.end_y,
                                width=self.line_width, fill=self.color,
                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
