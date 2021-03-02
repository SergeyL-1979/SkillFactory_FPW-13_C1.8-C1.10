class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width

    def information_employee(self):
        print(f'length = {self.length} ')
        print(f'width = {self.width} ')
        return f'AREA = {self.rectangle_area()}'


newRectangle = Rectangle(12, 10)

print(newRectangle.information_employee())

