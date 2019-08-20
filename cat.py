import random

class Dog:
    def speak(self):
        print("Woof!")

    def eat(self, food):
        if food == "food":
            print("Yummy food!")
        else:
            print("That's not food!")

class Cat:
    def speak(self):
        print(random.choice(["Meow!", "Purr!"]))
        print('test')