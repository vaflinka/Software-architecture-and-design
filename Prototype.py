from copy import deepcopy

# Клас, який визначає інтерфейс клонування
class Prototype:
    def clone(self):
        pass

# Конкретний клас, який реалізує клонування
class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        return deepcopy(self)

# Клієнтський код, який використовує прототипи
prototype_instance = ConcretePrototype(5)
clone1 = prototype_instance.clone()
clone2 = prototype_instance.clone()

print(clone1.value)  # Виведе: 5
print(clone2.value)  # Виведе: 5
