from abc import ABC, abstractmethod

# Елемент
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

# Конкретний елемент
class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

# Ще один конкретний елемент
class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

# Відвідувач
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element_a):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element_b):
        pass

# Конкретний відвідувач
class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element_a):
        print(f"Visited ConcreteElementA by ConcreteVisitor: {element_a}")

    def visit_concrete_element_b(self, element_b):
        print(f"Visited ConcreteElementB by ConcreteVisitor: {element_b}")

# Об'єкт структури
class ObjectStructure:
    def __init__(self):
        self.elements = []

    def attach(self, element):
        self.elements.append(element)

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)

# Використання
object_structure = ObjectStructure()
object_structure.attach(ConcreteElementA())
object_structure.attach(ConcreteElementB())

visitor = ConcreteVisitor()
object_structure.accept(visitor)
