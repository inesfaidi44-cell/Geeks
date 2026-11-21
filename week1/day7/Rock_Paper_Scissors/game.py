
import random


class Game:

    def get_user_item(self):
        choices = ["rock", "paper", "scissors"]

        while True:
            user_item = input("Choose rock, paper or scissors: ").strip().lower()

            if user_item in choices:
                return user_item
            else:
                print("Invalid choice! Try again.")

    def get_computer_item(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

    def get_game_result(self, user_item, computer_item):

        if user_item == computer_item:
            return "draw"

        elif (
            (user_item == "rock" and computer_item == "scissors") or
            (user_item == "paper" and computer_item == "rock") or
            (user_item == "scissors" and computer_item == "paper")
        ):
            return "win"

        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()

        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}.")
        print(f"The computer selected {computer_item}.")

        if result == "win":
            print("You win!")
        elif result == "loss":
            print("You lose!")
        else:
            print("It's a draw!")

        return result
