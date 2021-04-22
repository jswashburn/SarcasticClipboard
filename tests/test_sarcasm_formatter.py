import unittest
from sarcasm_formatter import SarcasmFormatter

class TestSarcasmFormatter(unittest.TestCase):
    
    def setUp(self):
        self.formatter = SarcasmFormatter()
        self.formatter.variance = 100
    
    def test_swaps_case(self):
        unformatted = "Swap Case"
        expected = "sWAP cASE"
        actual = self.formatter.format(unformatted)
        self.assertEqual(actual, expected)
    
    def test_returns_same_if_paused(self):
        unformatted = "Swap Case"
        expected = "Swap Case"
        self.formatter.is_paused = True
        actual = self.formatter.format(unformatted)
        self.assertEqual(actual, expected)