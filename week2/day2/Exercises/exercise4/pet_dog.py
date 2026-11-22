from dog import Dog
import random

class PetDog(Dog):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.trained = False

    def train(self):
        self.bark()
        self.trained = True

    def play(self, *args):
        dog_names = [self.name]

        for dog in args:
            dog_names.append(dog.name)

        print(" and ".join(dog_names) + " all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]

            print(random.choice(tricks))

dog1 = PetDog("Rex", 3)
dog2 = PetDog("Max", 2)
dog3 = PetDog("Rocky", 4)

dog1.train()
dog1.play(dog2, dog3)
dog1.do_a_trick()
