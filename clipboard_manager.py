import pyperclip

from sarcasm_formatter import SarcasmFormatter

class ClipboardManager:

    def __init__(self, formatter: SarcasmFormatter):
        self.formatter = formatter
        self.stopped = False
    
    def quit(self, future):
        print("clip quit called")
        self.stopped = True

    def do_sarcasm(self):
        copied = pyperclip.waitForNewPaste()
        sarcastic = self.formatter.format(copied)
        pyperclip.copy(sarcastic)

    def begin_sarcasm(self):
        while True:
            if self.stopped:
                print("clip quitting")
                return
            self.do_sarcasm()