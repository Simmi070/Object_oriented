class Pet:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

pet1 = Pet("Charlie", "pug", 7)
pet2 = Pet("Cookie", "poodle", 9)
pet3 = Pet("Snowball", "maltese", 5)

print("{} is a {} which is {} years old".format(pet1.name, pet1.breed, pet1.age))
print("{} is a {} which is {} years old".format(pet2.name, pet2.breed, pet2.age))
print("{} is a {} which is {} years old".format(pet3.name, pet3.breed, pet3.age))