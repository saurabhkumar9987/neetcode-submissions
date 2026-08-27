class SuperHero:
    """
    A class to represent a superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """
    
    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health
    

    # TODO: Define attack method and implement it
    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

    def heal(self,heal_points=10):
        self.health += heal_points 
        print(f"{self.name} heals {heal_points} points. New health: {self.health}.")


    # TODO: Define heal method and implment it
     

# TODO: Create superhero instance

catwoman = SuperHero("Catwoman","Agility",120)
catwoman.attack()
catwoman.heal()


# TODO: Use the attack() and heal() method
