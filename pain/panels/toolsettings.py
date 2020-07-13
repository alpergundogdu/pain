from tkinter import LEFT, Frame, Label, Widget

from pain.events import Event, EventBus, EventListener, EventType

from .panel import Panel


class ToolSettings(Panel, EventListener):

    def __init__(self, root: Widget, event_bus: EventBus):
        self.tool_settings = Frame(root)
        self.tool_settings.pack(side=LEFT)

        self.tool_name = Label(self.tool_settings)
        self.tool_name.pack()

        self.tool_parameters = Frame(self.tool_settings)
        self.tool_parameters.pack()

        self.event_bus = event_bus
        self.event_bus.register(self, EventType.TOOL_CHANGED)

    def start(self):
        pass

    def on_event(self, event: Event):
        if event.type == EventType.TOOL_CHANGED:
            for child in self.tool_parameters.winfo_children():
                child.destroy()
            tool = event.args[0]
            tool.create_tool_options_widget(self.tool_parameters)
            self.tool_name.config(text=tool.__class__.__name__)
