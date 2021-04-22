from sarcasm_formatter import SarcasmFormatter

class ConfigurationManager:
    
    def __init__(self, formatter: SarcasmFormatter):
        self.formatter = formatter
        self.available_commands = [
            "pause",
            "resume",
            "quit",
            "help",
            "set-sarcasm"
        ]

        self.command_actions = {
            "pause": self.pause,
            "resume": self.resume,
            "quit": self.quit,
            "help": self.help,
            "set-sarcasm": self.set_variance,
        }

        self.stopped = False

    def help(self, args):
        print("Available Commands:")
        for command in self.available_commands:
            print("- " + command)
    
    def quit(self, args):
        print("config quit called")
        self.stopped = True
    
    def pause(self, args):
        self.formatter.is_paused = True

    def resume(self, args):
        self.formatter.is_paused = False

    def set_variance(self, args):
        if not args.isdigit():
            raise TypeError(args)
        self.formatter.variance = int(args)

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
    
    def start_input_loop(self):
        while True:
            if self.stopped:
                return
            command = input("> ")
            self.handle_command(command)