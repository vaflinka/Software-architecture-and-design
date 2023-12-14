from abc import ABC, abstractmethod

# Поганий приклад: великий загальний інтерфейс
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

# Кращий приклад: розділений на спеціалізовані інтерфейси
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

# Клас, який реалізує обидва інтерфейси
class Worker(Workable, Eatable):
    def work(self):
        print("Working")

    def eat(self):
        print("Eating")
