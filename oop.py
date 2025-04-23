from ast import Pass


class Pet:
    def __init__(self, name="Puppy", hunger=5, energy=5, happiness=5):
        """
        Initialize a new Pet instance.
        
        :param name: The name of the pet.
        :param hunger: Hunger level (0 = full, 10 = very hungry).
        :param energy: Energy level (0 = tired, 10 = fully rested).
        :param happiness: Happiness level (0–10).
        """
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []  # Initialize an empty list to store learned tricks

    def __str__(self):
        """
        Return a string representation of the pet's current state.
        """
        return (f"Pet Name: {self.name}\n"
                f"Hunger: {self.hunger}/10\n"
                f"Energy: {self.energy}/10\n"
                f"Happiness: {self.happiness}/10")

    def eat(self):
        """
        Reduces hunger by 3 points (but not below 0), and increases happiness by 1.
        """
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        """
        Increases energy by 5 points (but not above 10).
        """
        self.energy = min(10, self.energy + 5)

    def play(self):
        """
        Decreases energy by 2, increases happiness by 2, and increases hunger by 1.
        """
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        """
        Prints the current state of the pet.
        """
        print(self)

    def train(self, trick):
        """
        Teaches the pet a new trick and stores it in the tricks list.
        
        :param trick: The name of the trick to teach the pet.
        """
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        """
        Prints all the tricks the pet has learned.
        """
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")