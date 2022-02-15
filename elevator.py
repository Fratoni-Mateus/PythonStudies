import time  # Imports the time module to use on print_pause()


def print_pause(text):  # Prints a message and then waits before going on
    print(text)
    time.sleep(2)


def which_floor():  # Validates the input of the user and returns
    # when a valid input is received
    while True:
        print_pause("Please enter the number for the floor \
        you would like to visit:")
        print("1. Lobby \n2. Human resources \n\
        3. Engineering department.")
        answer = input()
        if answer == "1":
            return 1
        elif answer == "2":
            return 2
        elif answer == "3":
            return 3


def first_floor(items):  # Defines the first floor activities.
    print_pause("You push the button for the first floor.")
    print_pause("After a few moments, you find yourself in the lobby.")
    if "ID card" in items:
        print_pause("The clerk greets you, but they have \
        already given you your ID card, so there is nothing \
        more to do here now.")
    else:
        print_pause("The clerk greets you and gives \
        you your ID card.")
        items.append("ID card")
    print_pause("Where would you like to go next?")
    elevator(items)


def second_floor(items):  # Defines the second floor activities.
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself in the \
    human resources department.")
    if "Handbook" in items:
        print_pause("The HR folks are busy at their desks.")
        print_pause("There doesn't seem to be much to do here.")
    else:
        print_pause("The head of HR greets you.")
        if "ID card" in items:
            print_pause("They look at your ID card and then give you a copy \
            of the employee handbook.")
            items.append("Handbook")
        else:
            print_pause("They have something for you, but say they can't \
            give it to you until you go get your ID card.")
    print_pause("Where would you like to go next?")
    elevator(items)


def third_floor(items):  # Defines the third floor activities.
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself in the \
    engineering department.")
    if "ID card" in items:
        print_pause("You use your ID card to open the door.")
        print_pause("Your program manager greets you and tells you that you \
        need to have a copy of the employee handbook in order to start work.")
        if "Handbook" in items:
            print_pause("Fortunately, you got that from HR!")
            print_pause("Congratulatons! You are ready to start your new job \
            as vice president of engineering!")
            exit()
        else:
            print_pause("They scowl when they see that you don't have it, \
            and send you back to the elevator.")
    else:
        print_pause("Unfortunately, the door is locked and you can't get in.")
        print_pause("It looks like you need some kind of key card to \
        open the door.")
        print_pause("You head back to the elevator.")
    print_pause("Where would you like to go next?")
    elevator(items)


def introduction():  # Initial codes that run once during startup.
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")


def elevator(items):  # Elevator mechanics
    floor = which_floor()
    if floor == 1:
        first_floor(items)
    elif floor == 2:
        second_floor(items)
    elif floor == 3:
        third_floor(items)


def play_game():  # Structures the code.
    items = []
    introduction()
    elevator(items)


if __name__ == '__main__':  # Execute if the module is initialized directly
    play_game()
