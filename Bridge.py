# Абстракція
class Shape:
    def __init__(self, implementation):
        self.implementation = implementation

    def draw(self):
        pass

# Реалізація абстракції
class Circle(Shape):
    def draw(self):
        return f"Drawing a Circle using {self.implementation.draw_implementation()}"

class Square(Shape):
    def draw(self):
        return f"Drawing a Square using {self.implementation.draw_implementation()}"

# Інтерфейс реалізації
class DrawingAPI:
    def draw_implementation(self):
        pass

# Конкретна реалізація
class DrawingAPI1(DrawingAPI):
    def draw_implementation(self):
        return "DrawingAPI1"

class DrawingAPI2(DrawingAPI):
    def draw_implementation(self):
        return "DrawingAPI2"

# Використання
implementation1 = DrawingAPI1()
implementation2 = DrawingAPI2()

circle1 = Circle(implementation1)
print(circle1.draw())  # Drawing a Circle using DrawingAPI1

circle2 = Circle(implementation2)
print(circle2.draw())  # Drawing a Circle using DrawingAPI2

square1 = Square(implementation1)
print(square1.draw())  # Drawing a Square using DrawingAPI1

square2 = Square(implementation2)
print(square2.draw())  # Drawing a Square using DrawingAPI2
