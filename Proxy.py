from abc import ABC, abstractmethod

# Суб'єкт
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# Реальний суб'єкт
class RealSubject(Subject):
    def request(self):
        return "RealSubject: Handling request."

# Замісник
class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # Виконує додаткову логіку перед передачею запиту реальному об'єкту
        return f"Proxy: Checking access.\n{self._real_subject.request()}"

# Використання
real_subject = RealSubject()
proxy = Proxy(real_subject)

# Замісник контролює доступ до реального об'єкту
print(proxy.request())
