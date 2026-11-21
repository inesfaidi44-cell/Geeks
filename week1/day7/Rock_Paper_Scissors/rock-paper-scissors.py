
from game import Game


def get_user_menu_choice():
    print("\n===== MAIN MENU =====")
    print("p - Play a new game")
    print("s - Show scores")
    print("q - Quit")

    choice = input("Enter your choice: ").lower()

    if choice in ["p", "s", "q"]:
        return choice
    else:
        print("Invalid choice!")
        return None


def print_results(results):
    print("\n===== GAME SUMMARY =====")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thank you for playing!")


def main():

    results = {
        "win": 0,
        "loss": 0,
        "draw": 0
    }

    while True:

        choice = get_user_menu_choice()

        if choice == "p":
            game = Game()
            result = game.play()

            results[result] += 1

        elif choice == "s":
            print_results(results)

        elif choice == "q":
            print_results(results)
            break


if __name__ == "__main__":
    main()
