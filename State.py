from abc import ABC, abstractmethod

# Контекст
class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

    def set_state(self, state):
        self._state = state

# Стан
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

# Конкретний стан
class ConcreteStateA(State):
    def handle(self):
        print("Handling request in State A.")

# Ще один конкретний стан
class ConcreteStateB(State):
    def handle(self):
        print("Handling request in State B.")

# Використання
context = Context(ConcreteStateA())
context.request()

# Зміна стану
context.set_state(ConcreteStateB())
context.request()
