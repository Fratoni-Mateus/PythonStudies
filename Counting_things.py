def count_characters(Word, letter):

    # Word = input("Write something to be counted: ")

    if Word == "":
        print("No word input, the word bonobos will be used.")
        Word = "bonobos"

    n = 0
    # letter = input("Choose a letter to be counted: ")

    if letter == "":
        print("No letter input received, the letter o will be counted.")
        letter = "o"

    for ch in Word:
        if ch == letter:
            n = n + 1

    # print ("There are", n, letter, "in the string", Word, ".")
    return "There are", n, letter, "in the string", Word, "."
    # return n

print("Should print a count of 3:")
print(count_characters("oxen and foxen all live in boxen", "x"))
#
print("Should print a count of 0:")
print(count_characters("that letter isn't here", "x"))
#
print("Should print a count of 9:")
print(count_characters("the goofy doom of the balloon goons", "o"))
#
print("Should print a count of 6:")
print(count_characters("papa pony and the parcel post problem", "p"))
#
print("Should print a count of 0:")
print(count_characters("this bunch of words has no", "e"))

word = "definitely"
length = len(word)

for n in range(length):
#     print(n)
    print(word[0:n+1])
    # Add your code here.
