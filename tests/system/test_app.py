import app
import io, sys
from unittest import TestCase
from unittest import mock


class TestApp(TestCase):
    def setUp(self) -> None: # Runs before each test method
        pass

    @mock.patch('builtins.input', return_value = 0)
    def test_menu_calls_input(self, mocked_input):
        app.menu()
        mocked_input.assert_called_once()

    def test_menu_calls_input2(self): # Using context manager instead of decorator
        with mock.patch('builtins.input', return_value = 0) as mocked_input:
            app.menu()
            mocked_input.assert_called_once()

    def test_print_blogs(self):
        with mock.patch('builtins.input', side_effect = [1,0]) as mocked_input:
            with mock.patch('app.print_blogs') as mocked_print_blogs:
                app.menu()
                mocked_print_blogs.assert_called_once()


    def test_invalid_input(self):
        with mock.patch('builtins.input', side_effect = [-5, 10, 3, 5, 0]) as mocked_input:
            app.menu()
            self.assertEqual(mocked_input.call_count, 5)
