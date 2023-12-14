class Flyweight:
    def operation(self, shared_state):
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, shared_state):
        return f"ConcreteFlyweight: {shared_state}"

class FlyweightFactory:
    _flyweights = {}

    def get_flyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = ConcreteFlyweight()
        return self._flyweights[key]

# Використання
factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("shared_state_1")
flyweight2 = factory.get_flyweight("shared_state_2")

print(flyweight1.operation("external_state_1"))
print(flyweight2.operation("external_state_2"))
