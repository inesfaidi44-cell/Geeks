# Exercise 1 : Dunder Methods
class PrintList():

    def __init__(self, my_list):
        self.my_list = my_list

    def __repr__(self):
        return str(self.my_list)


print_list_instance = PrintList(["a", "b", "c"])
print(print_list_instance.__repr__())
# output:['a', 'b', 'c']

#Exercise 2 : Exceptions

my_list = [2, 3, 1, 2, "four", 42, 1, 5, 3, "imanumber"]
def sum_numbers(numbers):
    total = 0

    for number in numbers:
        try:
            total += number
        except TypeError:
            print(f"Invalid value: {number}")

    return total

print(sum_numbers(my_list))

# Exercise 3 : Writing Our Own Modules
# folder : Calculator_Project/

# Exercise 4 : Dogs Domesticated
