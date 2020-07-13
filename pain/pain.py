from tkinter import LEFT, RIGHT, Frame, Tk

from .events import EventBus
from .panels import ActionButtons, ColorBox, Drawing, ToolBox, ToolSettings


class Pain:

    def __init__(self):
        self.root = Tk()
        self.event_bus = EventBus()
        self.root.title('Pain')

        self.center = Frame(self.root)
        self.center.pack()

        self.sidebar = Frame(self.center)
        self.sidebar.pack(side=LEFT)

        self.main = Frame(self.center)
        self.main.pack(side=RIGHT)

        self.footer = Frame(self.root)
        self.footer.pack()

        self.panels = []
        self.panels.append(ToolSettings(self.sidebar, self.event_bus))
        self.panels.append(Drawing(self.main, self.event_bus))
        self.panels.append(ToolBox(self.footer, self.event_bus))
        self.panels.append(ColorBox(self.footer, self.event_bus))
        self.panels.append(ActionButtons(self.footer, self.event_bus))

    def run(self):
        for panel in self.panels:
            panel.start()
        self.root.mainloop()
