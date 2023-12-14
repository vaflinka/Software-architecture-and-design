# Підсистема 1
class Engine:
    def start(self):
        return "Engine is started"

    def stop(self):
        return "Engine is stopped"

# Підсистема 2
class LightSystem:
    def turn_on(self):
        return "Lights are on"

    def turn_off(self):
        return "Lights are off"

# Підсистема 3
class MusicSystem:
    def play_music(self):
        return "Music is playing"

    def stop_music(self):
        return "Music is stopped"

# Фасад
class CarSystemFacade:
    def __init__(self):
        self.engine = Engine()
        self.lights = LightSystem()
        self.music = MusicSystem()

    def start_car(self):
        return f"{self.engine.start()}\n{self.lights.turn_on()}\n{self.music.play_music()}"

    def stop_car(self):
        return f"{self.engine.stop()}\n{self.lights.turn_off()}\n{self.music.stop_music()}"

# Використання
car_facade = CarSystemFacade()

# Запуск автомобіля
print("=== Starting the car ===")
print(car_facade.start_car())
print("========================")

# Зупинка автомобіля
print("\n=== Stopping the car ===")
print(car_facade.stop_car())
print("========================")
