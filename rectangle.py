class Rectangle:
    
    # constructor, with default initialization
    def __init__(self, base: float = 1, height: float = 1):
        self.base = base
        self.height = height
    
    def __str__(self):
        # usage: `str(self)` or `print(self)`, where `self` must be a `Rectangle` object
        return f"Rectangle object with base {self.base} and height {self.height}"

    def area(self):
        return self.base*self.height