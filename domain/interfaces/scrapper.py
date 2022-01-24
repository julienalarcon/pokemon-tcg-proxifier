from abc import ABC, abstractmethod

from domain import Card


class Scrapper(ABC):
    @abstractmethod
    def scrap_card(self, card: Card) -> None:
        pass
