import unittest
from clipboard_monitor import ClipboardMonitor
from sarcasm_formatter import SarcasmFormatter

class TestCommandActions(unittest.TestCase):

    def setUp(self):
        self.monitor = ClipboardMonitor(SarcasmFormatter())
    
    def test_set_sarcasm_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.monitor.handle_command("set-sarcasm abc")