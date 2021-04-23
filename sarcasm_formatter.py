import random

class SarcasmFormatterConfiguration:
    def __init__(self, variance=50, pure=True):
        self.variance = variance
        self.pure = pure

    def set_variance(self, variance):
        self.variance = variance
    
    def set_pure(self, pure):
        self.pure = pure

class SarcasmFormatter:
    def __init__(self, config):
        self.config = config

    def passes(self):
        score = random.randrange(0, 100)
        if score < self.config.variance:
            return True
    
    def format_pure(self, string):
        formatted = ""
        for i in range(len(string)):
            c = string[i]
            if i % 2 == 0:
                formatted += c.swapcase()
            else:
                formatted += c
        return formatted

    def format_with_variance(self, string):
        formatted = ""
        for c in string:
            if self.passes():
                formatted += c.swapcase()
            else:
                formatted += c
        return formatted

    def format(self, string: str):
        if self.config.pure:
            return self.format_pure(string)
        return self.format_with_variance(string)