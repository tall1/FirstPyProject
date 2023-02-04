class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger_level=0):
        self._name = name
        self._hunger_level = hunger_level

    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger_level > 0

    def feed(self):
        if self._hunger_level > 0:
            self._hunger_level -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, stink_count=6, hunger_level=0):
        super().__init__(name, hunger_level)
        self._stink_count = stink_count

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger_level=0, color="Green"):
        super().__init__(name, hunger_level)
        self._color = color

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    zoo_lst = [Dog("Brownie", 10), Cat("Zelda", 3), Skunk("Stinky"), Unicorn("Keith", 7), Dragon("Lizzy", 1450),
               Dog("Doggo", 80), Cat("Kitty", 80), Skunk("Stinky Jr.", 80), Unicorn("Clair", 80), Dragon("McFly", 80)]
    for animal in zoo_lst:
        print(animal.__class__.__name__ + " " + animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)


main()
