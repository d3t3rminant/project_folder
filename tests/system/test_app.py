import app
from unittest import TestCase
from unittest import mock


class TestApp(TestCase):
    def setUp(self) -> None:
        pass

    @mock.patch('builtins.print')
    def test_menu(self, mock_print):
        app.menu()
        mock_print.assert_called_once()

    def test_menu2(self):
        with mock.patch('builtins.print') as mocked_print:
            app.menu()
            mocked_print.assert_called_once()

    def test_menu_calls_print_blogs(self):
        with mock.patch('app.print_blogs') as mocked_print_blogs:
            app.menu()
            mocked_print_blogs.assert_called_once()

    def test_app_vypoctove_menu(self):
        suma = app.vypoctove_menu(1,2,3)
        self.assertEqual(suma, 0)

    def test_app_soucet_called(self):
        with mock.patch('app.soucet') as mocked_soucet:
            suma = app.vypoctove_menu(1,2,3)
            mocked_soucet.assert_called_once()

    @mock.patch('app.vypocet')
    def test_app_vypocet_called(self, mock_vypocet):
            suma = app.vypoctove_menu(1, 2, 3)
            mock_vypocet.assert_called_once()

