from clipboard_monitor import ClipboardMonitor
from sarcasm_formatter import SarcasmFormatter

if __name__ == "__main__":
    monitor = ClipboardMonitor(SarcasmFormatter())
    monitor.start()