from threading import Thread
from sarcasm_formatter import SarcasmFormatter

# TODO: find a way to factor out all the command parsing stuff (maybe a command_parser.handle_command(input))

import pyperclip

class ClipboardMonitor:
    
    def __init__(self, formatter: SarcasmFormatter):
        self.formatter = formatter
        self.available_commands = [
            "pause",
            "resume",
            "quit",
            "help",
            "pure-sarcasm",
            "set-sarcasm"
        ]

        self.command_actions = {
            "pause": self.pause,
            "resume": self.resume,
            "quit": self.quit,
            "help": self.help,
            "pure-sarcasm": self.enable_pure_sarcasm,
            "set-sarcasm": self.set_variance,
        }

        self.requested_quit = False

    def help(self, args):
        print("Available Commands:")
        for command in self.available_commands:
            print("- " + command)
    
    def quit(self, args):
        self.requested_quit = True
    
    def pause(self, args):
        self.formatter.is_paused = True

    def resume(self, args):
        self.formatter.is_paused = False

    def set_variance(self, args):
        if not args.isdigit():
            raise TypeError(args)
        self.formatter.variance = int(args)

    def enable_pure_sarcasm(self, args):
        if args.lower() == "on":
            self.formatter.use_pure_sarcasm(True)
        elif args.lower() == "off":
            self.formatter.use_pure_sarcasm(False)

    def is_valid_command(self, command):
        return command in self.available_commands

    def parse_command(self, command):
        split = command.split(" ", 1)
        command = split[0]
        args = ""
        if len(split) == 2:
            args = split[1]
        
        return command, args

    def handle_command(self, command):
        command, args = self.parse_command(command)
        if self.is_valid_command(command):
            self.command_actions[command](args)

    def monitor_clipboard(self):
        while True:
            if self.requested_quit:
                return
            try:
                copied = pyperclip.waitForNewPaste(1)
                formatted = self.formatter.format(copied)
                pyperclip.copy(formatted)
            except pyperclip.PyperclipTimeoutException:
                continue

    def start(self):
        clipboard_monitor = Thread(target=self.monitor_clipboard)
        clipboard_monitor.start()
        while True:
            if self.requested_quit:
                break

            command = input("> ")
            self.handle_command(command)