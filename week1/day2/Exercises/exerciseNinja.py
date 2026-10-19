# Exercise 1 : Outputs
#   3 <= 3 < 9    is TRUE 
#   3 == 3 == 3   is TRUE 
#   bool(0)   is FALSE
#   bool(5 == "5")  is FALSE
#   bool(4 == 4) == bool("4" == "4")  is TRUE
#   bool(bool(None))  is FALSE


#x = (1 == True)
#y = (1 == False)
#a = True + 4
#b = False + 10

#print("x is", x)    x is TRUE
#print("y is", y)    y is FALSE
#print("a:", a)      a is 5
#print("b:", b)      b is 10


# Exercise 2 : Longest word without a specific character

longest_length = 0
longest_sentence = ""

while True:
    sentence = input("Enter a sentence without A:")
    if sentence.lower() == "quit":
        break

    if "a" in sentence.lower():
        print("The sentence contains A. Try again!")
        continue

    if len(sentence) > longest_length:
        longest_sentence = sentence
        longest_length = len(sentence)
        print("Congratulations! New record!")

print("Longest sentence:", longest_sentence)
print("Length:", longest_length)


# Exercise 3: Working on a paragraph
paragraph = """Hidden behind a computer screen, the lonely person has control. They can search for company without the danger of being revealed or found wanting. They can reach out or they can hide; they can lurk and they can show themselves, safe from the humiliation of face-to-face rejection. The screen acts as a kind of protective membrane, a scrim that allows invisibility and transformation. You can filter your image, concealing unattractive elements, and you can emerge enhanced: an online avatar designed to attract likes. But now a problem arises, for the contact this produces is not the same thing as intimacy. Curating a perfected self might win followers or Facebook friends, but it will not necessarily cure loneliness, since the cure for loneliness is not being looked at, but being seen and accepted as a whole person—ugly, unhappy and awkward, as well as radiant and selfie-ready."""
print("Number of characters: ", len(paragraph))
print("Number of sentences:",paragraph.count("."))
word = paragraph.lower().split()
print("Number of words:",len(word))
print("Number of unique words:",len(set(word)))



# Bonus: How many non-whitespace characters it contains.
print("Number of non-whitespace characters:", len(''.join(paragraph.split())) )

# Bonus: The average amount of words per sentence in the paragraph.
print("Average words per sentence:", len(word) / paragraph.count("."))

#Bonus: the amount of non-unique words in the paragraph.
non_unique_words = len(word) - len(set(word))

print("Number of non-unique words:", non_unique_words)