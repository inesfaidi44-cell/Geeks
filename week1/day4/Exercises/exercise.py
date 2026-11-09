# Exercise 1 : Convert lists into dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = dict(zip(keys, values))
print(my_dict)


#  Exercise 2 : Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_price = 0
for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name} has to pay: ${price}")
    total_price += price
print(f"Total price for the family is: ${total_price}")

#Exercise 3: Zara
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
 
brand["number_stores"] = 2
print(brand)

print("Zara's clients are:", brand["type_of_clothes"])

brand["country_creation"] = "Spain"
print(brand)

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand)

del brand["creation_date"]
print(brand)

print(brand['international_competitors'][-1])

print(brand['major_color']['US'])

print(len(brand))

print(brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print(brand)

print(brand['number_stores'])
print('The update() method replaced the old value of number_stores (2) with the new value (10000), because the key already existed in the dictionary')

# Exercise 4 : Some Geography

def describe_city(city,country='Japan'):
    print(f"{city} is in {country}")

describe_city('Tokyo')

#  Exercise 5 : Random
import random

def random_number():
    my_num = int(input("Enter a number between 1 and 100: "))
    random_num = random.randint(1, 100) 

    if my_num == random_num:
        print(f"Congratulations! You guessed the number {random_num} correctly!")
    else:
        print(f"Sorry! Better luck next time!")
        print(f"Your number: {my_num}")
        print(f"Random number: {random_num}")
random_number()

# Exercise 6 : Let’s create some personalized shirts
def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt('M', 'Hello World')

def make_shirt_second(size="L", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt_second()

make_shirt_second('M')

make_shirt("Small", "Never give up!")

make_shirt(size="Large", text="Python is amazing")

#  Exercise 7 : Temperature Advice
def get_season(month):
    if month == 12 or month == 1 or month == 2:
        return "winter"
    elif 3 <= month <= 5:
        return "spring"
    elif 6 <= month <= 8:
        return "summer"
    elif 9 <= month <= 11:
        return "autumn"
    else:
        return None
    
def get_random_temp(season):
    if season == "winter":
        return random.uniform(-10, 16)
    elif season == "spring":
        return random.uniform(5, 25)
    elif season == "summer":
        return random.uniform(20, 40)
    elif season == "autumn":
        return random.uniform(10, 25)

print(get_random_temp("summer"))

def main():
    month = int(input("Enter a month (1-12): "))
    season = get_season(month)
    if season is None:
        print("Invalid month. Please enter a number between 1 and 12.")
        return
    
    temp = get_random_temp(season)
    print(f"The temperature is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= temp <= 23:
        print("It's cool. A light jacket should be fine.")
    elif 24 <= temp < 32:
        print("It's warm. Dress comfortably.")
    else:
        print("It's hot! Stay hydrated and wear light clothing.")

main()

#Exercise 8 : Star Wars Quiz
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


def ask_questions():
    correct = 0
    incorrect = 0
    wrong_answers = []

    for item in data:
        user_answer = input(item["question"] + " ")

        if user_answer.lower() == item["answer"].lower():
            print("Correct!")
            correct += 1
        else:
            print("Incorrect!")
            incorrect += 1

            wrong_answers.append({
                "question": item["question"],
                "your_answer": user_answer,
                "correct_answer": item["answer"]
            })

    return correct, incorrect, wrong_answers


def display_results(correct, incorrect, wrong_answers):
    print("\n Quiz Results ")
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)

    if wrong_answers:
        print("\nQuestions answered incorrectly")

        for item in wrong_answers:
            print("\nQuestion:", item["question"])
            print("Your answer:", item["your_answer"])
            print("Correct answer:", item["correct_answer"])


display_results(*ask_questions())
