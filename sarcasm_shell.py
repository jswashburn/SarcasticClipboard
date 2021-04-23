import cmd
from datetime import datetime
from threading import Thread

# TODO: Command to display current formatter configuration

class SarcasmShell(cmd.Cmd):

    intro = """Welcome to the sarcastic cliboard!

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
        self.monitor.quit()

    def do_quit(self, line):
        """Stop the clipboard monitor and exit the interpreter"""
        self.stop_monitor()
        self.do_EOF(line)
    
    def do_pause(self, line):
        """Prevent further formatting of copied text until 'resume' is entered"""
        self.monitor.pause()

    def do_resume(self, line):
        """Resume formatting copied text"""
        self.monitor.resume()

    def do_set_variance(self, line):
        """Sets the casing variance of sarcastically formatted text.
A higher number will result in an angrier looking string -
0 means no formatting at all, 100 means all caps.
set_variance: INT"""
        variance = parse_int(line)
        self.monitor.config(lambda c: c.set_variance(variance))

    def do_pure_sarcasm(self, line):
        """Enabled by default.
Every other letter is swapcased, and formatting no longer
relies on variance.
pure_sarcasm {ON, OFF}"""
        if line == "on":
            self.monitor.config(lambda c: c.set_pure(True))
        elif line == "off":
            self.monitor.config(lambda c: c.set_pure(False))
    
    def do_EOF(self, line):
        return True

def parse_int(arg):
    if arg.isdigit():
        return int(arg)

def get_time_prompt():
    time = datetime.now().strftime("%H:%M:%S")
    return f"({time}): "