import unittest
from clipboard_monitor import ClipboardMonitor
from sarcasm_formatter import SarcasmFormatter

class TestClipboardMonitorCommands(unittest.TestCase):

    def setUp(self):
        self.monitor = ClipboardMonitor(SarcasmFormatter())
    
    def test_parses_command_no_space(self):
        entered = "pause"
        expected = ("pause", "")
        actual = self.monitor.parse_command(entered)
        self.assertEqual(expected, actual)
    
    def test_parses_command_space_one_argument(self):
        entered = "set-sarcasm 34"
        expected = ("set-sarcasm", "34")
        actual = self.monitor.parse_command(entered)
        self.assertEqual(expected, actual)

    def test_parses_command_space_three_arguments(self):
        entered = "set-sarcasm 34 thirty four"
        expected = ("set-sarcasm", "34 thirty four")
        actual = self.monitor.parse_command(entered)
        self.assertEqual(expected, actual)
    
    def test_invalid_command_returns_false(self):
        entered = "poop"
        actual = self.monitor.is_valid_command(entered)
        self.assertFalse(actual)

    def test_valid_command_returns_true(self):
        entered = "quit"
        actual = self.monitor.is_valid_command(entered)
        self.assertTrue(actual)