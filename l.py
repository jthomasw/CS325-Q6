class Shape:
    def get_area(self):
        raise NotImplementedError("Subclasses must implement get_area method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

    def set_radius(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

#new Polygon!
class Polygon(Shape):
    def __init__(self, sides_length):
        self.sides_length = sides_length

    def get_area(self):
        
        return self.sides_length

def main():
    circle = Circle(5)
    rectangle = Rectangle(3, 6)
    triangle = Triangle(4, 3)
    polygon = Polygon(5)

    shapes = [circle, rectangle, triangle, polygon]

    for shape in shapes:
        print("Area of", type(shape).__name__, ":", shape.get_area())

if __name__ == "__main__":
    main()