#This function tests if the assigned string is
#longer than 140 characters.
#It returns "True" for > 140 len and "False" for everything else.

def too_long(s):
    return len(s) > 140
    # if len(s) > 140:
    #     return True
    # else:
    #     return False
    # return "Error in length counting function."

# Test a short string
print("This should be False:")
print(too_long("I'm a short string!"))

# Test a long string
print("This should be True:")
print(too_long("Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."))

for ch in "Hello!":
    print(ch)
    if ch == "!":
        print("I`m excited too!!!")
