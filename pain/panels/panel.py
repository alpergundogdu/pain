from abc import ABC, abstractclassmethod


class Panel(ABC):

    @abstractclassmethod
    def start(cls):
        pass
