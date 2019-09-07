class Pets:

    dogs = []
    
    def __init__(self,dogs):
        self.dogs = dogs

class Dog:

    # class attritubte
    species = 'mammals'
    _count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Dog._count += 1

    def description(self):
        return "{} is {}".format(self.name,self.age)

class RusselTerrier(Dog):
    def run(self,speed):
        return "{} runs {}".format(self.name,speed)

class Bulldog(Dog):
    def run(self,speed):
        return "{} runs {}".format(self.name,speed)

# Create instance of Dogs/Instantiate
my_dogs = [
    RusselTerrier("Tom",6),
    Bulldog("Fletcher",7),
    Dog("Larry",9)
    ]

# Instantitate the Pets class
my_pets = Pets(my_dogs)

print("I have {} dogs.".format(Dog._count))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))


if all(dog.species == "mammals" for dog in my_pets.dogs):
    print("And they're all {}, of course.".format(dog.species))
