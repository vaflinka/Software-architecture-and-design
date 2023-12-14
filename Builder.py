from abc import ABC, abstractmethod

# Клас продукту
class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None

    def __str__(self):
        return f"Computer: {self.cpu}, {self.memory}, {self.storage}"

# Інтерфейс будівельника
class Builder(ABC):
    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_memory(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    @abstractmethod
    def get_computer(self) -> Computer:
        pass

# Конкретний будівельник
class ConcreteBuilder(Builder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.cpu = "Intel Core i7"

    def build_memory(self):
        self.computer.memory = "16GB DDR4"

    def build_storage(self):
        self.computer.storage = "512GB SSD"

    def get_computer(self) -> Computer:
        return self.computer

# Директор, який використовує будівельника для створення об'єкта
class Director:
    def construct(self, builder: Builder):
        builder.build_cpu()
        builder.build_memory()
        builder.build_storage()

# Використання
builder = ConcreteBuilder()
director = Director()

# Створення об'єкта за допомогою директора та будівельника
director.construct(builder)
computer = builder.get_computer()

print(computer)
