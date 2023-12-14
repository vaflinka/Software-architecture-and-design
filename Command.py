from abc import ABC, abstractmethod

# Команда
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Конкретна команда
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_on()

# Отримувач
class Light:
    def turn_on(self):
        return "Light is ON"

# Викликач
class RemoteControl:
    def set_command(self, command):
        self.command = command

    def press_button(self):
        return self.command.execute()

# Клієнт
light = Light()
light_on = LightOnCommand(light)

remote = RemoteControl()
remote.set_command(light_on)

# Викликач виконує команду, і світло вмикається
result = remote.press_button()
print(result)
