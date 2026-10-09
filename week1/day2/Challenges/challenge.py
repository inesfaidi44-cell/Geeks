# Challenge 1

nombre = int(input("Enter a number: "))
length = int(input("Enter the length : "))

list = []
for i in range(1, length + 1):
    res = nombre * i
    list.append(res)
print(list)

# Challenge 2
word = input("Enter a word: ")
final_word = ""
for i in range(len(word) - 1):
    if word[i] != word[i + 1]:
        final_word += word[i ]
final_word += word[-1]  # Add the last character to the final_word          
print(final_word)