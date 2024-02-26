class Shape:
    def get_area(self):
        raise NotImplementedError("Subclasses must implement get_area method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

def main():
    circle = Circle(5)
    square = Square(4)
    rectangle = Rectangle(3, 6)
    triangle = Triangle(4, 3)

    shapes = [circle, square, rectangle, triangle]

    for shape in shapes:
        print("Area of", type(shape).__name__, ":", shape.get_area())

if __name__ == "__main__":
    main()