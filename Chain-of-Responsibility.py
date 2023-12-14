from abc import ABC, abstractmethod

# Обов'язок
class Handler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

    def set_successor(self, successor):
        self.successor = successor

# Конкретний обов'язок
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            return "ConcreteHandlerA: Handling request A."
        elif self.successor is not None:
            return self.successor.handle_request(request)
        else:
            return "ConcreteHandlerA: Unable to handle the request."

# Ще один конкретний обов'язок
class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            return "ConcreteHandlerB: Handling request B."
        elif self.successor is not None:
            return self.successor.handle_request(request)
        else:
            return "ConcreteHandlerB: Unable to handle the request."

# Використання
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()

handler_a.set_successor(handler_b)

# Клієнт створює запит та відправляє його на початок ланцюжка
request_a = handler_a.handle_request("A")
request_b = handler_a.handle_request("B")
request_c = handler_a.handle_request("C")

print(request_a)
print(request_b)
print(request_c)
