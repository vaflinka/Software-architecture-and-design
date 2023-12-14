from abc import ABC, abstractmethod

# Абстрактний клас Product
class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

# Конкретний клас Product
class ConcreteProductA(Product):
    def operation(self) -> str:
        return "ConcreteProductA operation"

# Конкретний клас Product
class ConcreteProductB(Product):
    def operation(self) -> str:
        return "ConcreteProductB operation"

# Абстрактний клас Creator (Творець)
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result

# Конкретний клас Creator (Творець)
class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

# Конкретний клас Creator (Творець)
class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Використання паттерну
def client_code(creator: Creator) -> None:
    print(f"Client: {creator.some_operation()}")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreatorA.")
    client_code(ConcreteCreatorA())

    print("\nApp: Launched with the ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
