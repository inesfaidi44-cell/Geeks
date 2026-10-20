
import datetime

birthdate = input("Enter your birthdate (DD/MM/YYYY): ")
birthdate = datetime.datetime.strptime(birthdate, "%d/%m/%Y")


#print(birthdate)

current_date = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day


age = current_date - birthdate.year
#print(age)
if birthdate.month > current_month or (birthdate.month == current_month and birthdate.day > current_day):
    age = age -1

candles = age % 10 

print()
print(" " + "| " * candles)
print("  _______________")
print(" |  HAPPY BIRTHDAY |")
print(" |_________________|")