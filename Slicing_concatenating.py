def word_triangle(word):
    # Add your code here
    length = len(word)

    for n in range(length):
        print(word[0:(length-n)])

word_triangle(input("Choose a word to slice."))

# Add your code for the adverbly function here
def adverbly(word):
    return word + 'ly'
# To test your code, un-comment this print statement
# and run the program from the terminal below:
print(adverbly("quick"))
