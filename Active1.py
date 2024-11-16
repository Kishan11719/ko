class Polygon:
    def __init__(self, *sides):
        self.sides = sides

    def area(self):
        raise NotImplementedError("This method should be implemented by subclasses")

class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(base, height)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(length, width)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Polygon):
    def __init__(self, side):
        super().__init__(side)
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Polygon):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

# Example usage
if __name__ == "__main__":
    triangle = Triangle(10, 5)
    print(f"Triangle Area: {triangle.area()}")

    rectangle = Rectangle(10, 5)
    print(f"Rectangle Area: {rectangle.area()}")

    square = Square(4)
    print(f"Square Area: {square.area()}")

    circle = Circle(7)
    print(f"Circle Area: {circle.area():.2f}")
