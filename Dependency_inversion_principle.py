from abc import ABC, abstractmethod

# Абстракція
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Низькорівневий модуль
class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: turned on")

    def turn_off(self):
        print("LightBulb: turned off")

# Високорівневий модуль
class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        if self.device.is_on():
            self.device.turn_off()
        else:
            self.device.turn_on()

# Високорівневий модуль
class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on")

    def turn_off(self):
        print("Fan: turned off")

# Високорівневий модуль
class SwitchWithTimer:
    def __init__(self, device):
        self.device = device

    def operate(self, minutes):
        self.device.turn_on()
        # Додатковий функціонал залежно від конкретного високорівневого модуля
        print(f"Device will turn off after {minutes} minutes.")

# Використання
bulb = LightBulb()
switch = Switch(bulb)
switch.operate()

fan = Fan()
switch_with_timer = SwitchWithTimer(fan)
switch_with_timer.operate(30)
