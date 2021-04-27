from clipboard_monitor import ClipboardMonitor, ClipboardMonitorConfiguration
from sarcasm_formatter import SarcasmFormatter, SarcasmFormatterConfiguration
from sarcasm_shell import SarcasmShell

# TODO: Add logging
# TODO: Write tests
# TODO: Add clipboard preview

if __name__ == '__main__':
    try:
        formatter = SarcasmFormatter(SarcasmFormatterConfiguration())
        monitor = ClipboardMonitor(formatter, ClipboardMonitorConfiguration())
        shell = SarcasmShell(monitor)

        shell.cmdloop()
    except KeyboardInterrupt:
        shell.stop_monitor()