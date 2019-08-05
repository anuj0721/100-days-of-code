class Dog:

    # class attribute
    species = "mammal"

    # instance attributes
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

#instantiation
bella = Dog("Bella",3,"brown")
toby = Dog("Toby",8,"black")
coco = Dog("Coco",5,"white")

def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old.".format(get_biggest_number(bella.age,toby.age,coco.age)))
