from abc import ABC, abstractmethod

# Абстрактний клас AbstractProductA
class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self) -> str:
        pass

# Абстрактний клас AbstractProductB
class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self) -> str:
        pass

# Конкретний клас ConcreteProductA1
class ConcreteProductA1(AbstractProductA):
    def operation_a(self) -> str:
        return "ConcreteProductA1 operation"

# Конкретний клас ConcreteProductB1
class ConcreteProductB1(AbstractProductB):
    def operation_b(self) -> str:
        return "ConcreteProductB1 operation"

# Конкретний клас ConcreteProductA2
class ConcreteProductA2(AbstractProductA):
    def operation_a(self) -> str:
        return "ConcreteProductA2 operation"

# Конкретний клас ConcreteProductB2
class ConcreteProductB2(AbstractProductB):
    def operation_b(self) -> str:
        return "ConcreteProductB2 operation"

# Абстрактний клас AbstractFactory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# Конкретний клас ConcreteFactory1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

# Конкретний клас ConcreteFactory2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

# Клієнтський код
def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_a.operation_a()}")
    print(f"{product_b.operation_b()}")


