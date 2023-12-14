from abc import ABC, abstractmethod

# Спостерігач
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

# Конкретний спостерігач
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message: {message}")

# Суб'єкт
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

# Конкретний суб'єкт
class ConcreteSubject(Subject):
    def do_something(self):
        print("Subject is doing something.")
        self.notify_observers("Subject did something.")

# Використання
observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

subject = ConcreteSubject()
subject.add_observer(observer1)
subject.add_observer(observer2)

subject.do_something()
