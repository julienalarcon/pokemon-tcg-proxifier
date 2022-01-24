import pytest

from domain import Printer


class PrinterImplementation(Printer):
    def print_deck(self):
        pass


class TestPrinter:
    def test_printer_is_an_abstract_interface(self):
        # When
        with pytest.raises(TypeError, match="Can't instantiate abstract class"):
            Printer()

    def test_printer_implementation_has_good_attributes_and_method(self):
        # When
        printer = PrinterImplementation()

        # Then
        assert hasattr(printer, "print_deck")
        assert printer.include_backcard is False
        assert issubclass(PrinterImplementation, Printer)
