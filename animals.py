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
        return f"Dog  | {super().__repr__()} | Breed: {self.breed}"
    
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor
    
    def __repr__(self):
        indoor_str = "Indoor" if self.indoor else "Outdoor"
        return f"Cat  | {super().__repr__()} | {indoor_str}"

    def make_sound(self):
        return "Meow!"
    
class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def __repr__(self):
        return f"Bird | {super().__repr__()} | Species: {self.species}"


    def make_sound(self):
        return "Tweet!"
    
class Shelter:
    def __init__(self, name):
        self.name = name 
        self.all_animals =  []

    def __repr__(self):
        return f"{self.name} Shelter | Animals: {len(self.all_animals)}"
    
    def add_animal(self, a_animal):
        self.all_animals.append(a_animal)

    def adopt(self, name):
        for a_animal in self.all_animals:
            if a_animal.name == name:
                return a_animal.adopt()
        return f"{name} not found in shelter."
    
    def show_all_animals(self):
        for a_animal in self.all_animals:
            print(a_animal)

    def available(self):
        available_animals = []
        for a_animal in self.all_animals:
            if not a_animal.adopted:
                available_animals.append(a_animal)
    
        return available_animals
            
    def by_type(self, type):
        animal_by_type = []
        for a_animal in self.all_animals:
            if a_animal.__class__.__name__ == type:
                animal_by_type.append(a_animal)

        return animal_by_type



shelter_made = Shelter("Jayan_Shelter")

shelter_made.add_animal(Cat("Toodles", 32, False))
shelter_made.add_animal(Cat("Niam", 67, True))


shelter_made.add_animal(Dog("Declan", 10, "Golden Doodle"))
shelter_made.add_animal(Dog("Bao", 10, "Golden Doodle"))

shelter_made.add_animal(Bird("Kishan", 4, "Peacock"))

shelter_made.show_all_animals()

shelter_made.adopt("Niam")

print("Availble animals")

for animal in shelter_made.by_type(("Dog")):
    print(animal)

shelter_made.adopt("Declan")

