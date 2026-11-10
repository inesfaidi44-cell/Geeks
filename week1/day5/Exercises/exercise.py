#  Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Loulou Katty", 3)
cat2 = Cat("Sousou Katty", 5)
cat3 = Cat("Mimi Katty", 2)

def oldest_cat(cat1, cat2, cat3):
    oldest = max(cat1.age, cat2.age, cat3.age)
    if oldest == cat1.age:
        return cat1
    elif oldest == cat2.age:
        return cat2
    else:
        return cat3

oldest_cat_info = oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat_info.name} and is {oldest_cat_info.age} years old.")

# Exercise 2 : Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        jump_height = self.height * 2
        print(f"{self.name} jumps {jump_height} cm high!")


davids_dog = Dog("Rex", 50)
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()   
davids_dog.jump()   

sarahs_dog = Dog("Teacup", 20)
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}.")
else:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}.")

# Exercise 3 : Who’s the song producer?

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.groups = {}

        for animal in sorted(self.animals):
            first_letter = animal[0].upper()

            if first_letter not in self.groups:
                self.groups[first_letter] = []

            self.groups[first_letter].append(animal)

    def get_groups(self):
        for letter, animals in self.groups.items():
            print(letter, ":", animals)


# Create the zoo
new_york_zoo = Zoo("New York Zoo")

# Add animals
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")

# Display animals
print("Animals:")
new_york_zoo.get_animals()

# Sell an animal
new_york_zoo.sell_animal("Bear")

# Display animals after selling
print("\nAfter selling:")
new_york_zoo.get_animals()

# Display groups
print("\nGroups:")
new_york_zoo.get_groups()