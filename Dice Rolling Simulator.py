import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        roll = input("Roll the dice? (yes or no): ").lower()
        if roll == "yes":
            result = roll_dice()
            print(f"You rolled a {result}!")
        elif roll == "no":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
