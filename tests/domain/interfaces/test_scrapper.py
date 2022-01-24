import pytest

from domain import Scrapper, Card


class ScrapperImplementation(Scrapper):
    def scrap_card(self, card: Card):
        pass


class TestScrapper:
    def test_scrapper_is_an_abstract_interface(self):
        # When
        with pytest.raises(TypeError, match="Can't instantiate abstract class"):
            Scrapper()

    def test_scrapper_implementation_has_a_method_called_scrap_card(self):
        # When
        scrapper = ScrapperImplementation()

        # Then
        assert hasattr(scrapper, "scrap_card")
        assert issubclass(ScrapperImplementation, Scrapper)
