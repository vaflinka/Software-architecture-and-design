from abc import ABC, abstractmethod

# Абстрактний клас
class AbstractClass(ABC):
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass

# Конкретний клас
class ConcreteClass(AbstractClass):
    def step_one(self):
        print("Step one from ConcreteClass")

    def step_two(self):
        print("Step two from ConcreteClass")

    def step_three(self):
        print("Step three from ConcreteClass")

# Використання
concrete_object = ConcreteClass()
concrete_object.template_method()
