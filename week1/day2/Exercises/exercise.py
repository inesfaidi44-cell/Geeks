# Exercise 1 : Hello World
print("Hello World \n Hello World \n Hello World \n Hello World")

# Exercise 2 : Some Math
print(99**3 * 8)

# Exercise 3 : What’s your name ?
name = input(" What is your name? ")
if name.lower() == "ines":
    print("Ohh! We have the same name!")
else:
    print(f"Nice to meet you, {name}! You're cool, but I'm cooler! ")

# Exercise 4 : Tall enough to ride a roller coaster
height = int(input("Enter your height in centimeters:"))
if height > 145:
    print("You are tall enough to ride the roller coaster!")
else:
    print("You need to grow some more to ride the roller coaster.")

# Exercise 5 : Favorite Numbers
my_fav_numbers = {4 , 10 , 21 , 44 , 101 }

my_fav_numbers.add(7)
my_fav_numbers.add(99)

my_fav_numbers.remove(99)

friend_fav_numbers = {3 , 8 , 12 , 21 , 44 }

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#  Exercise 6: Tuple

# Answer : No, it's not possible to add integers directly to a tuple because tuples are immutable(unchangeable).

# Exercise 7: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#basket.remove("Banana")
#basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")

count = 0
for x in basket:
    if x == "Apples":
        count = count + 1
print(count)

# or
y = basket.count("Apples")
print(y)

basket.clear()

print(basket)

# Exercise 8 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches = []
while sandwich_orders:
    san = sandwich_orders.pop(0)
    finished_sandwiches.append(san)

print(sandwich_orders)
print(finished_sandwiches)

for sandw in finished_sandwiches:
    print(f"I made your {sandw}.")
