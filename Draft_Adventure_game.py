import time


def print_pause(message):
    print(message)
    time.sleep(2)

print_pause("You're standing in an open field with green pastures and small \
green bushes.")
print_pause("Rumor has it that {{enemy}} is roaming these areas and harasing \
the population of the nearby cities.")
print_pause("In front of you there is a scary and dark cave.")
print_pause("To your left you see a water fountain.")
print_pause("Where would you like to go?")
choice = input("Please choose 1 to go to dark cave, 2 to go check water fountain:\n")
