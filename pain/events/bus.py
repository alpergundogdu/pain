from .event import Event, EventListener, EventType


class EventBus:
    def __init__(self):
        self.listeners = {event_type: set() for event_type in EventType}

    def emit(self, event: Event):
        for listener in self.listeners.get(event.type):
            listener.on_event(event)

    def register(self, listener: EventListener, event_type: EventType):
        self.listeners.get(event_type).add(listener)

    def unregister(self, listener: EventListener, event_type: EventType):
        if listener in self.listeners.get(event_type):
            self.listeners.get(event_type).remove(listener)
