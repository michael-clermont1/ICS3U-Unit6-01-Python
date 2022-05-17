#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: May 2022
# This program finds the average of arrays

import random


def main():
    # this function finds the average of arrays

    counter = 0
    counter2 = 0
    numbers_average = 0
    random_numbers = []
    # process & output
    for counter in range(0, 10):
        random_number = random.randint(1, 100)
        random_numbers.append(random_number)
        print("The random number is: {0}.".format(random_number))
    for counter2 in range(len(random_numbers)):
        numbers_average = random_numbers[counter2] + numbers_average
    numbers_average = numbers_average / len(random_numbers)
    print("\nThe average is {0}.".format(numbers_average))
    print("\nDone.")


if __name__ == "__main__":
    main()
