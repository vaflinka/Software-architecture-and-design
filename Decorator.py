# Компонент
class Coffee:
    def cost(self):
        return 5

# Декоратор
class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Конкретний декоратор
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

# Ще один конкретний декоратор
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

# Використання
simple_coffee = Coffee()
print(f"Cost of simple coffee: {simple_coffee.cost()}")

milk_coffee = MilkDecorator(simple_coffee)
print(f"Cost of coffee with milk: {milk_coffee.cost()}")

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"Cost of coffee with milk and sugar: {sugar_milk_coffee.cost()}")
