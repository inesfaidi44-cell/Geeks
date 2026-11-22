# Exercise 1 : Pets

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Create another breed
class Siamese(Cat):
    pass

all_cats = [
    Bengal("Mimi", 3),
    Chartreux("Lulu", 4),
    Siamese("Susu", 2)
]

sara_pets = Pets(all_cats)

sara_pets.walk()


# Exercise 2: Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):

        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} wins the fight!"

        elif my_power < other_power:
            return f"{other_dog.name} wins the fight!"

        else:
            return "It's a draw!"

dog1 = Dog("Rex", 5, 30)
dog2 = Dog("Max", 3, 20)
dog3 = Dog("Rocky", 4, 35)

print(dog1.bark())

print(dog1.run_speed())

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))

# Exercise 3 : Family
class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family!")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member["age"] > 18

        return False  

    def family_presentation(self):
        print(f"Family name: {self.last_name}")

        for member in self.members:
            for key, value in member.items():
                print(f"{key}: {value}")
            print("----------------")

members = [
    {"name": "Michael", "age": 35, "gender": "Male", "is_child": False},
    {"name": "Sarah", "age": 32, "gender": "Female", "is_child": False}
]

family = Family(members, "Smith")

family.family_presentation()

print("Is Michael over 18?", family.is_18("Michael"))
print("Is Sarah over 18?", family.is_18("Sarah"))

family.born(
    name="Jack",
    age=5,
    gender="Male",
    is_child=True
)

family.family_presentation()

#Exercise 4 : TheIncredibles Family
class TheIncredibles(Family):

    def use_power(self, name):
        for member in self.members:
            if member["name"] == name:

                if member["age"] > 18:
                    print(f"{name}'s power: {member['power']}")
                else:
                    print(f"{name} is not old enough to use their power.")

                return

        print("Member not found!")

    def incredible_presentation(self):
        print("Here is our powerful family!")

        super().family_presentation()


incredible_members = [
    {
        "name": "Michael",
        "age": 35,
        "gender": "Male",
        "is_child": False,
        "power": "fly",
        "incredible_name": "MikeFly"
    },
    {
        "name": "Sarah",
        "age": 32,
        "gender": "Female",
        "is_child": False,
        "power": "read minds",
        "incredible_name": "SuperWoman"
    }
]

incredibles = TheIncredibles(incredible_members, "Incredibles")

incredibles.incredible_presentation()

incredibles.use_power("Michael")
incredibles.use_power("Sarah")

incredibles.born(
    name="Jack",
    age=0,
    gender="Male",
    is_child=True,
    power="Unknown Power",
    incredible_name="Baby Jack"
)

incredibles.incredible_presentation()

incredibles.use_power("Jack")