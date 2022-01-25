import pytest

from pokemon_tcg_proxifier.domain import Card, Deck


@pytest.fixture
def valid_card_list():
    cards = []

    for i in range(0, Deck.MAX_NUMBER_OF_CARDS):
        cards.append(Card("TEST", i))

    return cards


class TestCard:
    def test_card_has_expected_attributes_and_empty_image_by_default(self):
        # Given
        number = 23
        extension = "TEST"

        # When
        card = Card(extension_number=number, extension_short_name=extension)

        # Then
        assert card.extension_number == number
        assert card.extension_short_name == extension
        assert card.image_path == ""


class TestDeck:
    def test_deck_has_empty_cards_by_default(self):
        # When
        deck = Deck()

        # Then
        assert len(deck.cards) == 0

    def test_card_is_properly_added_in_deck(self):
        # Given
        deck = Deck()
        card = Card(extension_short_name="TEST", extension_number=23)

        # When
        deck.add_card(card)

        # Then
        assert len(deck.cards) == 1
        assert deck.cards[0] == card

    def test_deck_is_invalid_without_good_number_of_cards(self):
        # When
        deck = Deck()

        # Then
        assert deck.is_valid() is False

    def test_deck_is_valid_with_good_number_of_cards(self, valid_card_list):
        # When
        deck = Deck(cards=valid_card_list)

        # Then
        assert deck.is_valid() is True
