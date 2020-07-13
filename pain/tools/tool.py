from tkinter import Canvas, Widget


class Tool:
    color = None
    canvas = None

    def set_color(self, color):
        self.color = color

    def set_canvas(self, canvas: Canvas):
        self.canvas = canvas

    def save_canvas(self):
        pass

    def restore_canvas(self):
        pass

    def create_tool_options_widget(self, root: Widget):
        pass

    def mouse_down(self, x: int, y: int):
        pass

    def mouse_move(self, x: int, y: int):
        pass

    def mouse_up(self):
        pass
