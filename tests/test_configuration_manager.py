import unittest
from configuration_manager import ConfigurationManager
from sarcasm_formatter import SarcasmFormatter

class TestConfigurationManager(unittest.TestCase):

    def setUp(self):
        self.configuration_manager = ConfigurationManager(SarcasmFormatter())
    
    def test_parses_command_no_space(self):
        entered = "pause"
        expected = ("pause", "")
        actual = self.configuration_manager.parse_command(entered)
        self.assertEqual(expected, actual)
    
    def test_parses_command_space_one_argument(self):
        entered = "set-sarcasm 34"
        expected = ("set-sarcasm", "34")
        actual = self.configuration_manager.parse_command(entered)
        self.assertEqual(expected, actual)

    def test_parses_command_space_three_arguments(self):
        entered = "set-sarcasm 34 thirty four"
        expected = ("set-sarcasm", "34 thirty four")
        actual = self.configuration_manager.parse_command(entered)
        self.assertEqual(expected, actual)
    
    def test_invalid_command_returns_false(self):
        entered = "poop"
        actual = self.configuration_manager.is_valid_command(entered)
        self.assertFalse(actual)

    def test_valid_command_returns_true(self):
        entered = "quit"
        actual = self.configuration_manager.is_valid_command(entered)
        self.assertTrue(actual)