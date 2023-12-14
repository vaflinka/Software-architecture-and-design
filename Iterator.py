from abc import ABC, abstractmethod

# Агрегат
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

# Ітератор
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

# Конкретний агрегат
class ConcreteAggregate(Aggregate):
    def __init__(self):
        self._data = [1, 2, 3, 4, 5]

    def create_iterator(self):
        return ConcreteIterator(self)

    def get_item(self, index):
        return self._data[index]

    def size(self):
        return len(self._data)

# Конкретний ітератор
class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        self._aggregate = aggregate
        self._index = 0

    def has_next(self):
        return self._index < self._aggregate.size()

    def next(self):
        if self.has_next():
            item = self._aggregate.get_item(self._index)
            self._index += 1
            return item
        else:
            raise StopIteration("End of iteration")

# Використання
aggregate = ConcreteAggregate()
iterator = aggregate.create_iterator()

while iterator.has_next():
    item = iterator.next()
    print(item)
