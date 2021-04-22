import random

class SarcasmFormatter:
    def __init__(self):
        self.variance = 50
        self.is_paused = False
    
    def passes(self):
        score = random.randrange(0, 100)
        if score < self.variance:
            return True

    def format(self, string: str):
        if self.is_paused:
            return string
            
        formatted = ""
        for c in string:
            if self.passes():
                formatted += c.swapcase()
        return formatted
