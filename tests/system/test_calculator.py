import calculator
from unittest import TestCase, mock

class TestCalculator(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_soucet_input_mocked(self):
        with mock.patch('builtins.input') as mocked_input:
            mocked_input.side_effect = 5,10
            suma = calculator.soucet_input()
            self.assertEqual(suma, 15)

    @mock.patch('builtins.input', side_effect=(5,10))
    def test_soucet_input_mocked2(self, mocked_input):
        suma = calculator.soucet_input()
        self.assertEqual(suma, 15)

    def test_soucet_in_soucet_input(self):
        with mock.patch('calculator.soucet') as mocked_soucet:
            with mock.patch('builtins.input', side_effect=(5,10)) as mocked_input:
                calculator.soucet_input()
                mocked_soucet.assert_called_once()

    @mock.patch('builtins.input', side_effect=[5,10])
    def test_soucet_input_called_with_arguements(self, mocked_input):
        calculator.soucet_input()
        assert mocked_input.mock_calls[0] == mock.call("Enter your first number")
        assert mocked_input.mock_calls[1] == mock.call("Enter your second number")