from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from enum import Enum
from typing import List


class EventType(Enum):
    TOOL_CHANGED = 1   # Event args: [Tool]
    COLOR_CHANGED = 2  # Event args: [Color]
    CANVAS_LOADED = 3  # Event args: [Canvas]
    MOUSE_DOWN = 4     # Event args: [X, Y]
    MOUSE_MOVE = 5     # Event args: [X, Y]
    MOUSE_UP = 6       # Event args: [X, Y]


@dataclass
class Event:
    type: EventType
    args: List[object]


class EventListener(ABC):

    @abstractclassmethod
    def on_event(cls, event):
        pass
