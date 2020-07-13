from functools import partial
from tkinter import (
    LEFT, RAISED, RIDGE, SUNKEN, Button, Frame, Label, Widget, Y)

from pain.events import Event, EventBus, EventListener, EventType
from pain.tools import Eraser, Line, Pen, Rectangle, Spirograph, Tool

from .panel import Panel


class ToolBox(Panel, EventListener):

    def __init__(self, root: Widget, event_bus: EventBus):
        self.active_tool = None
        self.tools = [Pen(), Line(), Rectangle(), Spirograph(), Eraser()]
        self.tool_buttons = []

        self.toolbox = Frame(root, borderwidth=1, relief=RIDGE)
        self.toolbox.pack(side=LEFT, fill=Y, padx=5, pady=5)

        Label(self.toolbox, text='Tools').pack()

        for i in range(len(self.tools)):
            tool = self.tools[i]
            button = Button(self.toolbox, text=tool.__class__.__name__)
            button.config(command=partial(self.activate_tool, tool, button))
            button.pack(side=LEFT)
            self.tool_buttons.append(button)

        self.event_bus = event_bus
        self.event_bus.register(self, EventType.COLOR_CHANGED)
        self.event_bus.register(self, EventType.CANVAS_LOADED)
        self.event_bus.register(self, EventType.MOUSE_DOWN)
        self.event_bus.register(self, EventType.MOUSE_MOVE)
        self.event_bus.register(self, EventType.MOUSE_UP)

    def start(self):
        self.activate_tool(self.tools[0], self.tool_buttons[0])

    def activate_tool(self, tool: Tool, tool_button: Button):
        self.active_tool = tool
        for button in self.tool_buttons:
            button.config(relief=RAISED)
        tool_button.config(relief=SUNKEN)
        self.event_bus.emit(Event(EventType.TOOL_CHANGED, [tool]))

    def on_event(self, event: Event):
        if event.type == EventType.COLOR_CHANGED:
            for tool in self.tools:
                tool.set_color(event.args[0])
        if event.type == EventType.CANVAS_LOADED:
            for tool in self.tools:
                tool.set_canvas(event.args[0])
        if event.type == EventType.MOUSE_DOWN:
            self.active_tool.mouse_down(event.args[0], event.args[1])
        if event.type == EventType.MOUSE_MOVE:
            self.active_tool.mouse_move(event.args[0], event.args[1])
        if event.type == EventType.MOUSE_UP:
            self.active_tool.mouse_up()
