# oop-python-learning

class Animal:
    def __init__(self, name, age, adopted=False):
        self.name = name
        self.age = age
        self.adopted = adopted

    def __repr__(self):
        status = "Adopted" if self.adopted else "Available"
        return f"{self.name} | Age: {self.age} | {status}"
    
    def adopt(self):
        if self.adopted:
            return f"{self.name} has already been adopted."
        elif not self.adopted:
            self.adopted = True
            return f"{self.name} has been adopted!"
    
    def make_sound(self):
        return "..."
    
    def info(self):
        return (f"{self.name} is {self.age} years old"
        f"and makes a sound like: {self.make_sound()}."
        f"Also, {self.name} is {'adopted' if self.adopted else 'available for adoption'}.")
    
        
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


    def __repr__(self):
        return f" Dog  | {super().__repr__()} | Breed: {self.breed}"
    
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor
    
    def __repr__(self):
        indoor_str = "Indoor" if self.indoor else "Outdoor"
        return f"🐱 Cat  | {super().__repr__()} | {indoor_str}"

    def make_sound(self):
        return "Meow!"
    
class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def __repr__(self):
        return f"🐦 Bird | {super().__repr__()} | Species: {self.species}"


    def make_sound(self):
        return "Tweet!"
    
class Shelter:
    def __init__(self, name):
        self.name = name 
        self.animals =  []

    def __repr__(self):
        return f"{self.name} Shelter | Animals: {len(self.animals)}"
    
    def add_animal(self, animal):
        self.animals =  self.animals.append(animal)

    def adopt(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal.adopt()
        return f"{name} not found in shelter."
    
    def show_all_animals(self):
        for animal in self.animals:
            print(animal)

    def available(self):
        available_animals = []
        for animal in self.animals:
            if not animal.adopted:
                available_animals.append(animal)
            elif animal.adopted:
                return "Animal is already adopted"
            
    def by_type(self, type):
        animal_by_type = []
        for animal in self.animals:
            if animal.__class__.__name__ == type:
                animal_by_type.append(animal)

        return animal_by_type

        