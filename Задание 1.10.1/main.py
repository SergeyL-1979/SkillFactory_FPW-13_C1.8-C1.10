class Rectangle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f'x = {self.x}, ' \
               f'y = {self.y}, ' \
               f'width = {self.width}, ' \
               f'height = {self.height}'

rect1 = Rectangle(5, 10, 50, 100)
print(rect1)
