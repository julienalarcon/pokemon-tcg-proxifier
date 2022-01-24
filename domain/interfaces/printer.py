from abc import ABC, abstractmethod


class Printer(ABC):
    def __init__(self):
        self.include_backcard = False

    @abstractmethod
    def print_deck(self):
        pass
