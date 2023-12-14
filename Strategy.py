from abc import ABC, abstractmethod

# Контекст
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        return self._strategy.execute()

# Стратегія
class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретна стратегія
class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Executing strategy A."

# Ще одна конкретна стратегія
class ConcreteStrategyB(Strategy):
    def execute(self):
        return "Executing strategy B."

# Використання
context = Context(ConcreteStrategyA())
result = context.execute_strategy()
print(result)

# Зміна стратегії
context.set_strategy(ConcreteStrategyB())
result = context.execute_strategy()
print(result)
