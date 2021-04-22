import unittest
from configuration_manager import ConfigurationManager
from sarcasm_formatter import SarcasmFormatter

class TestCommandActions(unittest.TestCase):

    def setUp(self):
        self.configuration_manager = ConfigurationManager(SarcasmFormatter())
    
    def test_set_sarcasm_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.configuration_manager.handle_command("set-sarcasm abc")