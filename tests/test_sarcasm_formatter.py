import unittest
from sarcasm_formatter import SarcasmFormatter

class TestSarcasmFormatter(unittest.TestCase):
    
    def setUp(self):
        self.formatter = SarcasmFormatter()
    
    def test_swaps_case(self):
        unformatted = "Swap Case"
        expected = "sWAP cASE"
        self.formatter.use_pure_sarcasm(False)
        self.formatter.variance = 100
        actual = self.formatter.format(unformatted)
        self.assertEqual(actual, expected)
    
    def test_returns_same_if_paused(self):
        unformatted = "Swap Case"
        expected = "Swap Case"
        self.formatter.is_paused = True
        actual = self.formatter.format(unformatted)
        self.assertEqual(actual, expected)
        self.formatter.is_paused = False
    
    def test_all_original_characters_preserved(self):
        unformatted = "Swap Case"
        actual = self.formatter.format(unformatted)
        self.assertEqual(len(actual), len(unformatted))