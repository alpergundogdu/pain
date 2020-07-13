from tkinter import (HORIZONTAL, TOP, BooleanVar, Checkbutton, Frame, IntVar,
                     Scale, Widget)

from .tool import Tool

DEFAULT_LINE_WIDTH = 5
GHOST_LINE_COLOR = '#ff00ff'


class Rectangle(Tool):
    def __init__(self):
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.line_width = IntVar(value=DEFAULT_LINE_WIDTH)
        self.fill = BooleanVar()

    def create_tool_options_widget(self, root: Widget):
        frame = Frame(root)
        frame.pack()
        fill_button = Checkbutton(frame, text="Fill", variable=self.fill)
        fill_button.pack()
        choose_size_button = Scale(
            frame, from_=1, to=10, orient=HORIZONTAL, variable=self.line_width)
        choose_size_button.pack(side=TOP)

    def mouse_down(self, x, y):
        self.start_x = x
        self.start_y = y

    def mouse_move(self, x, y):
        self.end_x = x
        self.end_y = y
        self.canvas.delete('ghostrect')
        self.canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y,
                                     width=self.line_width.get(), outline=GHOST_LINE_COLOR, tags=('ghostrect'))

    def mouse_up(self):
        self.canvas.delete('ghostrect')
        fill_color = self.color if self.fill.get() else ''
        self.canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y,
                                     width=self.line_width.get(), outline=self.color, fill=fill_color)
