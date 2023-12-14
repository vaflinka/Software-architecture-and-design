class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

def make_bird_fly(bird):
    bird.fly()

# Використання принципу LSP
sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)  # Виведе: "Sparrow can fly"
make_bird_fly(penguin)  # Виведе: "Penguin can't fly"
