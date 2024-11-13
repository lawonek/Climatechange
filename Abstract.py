# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Triangle subclass
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Example usage
rectangle = Rectangle(5, 10)
circle = Circle(7)
triangle = Triangle(4, 8)

print("Rectangle area:", rectangle.area())
print("Circle area:", circle.area())
print("Triangle area:", triangle.area())
