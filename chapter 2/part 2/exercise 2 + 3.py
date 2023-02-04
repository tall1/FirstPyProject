class Octopus:
    octCount = 0

    def __init__(self, age, name="Octavio"):
        self._name = name
        self._age = age
        Octopus.octCount += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


def main():
    oct1 = Octopus(10)
    oct2 = Octopus(5, "Octu")
    print(oct1.get_name() + " is now " + str(oct1.get_age()) + " years old.")
    print(oct2.get_name() + " is now " + str(oct2.get_age()) + " years old.")

    oct1.set_name("Octy")
    print(oct1.get_name())
    print("Number of octopuses: " + str(Octopus.octCount))

main()
