from abc import ABC, abstractmethod

# Компонент
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Лист
class Leaf(Component):
    def operation(self):
        return "Leaf"

# Композит
class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Composite({', '.join(results)})"

# Використання
leaf1 = Leaf()
leaf2 = Leaf()
composite1 = Composite()
composite1.add(leaf1)
composite1.add(leaf2)

leaf3 = Leaf()
composite2 = Composite()
composite2.add(leaf3)

composite3 = Composite()
composite3.add(composite1)
composite3.add(composite2)

print(composite3.operation())
