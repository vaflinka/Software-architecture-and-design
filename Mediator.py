from abc import ABC, abstractmethod

# Посередник
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

# Компонент
class Colleague(ABC):
    def __init__(self, mediator):
        self.mediator = mediator

    @abstractmethod
    def send(self, event):
        pass

    @abstractmethod
    def receive(self, event):
        pass

# Конкретний посередник
class ConcreteMediator(Mediator):
    def __init__(self, colleague1, colleague2):
        self.colleague1 = colleague1
        self.colleague2 = colleague2

    def notify(self, sender, event):
        if sender == self.colleague1:
            self.colleague2.receive(event)
        else:
            self.colleague1.receive(event)

# Конкретний компонент
class ConcreteColleague(Colleague):
    def send(self, event):
        print(f"Sending event: {event}")
        self.mediator.notify(self, event)

    def receive(self, event):
        print(f"Received event: {event}")

# Використання
mediator = ConcreteMediator(None, None)
colleague1 = ConcreteColleague(mediator)
colleague2 = ConcreteColleague(mediator)

mediator.colleague1 = colleague1
mediator.colleague2 = colleague2

colleague1.send("Hello from Colleague 1!")
colleague2.send("Greetings from Colleague 2!")
