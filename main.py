def start_game():
    print("Welcome to the Text Adventure Game!")
    print("You wake up in a dark forest with two paths in front of you.")
    print("1. Take the small path to the left")
    print("2. Take the wide road to the right")

    choice1 = input("Which path do you choose? Enter 1 or 2: ")

    if choice1 == "1":
        forest_path()
    elif choice1 == "2":
        highway_path()
    else:
        print("You wander off and get lost. Game over.")


def forest_path():
    print("\nYou follow the small path into the forest. You hear rustling in the bushes.")
    print("1. Go check it out")
    print("2. Walk away quickly")

    choice = input("Your choice? Enter 1 or 2: ")

    if choice == "1":
        print("\nA small fox jumps out and becomes your friend! You win! 🎉")
    else:
        print("\nYou get lost in the forest and are chased by wolves. Game over. 💀")


def highway_path():
    print("\nYou take the wide road. There's an old cabin ahead.")
    print("1. Knock on the door")
    print("2. Keep walking")

    choice = input("Your choice? Enter 1 or 2: ")

    if choice == "1":
        print("\nAn old lady gives you food and helps you escape the forest. You win! 🎉")
    else:
        print("\nYou walk for hours with no end in sight and collapse from exhaustion. Game over. 💀")


if __name__ == "__main__":
    start_game()