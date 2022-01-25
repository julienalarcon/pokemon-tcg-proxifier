from dataclasses import dataclass, field
from typing import ClassVar, List


@dataclass
class Card:
    """Class to represent a single card."""

    extension_short_name: str
    extension_number: int
    image_path: str = ""


@dataclass
class Deck:
    """Class to represent a deck of 60 cards"""

    MAX_NUMBER_OF_CARDS: ClassVar[int] = 60
    cards: List[Card] = field(default_factory=list)

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def is_valid(self) -> bool:
        return len(self.cards) == Deck.MAX_NUMBER_OF_CARDS
