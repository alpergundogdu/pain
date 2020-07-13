from tkinter import LEFT, RIDGE, Button, Frame, Widget, Y
from tkinter.filedialog import asksaveasfilename

from pain.events import Event, EventBus, EventListener, EventType

from .panel import Panel


class ActionButtons(Panel, EventListener):

    def __init__(self, root: Widget, event_bus: EventBus):
        self.canvas = None
        self.frame = Frame(root, borderwidth=1, relief=RIDGE)
        self.frame.pack(side=LEFT, fill=Y, padx=5, pady=5)

        self.button = Button(self.frame, text='Save', command=self.save)
        self.button.pack(side=LEFT, fill=Y, padx=5, pady=5)

        self.button = Button(self.frame, text='Clear', command=self.clear)
        self.button.pack(side=LEFT, fill=Y, padx=5, pady=5)

        self.event_bus = event_bus
        self.event_bus.register(self, EventType.CANVAS_LOADED)

    def start(self):
        pass

    def on_event(self, event: Event):
        if event.type == EventType.CANVAS_LOADED:
            self.canvas = event.args[0]

    def save(self):
        self.canvas.postscript(file=asksaveasfilename(initialfile='image.ps', defaultextension='.ps', filetypes=[
                               ("All Files", "*.*"), ("Postscript", "*.ps")]), colormode='color')

    def clear(self):
        self.canvas.delete("all")
