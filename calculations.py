#!/usr/bin/env python3

# A calculator that adds, divides, multiplies, and subtracts two numbers.

import time
import sys
from threading import Thread

def addition(x, y):
    """This function will add two numbers together."""

    return x + y


def subtraction(x, y):
    """This function will subtract two numbers."""

    return x - y


def division(x, y):
    """This function will divide two numbers."""

    return x / y


def multiplication(x, y):
    """This function will multiply two numbers."""

    return x * y


answer = None


def check():
    """Exiting the program if the user is inactive for 2 minutes."""
    time.sleep(120)
    if answer != None:
        return
    print('\nYou have not entered anything within 3 seconds, '
            ' goodbye.')
    sys.exit()


while True:
    print('This calcultor can only perform these 4 math functions '
            'with two numbers: '
            'Addition(1), Subtraction(2), Division(3), and Multiplication(4)')
    try:
        # Try and except block is to print an error if the user
        # tries to enter anything other than a number.
        Thread(target = check).start()
        operation_type = float(input('\nWhat operation would you '
            'like to perform? '
            '\nHint: Enter a number to a corresponding operation: '))
    except ValueError:
        print('That is not a valid response, please try again.')
        continue
    if operation_type == 1:
        print('You have selected Addition.')
        addition_input_1 = float(input('Enter your first number: '))
        addition_input_2 = float(input('Enter your second number: '))
        sum = addition(addition_input_1, addition_input_2)
        print('The sum of your two numbers is {}'.format(sum))
    elif operation_type == 2:
        print('You have selected Subtraction.')
        subtraction_input_1 = float(input('Enter your first number: '))
        subtraction_input_2 = float(input('Enter your second number: '))
        difference = subtraction(subtraction_input_1, subtraction_input_2)
        print('The difference of your two numbers is {}'.format(difference))
    elif operation_type == 3:
        print('You have selected Division.')
        division_input_1 = float(input('Enter your first number: '))
        division_input_2 = float(input('Enter your second number: '))
        quotient = division(division_input_1, division_input_2)
        print('The quotient of your two numbers is {}'.format(quotient))
    elif operation_type == 4:
        multiplication_input_1 = float(input('Enter your first number: '))
        multiplication_input_2 = float(input('Enter your second number: '))
        product = multiplication(multiplication_input_1, multiplication_input_2)
        print('The product of your two numbers is {}'.format(product))


