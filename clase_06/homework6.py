class Animal:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def set_name(self, name):
        self.__name = name

    def make_sound(self):
        pass

    def move(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print(f"Lion {self.name} roars")
    
    def move(self):
        print(f"Lion {self.name} is running")

class Snake(Animal):
    def make_sound(self):
        print(f"Snake {self.name} hiss")
    
    def move(self):
        print(f"Snake {self.name} is slithering")

class Bird(Animal):
    def make_sound(self):
        print(f"Bird {self.name} sings")
    
    def move(self):
        print(f"Bird {self.name} is flying")

class Visitor:
    def interact_with_animal(self, animal:Animal):
        animal.make_sound()
        animal.move()

    def zoo_simulation(self, list_animals):
        for animal in list_animals:
            self.interact_with_animal(animal)


animals = [Lion("King"), Snake("Sam"), Bird("Sally")]
juan = Visitor()
juan.zoo_simulation(animals)

