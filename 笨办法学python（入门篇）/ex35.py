from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice or "2" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy dog! You are eaten by a masterful lord!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "Take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print(f"You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and turns into a lunatic.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I don't understand that.")

def cthulhu_home():
    print("The Cthulhu's home is full of great people.")
    print("Their names are: Cooper, Feed, Drink, and Eat.")
    print("How are you going to move the great people?")
    print("1. Fight or 2. Run or 3. Run away.")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("The great people are ate by a masterful lord!")
    else:
        cthulhu_home()

def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a land filled with a dead end crowd.")
    print("There are three doors, one to your right and one to your left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_home()
    else:
        dead("You fall into a pit of hatred and die!")

start()