print("hello world")
from random import randint
from time import sleep

def get_user_guess(max_val):
    guess = int(input("Enter your guess: "))
    if guess > max_val:
        print("Guess is invalid! Try again.")
        return get_user_guess(max_val)
    return guess

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)

    max_val = number_of_sides * 2
    print("The maximum possible value is:", max_val)

    guess = get_user_guess(max_val)

    print("Rolling...")
    sleep(1)

    print("The 1st roll is:", first_roll)
    sleep(1)

    print("The 2nd roll is:", second_roll)
    sleep(1)

    total_roll = first_roll + second_roll
    print("Total value is:", total_roll)

    if guess == total_roll:
        print("You won!!")
    else:
        print("You lost, please try again.")

roll_dice(6)