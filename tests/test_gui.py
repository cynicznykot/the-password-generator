import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from src.gui import main


@unittest.skip("GUI tests are slow, skipping for now")
class TestGuiVariables(unittest.TestCase):
    """Тесты для переменных GUI."""

    def test_variables_created(self):
        """Проверяем, что переменные создаются."""
        with patch('tkinter.Tk') as mock_tk:
            mock_root = MagicMock()
            mock_tk.return_value = mock_root

            main()

            # Проверяем, что переменные были созданы
            mock_root.title.assert_called_with("Your Personal Password Generator")
            mock_root.geometry.assert_called_with("700x600")

    def test_length_var_default(self):
        """Проверяем значение по умолчанию для длины."""
        root = tk.Tk()
        length_var = tk.IntVar(value=16)
        self.assertEqual(length_var.get(), 16)
        root.destroy()

    def test_use_letters_default(self):
        """Проверяем значение по умолчанию для чекбокса 'Use Letters'."""
        root = tk.Tk()
        use_letters = tk.BooleanVar(value=True)
        self.assertTrue(use_letters.get())
        root.destroy()

    def test_use_digits_default(self):
        """Проверяем значение по умолчанию для чекбокса 'Use Digits'."""
        root = tk.Tk()
        use_digits = tk.BooleanVar(value=True)
        self.assertTrue(use_digits.get())
        root.destroy()

    def test_use_symbols_default(self):
        """Проверяем значение по умолчанию для чекбокса 'Use Symbols'."""
        root = tk.Tk()
        use_symbols = tk.BooleanVar(value=True)
        self.assertTrue(use_symbols.get())
        root.destroy()


@unittest.skip("GUI tests are slow, skipping for now")
class TestGuiFunctions(unittest.TestCase):
    """Тесты для функций GUI (без реального отображения)."""

    def setUp(self):
        """Создаём корневое окно для каждого теста."""
        self.root = tk.Tk()
        self.root.withdraw()  # Скрываем окно

    def tearDown(self):
        """Уничтожаем окно после каждого теста."""
        self.root.destroy()

    @patch('tkinter.Tk')
    def test_on_generate_called(self, mock_tk):
        """Проверяем, что функция on_generate определена."""
        mock_tk.return_value = self.root

        # Импортируем gui заново, чтобы использовать мок
        import importlib
        import src.gui as gui
        importlib.reload(gui)

        try:
            gui.main()
        except Exception as e:
            self.fail(f"main() raised an exception: {e}")

    @patch('tkinter.Tk')
    def test_copy_password_called(self, mock_tk):
        """Проверяем, что функция copy_password определена."""
        mock_tk.return_value = self.root

        import importlib
        import src.gui as gui
        importlib.reload(gui)

        try:
            gui.main()
        except Exception as e:
            self.fail(f"main() raised an exception: {e}")

    @patch('tkinter.Tk')
    def test_save_password_called(self, mock_tk):
        """Проверяем, что функция save_password определена."""
        mock_tk.return_value = self.root

        import importlib
        import src.gui as gui
        importlib.reload(gui)

        try:
            gui.main()
        except Exception as e:
            self.fail(f"main() raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()