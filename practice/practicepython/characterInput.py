# Ask the user to enter his name and age. Print out a message the year that they'll turn 100 years old.

    # name = str(input("What's your name? "))
    # age = int(input("How old are you? "))
    # currentYear = int(input('Tell me the current year: '))

    # Here, the code will calculate when the user will turn 100 years old.
    # turnAge = (100 - age) + currentYear

    # Print out a message
    # print("Hello, {} ! So, your age is {} and the year that you'll turn 100 ya will be in {} .".format(name, age, turnAge))
    # print("Congrats!")

# Another way to solve this problem

import datetime

name = str(input("What's your name? "))
age = int(input("How old are you? "))
num = int(input('Give me a number: '))

turnAge = str((100 - age) + datetime.datetime.today().year)

print(num * str("Hello, {} ! So, your age is {} and the year that you'll turn 100 ya will be in {} .\n").format(name, age, turnAge))