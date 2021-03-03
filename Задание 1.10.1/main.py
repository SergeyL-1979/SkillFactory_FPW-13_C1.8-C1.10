class Rectangle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def information_employee(self):
        return f'x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height}'


rect1 = Rectangle(5, 10, 50, 100)

print(str(rect1.information_employee()))
