import copy

# Знімок
class Memento:
    def __init__(self, state):
        self.state = state

# Відправник
class Originator:
    def __init__(self, state):
        self.state = state

    def create_memento(self):
        return Memento(copy.deepcopy(self.state))

    def restore_from_memento(self, memento):
        self.state = memento.state

# Опікун
class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]

# Використання
originator = Originator("State1")
caretaker = Caretaker()

# Зберігаємо стан
memento1 = originator.create_memento()
caretaker.add_memento(memento1)

# Змінюємо стан
originator.state = "State2"

# Знову зберігаємо стан
memento2 = originator.create_memento()
caretaker.add_memento(memento2)

# Відновлення до попереднього стану
originator.restore_from_memento(caretaker.get_memento(0))

print(originator.state)  # Виведе: State1
