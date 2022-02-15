# Add your code here:
def remove_substring(string, word):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(word)] == word:
            index += len(word)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)

def replace_substring(string, oldsubstring, newsubstring):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(oldsubstring)] == oldsubstring:
            output.append(newsubstring)
            index +=len(oldsubstring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)

# Here are some examples you can test it with:
print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
print(replace_substring("The word 'definately' is definately often misspelled.", 'definately', 'definitely'))

# Here are some strings you can test your function:
print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
print(remove_substring('I am NOT learning to code.', 'NOT '))
