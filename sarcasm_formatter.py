import random

class SarcasmFormatter:
    def __init__(self):
        self.variance = 50
        self.is_paused = False
        self.pure = True
    
    def passes(self):
        score = random.randrange(0, 100)
        if score < self.variance:
            return True
    
    def use_pure_sarcasm(self, pure):
        self.pure = pure
    
    def format_pure(self, string):
        formatted = ""
        for i in range(len(string)):
            c = string[i]
            if i % 2 == 0:
                formatted += c.swapcase()
            else:
                formatted += c
        return formatted

    def format(self, string: str):
        if self.is_paused:
            return string
            
        if self.pure:
            return self.format_pure(string)

        formatted = ""
        for c in string:
            if self.passes():
                formatted += c.swapcase()
            else:
                formatted += c
        return formatted
