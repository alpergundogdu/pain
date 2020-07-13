from math import cos, sin
from random import randint
from tkinter import HORIZONTAL, ROUND, TRUE, Button, IntVar, Scale

from .tool import Tool

LENGTH_MIN = 10
LENGTH_MAX = 200
SPEED_MIN = 1
SPEED_MAX = 10


class Spirograph(Tool):

    def __init__(self):
        self.center_x = None
        self.center_y = None
        self.prev_x = None
        self.prev_y = None
        self.step = 0
        self.arm_lengths = [IntVar(), IntVar(), IntVar()]
        self.arm_speeds = [IntVar(), IntVar(), IntVar()]
        self.arm_count = len(self.arm_lengths)
        self.randomize()

    def create_tool_options_widget(self, root):
        for i in range(self.arm_count):
            arm_length = self.arm_lengths[i]
            Scale(root, variable=arm_length,
                  label=f"Arm {i+1} length", orient=HORIZONTAL, from_=LENGTH_MIN, to=LENGTH_MAX).pack()
            arm_speed = self.arm_speeds[i]
            Scale(root, variable=arm_speed,
                  label=f"Arm {i+1} speed", orient=HORIZONTAL, from_=SPEED_MIN, to=SPEED_MAX).pack()
        Button(root, text="Randomize", command=self.randomize).pack()

    def calculate_for_step(self, step):
        pos_x = self.center_x
        pos_y = self.center_y
        for i in range(self.arm_count):
            angle = self.arm_speeds[i].get() * step
            length = self.arm_lengths[i].get()
            pos_x += cos(angle) * length
            pos_y += sin(angle) * length
        return pos_x, pos_y

    def randomize(self):
        for i in range(self.arm_count):
            self.arm_lengths[i].set(randint(LENGTH_MIN, LENGTH_MAX))
            self.arm_speeds[i].set(randint(SPEED_MIN, SPEED_MAX))

    def mouse_down(self, x, y):
        self.center_x = x
        self.center_y = y
        self.prev_x, self.prev_y = self.calculate_for_step(0)

    def mouse_move(self, x, y):
        self.step += 1
        x, y = self.calculate_for_step(self.step)
        self.canvas.create_line(self.prev_x, self.prev_y, x, y,
                                width=1, fill=self.color,
                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.prev_x = x
        self.prev_y = y

    def mouse_up(self):
        self.step = 0
