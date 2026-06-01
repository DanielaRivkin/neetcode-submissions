class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> None:
        print("Animal makes a sound")

# TODO: Create a Dog class and a Cat class that inherit from the `Animal` class.
class Dog(Animal):
# TODO: Override the `make_sound` method in the `Dog` class to make the dog bark.
    def make_sound(self):
        print(f"{self.name} is barking")
# TODO: Override the `make_sound` method in the `Cat` class to make the cat meow.

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} is meowing")


# Do not modify the code below
animal = Animal("Cow")
animal.make_sound() # Output: Animal makes a sound
dog = Dog("Max")
dog.make_sound() # Output: Max is barking
cat = Cat("Luna")
cat.make_sound() # Output: Luna is meowing
