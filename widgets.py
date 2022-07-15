import random
import string


class Button:
    def __init__(self, width=80, height=40, x=0, y=0, text="Text", mode="clear", callback_function=None):
        self.signature = self.generate_random_signature()
        self.width = int(width)
        self.height = int(height)
        self.x = int(x)
        self.y = int(y)
        self.text = text
        self.is_down = False

        if callable(callback_function):
            self.callback_function = callback_function
        else:
            self.mode = mode

    def is_hover(self, x, y):
        return self.x < x < (self.x + self.width) and self.y < y < (self.y + self.height)

    def generate_random_signature(self):
        all_ = list(string.ascii_letters)
        char = ""
        for i in range(6):
            char += random.choice(all_)
        return char
