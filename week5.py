
#PART 1
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # private attribute (encapsulation)

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")

    def battery_status(self):
        print(f"🔋 Battery: {self.__battery}%")

    def use_battery(self, amount):
        self.__battery = max(0, self.__battery - amount)


# Child class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, gpu):
        super().__init__(brand, model, battery)
        self.gpu = gpu

    def play_game(self, game):
        print(f"🎮 Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!")
        self.use_battery(20)


# --- Demo ---
phone1 = Smartphone("Samsung", "Galaxy S23", 85)
phone1.make_call("123-456-789")
phone1.battery_status()

gaming_phone = GamingPhone("Asus", "ROG Phone 7", 100, "Adreno 740")
gaming_phone.play_game("PUBG Mobile")
gaming_phone.battery_status()


#PART2

class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


class Dog(Animal):
    def move(self):
        print("🐕 Running on four legs!")


class Bird(Animal):
    def move(self):
        print("🐦 Flying in the sky!")


class Fish(Animal):
    def move(self):
        print("🐟 Swimming in the water!")


# --- Demo ---
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()   
    
    
    
    
