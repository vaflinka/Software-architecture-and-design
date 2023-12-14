from abc import ABC, abstractmethod

# Абстрактний клас або інтерфейс
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Клас, який реалізує абстрактний клас або інтерфейс
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Ще один клас, який реалізує абстрактний клас або інтерфейс
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Функція, яка використовує поліморфізм
def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area

# Використання функції для розрахунку площі для різних фігур
shapes = [Rectangle(2, 3), Circle(5)]
total_area = calculate_total_area(shapes)
print(f'Total Area: {total_area}')
