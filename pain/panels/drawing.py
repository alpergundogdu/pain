from tkinter import BOTH, Canvas, Widget

from pain.events import Event, EventBus, EventType

from .panel import Panel


class Drawing(Panel):

    def __init__(self, root: Widget, event_bus: EventBus):
        self.event_bus = event_bus
        self.canvas = Canvas(root, bg='white', width=1200, height=600)
        self.canvas.bind('<Button-1>', self.mouse_down)
        self.canvas.bind('<B1-Motion>', self.mouse_move)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_up)
        self.canvas.pack(fill=BOTH)

    def start(self):
        self.event_bus.emit(Event(EventType.CANVAS_LOADED, [self.canvas]))

    def mouse_down(self, event):
        self.event_bus.emit(Event(EventType.MOUSE_DOWN, [event.x, event.y]))

    def mouse_move(self, event):
        self.event_bus.emit(Event(EventType.MOUSE_MOVE, [event.x, event.y]))

    def mouse_up(self, event):
        self.event_bus.emit(Event(EventType.MOUSE_UP, []))
