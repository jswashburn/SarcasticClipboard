import pyperclip

class ClipboardMonitor:
    
    def __init__(self, formatter):
        self.formatter = formatter
        self.requested_quit = False
        self.paused = False

    def config(self, config_action):
        config_action(self.formatter.config)
    
    def get_formatter_config(self):
        return self.formatter.config
    
    def get_config_status(self):
        pause_status = "Monitor is{paused} paused".format(
            paused="" if self.paused else " NOT")
        return (pause_status,)

    def quit(self):
        self.requested_quit = True

    def pause(self):
        self.paused = True
    
    def resume(self):
        self.paused = False

    def monitor_clipboard(self):
        while not self.requested_quit:
            # waitForNewPaste blocks, so
            # time it out in order to check if a cancellation was requested
            try:
                copied = pyperclip.waitForNewPaste(timeout=1)
                formatted = self.formatter.format(copied)
                if not self.paused:
                    pyperclip.copy(formatted)
            except pyperclip.PyperclipTimeoutException:
                continue