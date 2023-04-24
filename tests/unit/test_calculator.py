import calculator
from unittest import TestCase


class TestCalculator(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_soucet(self):
        suma = calculator.soucet(1, 2)
        self.assertEqual(suma, 3)