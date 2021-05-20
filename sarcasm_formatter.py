import random

def maybe(rarity):
    return random.randrange(0, 100) < rarity

class SarcasmFormatterConfiguration:
    def __init__(self, variance=50, pure=True):
        self.variance = variance
        self.pure = pure

    def get_status(self):
        pure_sarcasm = "Pure Sarcasim is {pure}".format(
            pure="ON" if self.pure else "OFF")
        variance = "Current variance is {variance}".format(
            variance=self.variance)
        return pure_sarcasm, variance

    def set_variance(self, variance):
        self.variance = variance
    
    def set_pure(self, pure):
        self.pure = pure

class SarcasmFormatter:
    def __init__(self, config):
        self.config = config

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
            if maybe(self.config.variance):
                formatted += c.swapcase()
            else:
                formatted += c
        return formatted

    def format(self, string):
        if self.config.pure:
            return self.format_pure(string)
        return self.format_with_variance(string)