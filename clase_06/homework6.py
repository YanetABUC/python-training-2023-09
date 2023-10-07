class Animal:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
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

def interact_with_animal(animal:Animal):
    animal.make_sound()
    animal.move()

def zoo_simulation(list_animals):
    for animal in animals:
        interact_with_animal(animal)


animals = [Lion("King"), Snake("Sam"), Bird("Sally")]
zoo_simulation(animals)

