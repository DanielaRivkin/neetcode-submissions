class SuperHero:
    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power
    
    def attack(self) -> None:
        print(f"{self.name} is attacking with {self.power}")

# TODO: Create a Avenger class that inherits from the SuperHero class
class Avenger(SuperHero):
# TODO: Override the __init__ method to add a team property to the Avenger class
    def __init__(self, name, power, team):
        super().__init__(name, power)
        self.team = team

# TODO: Call the attack method of the SuperHero class from the Avenger class
    def attack(self):
        super().attack()



# Don't change the code below
avenger = Avenger("Iron Man", "repulsor beams", "Avengers")
print(avenger.name)
print(avenger.power)
print(avenger.team)
avenger.attack()
