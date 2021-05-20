import cmd
import sys
from datetime import datetime
from threading import Thread

def parse_int(arg):
    if arg.isdigit():
        return int(arg)

def get_time_prompt():
    time = datetime.now().strftime("%H:%M:%S")
    return f"({time}): "

class SarcasmShell(cmd.Cmd):

    intro = """
Welcome to the sarcastic clipboard!

Copy some text and when you paste, it will be formatted sArCastIclY.
Enter 'help' for a list of available configuration commands.
Enter 'quit' to gracefully exit, or just close the interpreter.

Please use sarcasm responsibly.
"""

    prompt = get_time_prompt()

    def __init__(self, monitor):
        self.monitor = monitor
        self.monitor_thread = Thread(target=self.monitor.monitor_clipboard) 
        super().__init__()

    def emptyline(self):
        # run when no command is entered, by default repeats last command.
        # disable this behavior with pass
        pass

    def preloop(self):
        self.start_monitor()
    
    def postloop(self):
        self.stop_monitor()

    def postcmd(self, stop, line):
        self.prompt = get_time_prompt()

    def start_monitor(self):
        self.monitor_thread.start()
    
    def stop_monitor(self):
        self.monitor.config.quit()

    def do_quit(self, line):
        """Stop the clipboard monitor and exit the interpreter"""
        self.stop_monitor()
        sys.exit()
    
    def do_pause(self, line):
        """Prevent further formatting of copied text until 'resume' is entered"""
        self.monitor.configure(lambda c: c.pause())

    def do_resume(self, line):
        """Resume formatting copied text"""
        self.monitor.configure(lambda c: c.resume())

    def do_set_variance(self, line):
        """Sets the casing variance of sarcastically formatted text.
A higher number will result in an angrier looking string -
0 means no formatting at all, 100 means all caps.
set_variance: INT"""
        variance = parse_int(line)
        self.monitor.configure_formatter(lambda c: c.set_variance(variance))

    def do_pure_sarcasm(self, line):
        """Enabled by default.
Every other letter is swapcased, and formatting no longer
relies on variance.
pure_sarcasm {ON, OFF}"""
        if line == "on":
            self.monitor.configure_formatter(lambda c: c.set_pure(True))
        elif line == "off":
            self.monitor.configure_formatter(lambda c: c.set_pure(False))

    def do_settings(self, line):
        """Display current settings"""
        formatter_settings = self.monitor.get_formatter_config().get_status()
        monitor_settings = self.monitor.config.get_status()

        current_settings = "\n".join(setting for setting in formatter_settings) + "\n"
        current_settings += "\n".join(setting for setting in monitor_settings)

        print(current_settings)

    def do_EOF(self, line):
        return True