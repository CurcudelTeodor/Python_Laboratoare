class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        pass  # Placeholder for making a sound, to be implemented by subclasses

    def move(self):
        pass  # Placeholder for movement behavior, to be implemented by subclasses

    def display_info(self):
        return f"Name: {self.name}, Habitat: {self.habitat}"


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} is giving birth to live young."

    def make_sound(self):
        return "Mammals make various sounds."

    def move(self):
        return f"{self.name} is walking or running."


class Bird(Animal):
    def __init__(self, name, habitat, wing_span):
        super().__init__(name, habitat)
        self.wing_span = wing_span

    def lay_eggs(self):
        return f"{self.name} is laying eggs in a nest."

    def make_sound(self):
        return "Birds produce songs, calls, or chirps."

    def move(self):
        return f"{self.name} is flying through the sky."


class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def lay_eggs(self):
        return f"{self.name} is laying eggs in the water."

    def make_sound(self):
        return "Fish generally do not produce sounds."

    def move(self):
        return f"{self.name} is swimming in the water."


def main():
    lion = Mammal("Lion", "Grasslands", "Yellow")
    sparrow = Bird("Sparrow", "Urban", "Small")
    salmon = Fish("Salmon", "Freshwater", "Silver")

    print(lion.display_info())
    print(lion.give_birth())
    print(lion.make_sound())
    print(lion.move())

    print(sparrow.display_info())
    print(sparrow.lay_eggs())
    print(sparrow.make_sound())
    print(sparrow.move())

    print(salmon.display_info())
    print(salmon.lay_eggs())
    print(salmon.make_sound())
    print(salmon.move())


if __name__ == "__main__":
    main()
    