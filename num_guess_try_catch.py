#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Dec. 14, 2021
# This program generates a random
# number and uses a try catch statement
# to determine if a user has
# guessed correctly.

import random


# defines random number variable
random_number = random.randint(0, 9)


# this function uses a try catch statement
# to check if the user has entered the
# correct number
def main():
    # displays opening message
    print("Today you will try to guess the random number!\n")

    user_number_string = input("Enter an integer number: ")
    print("")

    try:
        user_number_int = int(user_number_string)
        if user_number_int == random_number:
            print("You are correct!")
            print("Thank you for playing!")
        elif user_number_int > 9:
            print("Please enter a valid number.")
        elif user_number_int < 0:
            print("Please enter a valid number.")
        else:
            print("Sorry, you are incorrect.")
            print("The correct answer is: {}" .format(random_number))

    except Exception:
        print("{} is not a number.". format(user_number_string))


if __name__ == "__main__":
    main()
