# SarcasticClipboard
Copy text, and paste in sarcasm case
### Looks like this: 
> "yeah sure i'll get right on that" -> "YeAh sUrE I'Ll gEt rIgHt oN ThAt"

Great for sarcastic people who are tired of manually typing their sarcasm. With this script and the help of the [pyperclip](https://github.com/asweigart/pyperclip) module from Al Sweigart, you can copy any text and paste it sarcasticly.

## Dependancies:
- If you download this you will need the [pyperclip](https://pypi.org/project/pyperclip/) module to run it.

## Usage:
1. Run "main.py"
2. While script is running, any text you copy to your clipboard will be made sArCasTiC
3. You can enter certain commands to the script while its running to configure options for sarcasm formatting
4. Enter 'help' to see the list of available commands
5. To quit, type 'quit' or simply close the terminal window

**Note**: Formatting is applied to clipboard text _after copying_ , not after pasting. If you change formatting settings during the runtime, you won't see them applied until you've copied some new text.

## Commands:
- pause: formatting will not be applied to copied text after entering this command
- resume: resumes formatting copied text after pausing
- quit: exits application
- help: displays available commands
- pure-sarcasm {on, off}: **Enabled by default**, Makes it so all even indexed characters in a string are swapped case, and all odd indexed characters remain the same. Perfect, pure sarcasm. Ex: HeRe iS aN eXaMpLe (every other character is caps)
- set-sarcasm INT: When pure-sarcasm is disabled, pass an integer to this command. The closer to 100, the more capital letters you will see in the formatted text. The higher this number, the more angry your text will look.

**_Use sarcasm responsibly_** ༼ つ ◕_◕ ༽つ 🙄
