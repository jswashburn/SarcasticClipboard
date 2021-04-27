import pyperclip

class ClipboardMonitorConfiguration:

    def __init__(self):
        self.format_on_copy = False
        self.paused = False
        self.requested_quit = False
    
    def quit(self):
        self.requested_quit = True

    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False
    
    def set_format_on_copy(self, format_on_copy):
        self.format_on_copy = format_on_copy
    
    def get_status(self):
        pause_status = "Monitor is{paused} paused".format(
            paused="" if self.paused else " NOT")
        return (pause_status,)

class ClipboardMonitor:
    
    def __init__(self, formatter, config):
        self.formatter = formatter
        self.config = config

    def configure(self, config_action):
        config_action(self.config)

    def configure_formatter(self, config_action):
        config_action(self.formatter.config)
    
    def get_formatter_config(self):
        return self.formatter.config

    def monitor_clipboard(self):
        while not self.config.requested_quit:
            # waitForNewPaste blocks, so
            # time it out in order to check if a cancellation was requested
            try:
                copied = pyperclip.waitForNewPaste(timeout=1)
                formatted = self.formatter.format(copied)
                if not self.config.paused:
                    pyperclip.copy(formatted)
            except pyperclip.PyperclipTimeoutException:
                continue