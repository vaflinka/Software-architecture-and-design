# Цільовий інтерфейс
class Target:
    def request(self):
        return "Target: The default target's behavior."

# Адаптований клас (Adaptee)
class Adaptee:
    def specific_request(self):
        return "Adaptee: The specific behavior."

# Адаптер
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (Translated) {self.adaptee.specific_request()}"

# Використання
adaptee = Adaptee()
adapter = Adapter(adaptee)

print("Adaptee interface is incompatible with the Target.")
print(f"Adaptee: {adaptee.specific_request()}")

print("But with the Adapter, it becomes compatible with the Target.")
print(f"Adapter: {adapter.request()}")
