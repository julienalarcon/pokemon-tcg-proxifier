import pytest

from pokemon_tcg_proxifier.domain import Printer


class PrinterImplementation(Printer):
    def print_deck(self):
        return None


class TestPrinter:
    def test_printer_is_an_abstract_interface(self):
        # When
        with pytest.raises(TypeError, match="Can't instantiate abstract class"):
            Printer()

    def test_printer_implementation_has_good_attributes_and_method(self):
        # When
        printer = PrinterImplementation()
        printer.print_deck()

        # Then
        assert hasattr(printer, "print_deck")
        assert printer.include_backcard is False
        assert issubclass(PrinterImplementation, Printer)
