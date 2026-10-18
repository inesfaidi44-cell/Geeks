# Exercise 1: What is the Season?

month = int(input("Enter the month (1-12): "))
if month < 1 or month > 12:
    print("Invalid month!")
elif month >= 3 and month <= 5:
    print("It's Spring!")
elif month >= 6 and month <= 8:
    print("It's Summer!")
elif month >= 9 and month <= 11:
    print("It's Autumn!")
else:
    print("It's Winter!")


# Exercise 2: For Loop
#1
for i in range(1, 21):
    print(i)
#2
for i in range(1, 21):
    if i % 2 ==0:
        print(i)


#Exercise 3: While Loop
#1
name = input('Enter your name :').lower()
while name != 'ines':
    name = input('Enter your name :').lower()

#2
name=''
while name != 'ines':
    name = input('Enter your name :').lower()


#Exercise 4: Check the index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input('Enter your name : ')

if name in names:
    print(f"{name} is in the list at index {names.index(name)}")
else:
    print(f"{name} is not in the list")

#Exercise 5: Greatest Number

num1 = int(input("Input the 1st number : "))
num2 = int(input("Input the 2nd number : "))
num3 = int(input("Input the 3rd number : "))

if num1 >= num2 and num1 >= num3:
    print(f"The greatest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The greatest number is: {num2}")
else:
    print(f"The greatest number is: {num3}")

# Exercise 6: Random number
import random
numero = int(input("Enter a number between 1 and 9 : ")) 
random_num = random.randint(1,9)

#first 
if numero == random_num:
    print("Winner")
else:
    print("Better luck next time.")
print("The random number was:", random_num)

#bonus + bonus2

wins = 0 
losses = 0

while True:
    numero = int(input("Enter a number between 1 and 9 : ")) 
    random_num = random.randint(1,9)

    if numero == random_num:
        print("winner!")
        wins += 1
    else:
        print("Better luck next time")
        print("The random number was:", random_num) 
        losses += 1

    play_again = input('Do you want to play again? (yes/no): ')

    if play_again.lower() != 'yes':
        break

print(wins)
print(losses)
