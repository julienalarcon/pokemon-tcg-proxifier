from abc import ABC, abstractmethod

from pokemon_tcg_proxifier.domain import Card


class Scrapper(ABC):
    @abstractmethod
    def scrap_card(self, card: Card) -> None:
        """Must be implemented by child classes"""
