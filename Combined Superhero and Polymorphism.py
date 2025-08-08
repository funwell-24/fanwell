class Superhero:
    """Base class representing a superhero"""
    
    def __init__(self, name, secret_identity, powers, weakness):
        self.name = name
        self._secret_identity = secret_identity  # Encapsulated attribute
        self.powers = powers
        self.weakness = weakness
        self.energy_level = 100
        
    def use_power(self):
        """Generic power usage method to be overridden by subclasses"""
        print(f"{self.name} uses a generic power!")
        self.energy_level -= 10
        
    def reveal_identity(self):
        """Method demonstrating encapsulation"""
        print(f"My secret identity is {self._secret_identity}")
        
    def rest(self):
        """Recover energy"""
        self.energy_level = min(100, self.energy_level + 30)
        print(f"{self.name} rests. Energy level: {self.energy_level}%")
        
    def __str__(self):
        return f"{self.name} - Powers: {', '.join(self.powers)} | Weakness: {self.weakness}"


class FlyingHero(Superhero):
    """Subclass for flying superheroes"""
    
    def __init__(self, name, secret_identity, powers, weakness, max_altitude):
        super().__init__(name, secret_identity, powers, weakness)
        self.max_altitude = max_altitude  # in meters
        
    def use_power(self):
        """Override base method with flying-specific behavior"""
        print(f"{self.name} soars through the air at {self.max_altitude}m!")
        self.energy_level -= 15
        
    def aerial_attack(self):
        """Special move only flying heroes have"""
        print(f"{self.name} performs a devastating aerial attack!")
        self.energy_level -= 25


class TechHero(Superhero):
    """Subclass for tech-based superheroes"""
    
    def __init__(self, name, secret_identity, powers, weakness, gadget_count):
        super().__init__(name, secret_identity, powers, weakness)
        self.gadget_count = gadget_count
        
    def use_power(self):
        """Override base method with tech-specific behavior"""
        print(f"{self.name} deploys {self.gadget_count} high-tech gadgets!")
        self.energy_level -= 5
        
    def invent_gadget(self):
        """Special method only tech heroes have"""
        self.gadget_count += 1
        print(f"{self.name} invents a new gadget! Total gadgets: {self.gadget_count}")


class Animal:
    """Base class for animals"""
    
    def __init__(self, name):
        self.name = name
        
    def move(self):
        """Generic movement method to be overridden"""
        print(f"{self.name} moves in some way")
        

class Fish(Animal):
    """Fish subclass that swims"""
    
    def move(self):
        print(f"{self.name} is swimming ")
        

class Bird(Animal):
    """Bird subclass that flies"""
    
    def move(self):
        print(f"{self.name} is flying ")
        

class Snake(Animal):
    """Snake subclass that slithers"""
    
    def move(self):
        print(f"{self.name} is slithering ")
        

class Vehicle:
    """Base class for vehicles"""
    
    def __init__(self, model):
        self.model = model
        
    def move(self):
        """Generic movement method to be overridden"""
        print(f"{self.model} moves in some way")
        

class Car(Vehicle):
    """Car subclass that drives"""
    
    def move(self):
        print(f"{self.model} is driving ")
        

class Plane(Vehicle):
    """Plane subclass that flies"""
    
    def move(self):
        print(f"{self.model} is flying ")
        

class Boat(Vehicle):
    """Boat subclass that sails"""
    
    def move(self):
        print(f"{self.model} is sailing ")


def demonstrate_superheroes():
    print("\n" + "="*50)
    print("SUPERHERO DEMONSTRATION")
    print("="*50 + "\n")
    
    # Create instances
    superman = FlyingHero("Superman", "Clark Kent", 
                         ["Super strength", "Heat vision", "Flight"], 
                         "Kryptonite", 10000)
    
    iron_man = TechHero("Iron Man", "Tony Stark", 
                       ["Powered armor", "AI systems", "Weapons"], 
                       "Electromagnetic pulses", 42)
    
    # Demonstrate polymorphism
    heroes = [superman, iron_man]
    
    for hero in heroes:
        print("\n" + str(hero))
        hero.use_power()  # Same method, different behavior
        print(f"Energy after power use: {hero.energy_level}%")
        
        # Demonstrate unique subclass methods
        if isinstance(hero, FlyingHero):
            hero.aerial_attack()
        elif isinstance(hero, TechHero):
            hero.invent_gadget()
        
        hero.rest()


def demonstrate_polymorphism():
    print("\n" + "="*50)
    print("POLYMORPHISM DEMONSTRATION")
    print("="*50 + "\n")
    
    # Create a list of animals and vehicles
    creatures = [
        Fish("Nemo"),
        Bird("Eagle"),
        Snake("Viper"),
        Car("Tesla Model S"),
        Plane("Boeing 747"),
        Boat("Sailboat")
    ]
    
    # Demonstrate polymorphism - same method name, different behaviors
    for entity in creatures:
        entity.move()
        
    print("\nBonus: Just the vehicles:")
    # We can also filter by type
    vehicles = [x for x in creatures if isinstance(x, Vehicle)]
    for vehicle in vehicles:
        vehicle.move()


def main():
    print("COMBINED CLASS DESIGN AND POLYMORPHISM DEMONSTRATION")
    print("="*70 + "\n")
    
    # Run both demonstrations
    demonstrate_superheroes()
    demonstrate_polymorphism()
    
    print("\n" + "="*70)
    print("PROGRAM COMPLETE")


if __name__ == "__main__":
    main()