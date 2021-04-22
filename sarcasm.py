import concurrent.futures

from clipboard_manager import ClipboardManager
from configuration_manager import ConfigurationManager
from sarcasm_formatter import SarcasmFormatter

def main():
    formatter = SarcasmFormatter()
    config_manager = ConfigurationManager(formatter)
    clip_manager = ClipboardManager(formatter)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(config_manager.start_input_loop).add_done_callback(clip_manager.quit)
        executor.submit(clip_manager.begin_sarcasm)

# TODO: Figure out graceful exiting of both threads

if __name__ == "__main__":
    main()