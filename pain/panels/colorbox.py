from functools import partial
from tkinter import LEFT, RIDGE, RIGHT, Canvas, Frame, Label, Widget, Y
from tkinter.colorchooser import askcolor

from pain.events import Event, EventBus, EventType

from .panel import Panel


class ColorBox(Panel):

    def __init__(self, root: Widget, event_bus: EventBus):
        self.color = '#000000'
        self.recent_colors = ['#FF0000', '#00FF00', '#0000FF',
                              '#FFFF00', '#FF00FF', '#00FFFF', '#FFFFFF', '#000000']
        self.recent_color_canvases = []

        self.colorbox = Frame(root, borderwidth=1, relief=RIDGE)
        self.colorbox.pack(side=LEFT, fill=Y, padx=5, pady=5)

        Label(self.colorbox, text='Colors').pack()

        recent_label = Label(self.colorbox, text='Recent: ')
        recent_label.pack(side=LEFT)

        for i in range(len(self.recent_colors) - 1):
            recent_color_canvas = Canvas(
                self.colorbox, bg=self.recent_colors[i], width=32, height=32)
            recent_color_canvas.pack(side=LEFT)
            recent_color_canvas.bind(
                '<ButtonRelease-1>', partial(self.pick_recent_color, i))
            self.recent_color_canvases.append(recent_color_canvas)

        current_label = Label(self.colorbox, text='Current: ')
        current_label.pack(side=LEFT)

        self.color_canvas = Canvas(
            self.colorbox, bg=self.color, width=32, height=32)
        self.color_canvas.pack(side=RIGHT)
        self.color_canvas.bind('<ButtonRelease-1>', self.choose_color)

        self.event_bus = event_bus

    def start(self):
        self.set_color(self.color)

    def emit_color(self):
        self.event_bus.emit(Event(EventType.COLOR_CHANGED, [self.color]))

    def choose_color(self, event):
        self.set_color(askcolor(color=self.color)[1])

    def set_color(self, color: str):
        self.color = color
        self.color_canvas.config(bg=color)
        found = False
        for i in range(len(self.recent_colors)):
            if self.recent_colors[i] == color:
                if i < len(self.recent_colors) - 1:
                    self.recent_colors = self.recent_colors[:i] + \
                        self.recent_colors[i+1:] + [color]
                found = True
                break
        if not found:
            self.recent_colors = self.recent_colors[1:] + [self.color]
        self.update_recent_colors()
        self.emit_color()

    def pick_recent_color(self, i, event):
        self.set_color(self.recent_colors[i])

    def update_recent_colors(self):
        for color, canvas in zip(self.recent_colors, self.recent_color_canvases):
            canvas.config(bg=color)
