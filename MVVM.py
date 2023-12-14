from tkinter import Tk, Label, Button, StringVar

# Model
class CounterModel:
    def __init__(self):
        self._count = 0

    def get_count(self):
        return self._count

    def increment(self):
        self._count += 1

# ViewModel
class CounterViewModel:
    def __init__(self, model):
        self.model = model
        self.count_var = StringVar()
        self.update_count()

    def update_count(self):
        self.count_var.set(f"Count: {self.model.get_count()}")

    def increment(self):
        self.model.increment()
        self.update_count()

# View
class CounterView:
    def __init__(self, master, view_model):
        self.master = master
        self.view_model = view_model
        master.title("MVVM Example")

        self.label = Label(master, textvariable=view_model.count_var)
        self.label.pack()

        self.increment_button = Button(master, text="Increment", command=view_model.increment)
        self.increment_button.pack()

# Використання
model = CounterModel()
view_model = CounterViewModel(model)

root = Tk()
view = CounterView(root, view_model)

root.mainloop()
