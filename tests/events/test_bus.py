
from unittest import TestCase, mock

from pain.events import Event, EventBus, EventListener, EventType


class TestEventBus(TestCase):

    def setUp(self):
        self.event_bus = EventBus()
        self.listener1 = mock.create_autospec(spec=EventListener)
        self.listener2 = mock.create_autospec(spec=EventListener)

    def test_listener_channels(self):
        self.event_bus.register(self.listener1, EventType.CANVAS_LOADED)
        self.event_bus.register(self.listener2, EventType.TOOL_CHANGED)
        event1 = Event(EventType.CANVAS_LOADED, [None])
        self.event_bus.emit(event1)
        event2 = Event(EventType.TOOL_CHANGED, [None])
        self.event_bus.emit(event2)

        self.listener1.on_event.assert_called_with(event1)
        self.listener2.on_event.assert_called_with(event2)
