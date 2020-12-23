#!/usr/bin/env python
"""
Met dit rekenmachine kan je optellen,aftrekken,vermenigvuldigen en delen door 2 getallen te kiezen
"""


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Finished"


# This function add 2 numbers
def add(x, y):
    try:
        return(x + y)
    except Exception as s:
        print(s)


# This function substract 2 numbers
def subtract(x, y):
    try:
        return(x - y)
    except Exception as s:
        print(s)


# This function multiplies 2 numbers
def multiplies(x, y):
    try:
        return(x * y)
    except Exception as s:
        print(s)



# This function divides 2 numbers
def divide(x, y):
    try:
        return(x / y)
    except Exception as s:
        print(s)





def main():
    print("Select operation.")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    try:

        choice = input("Enter choice(1/2/3/4):\n")   # Asks input from the user

        # Makes sure that you've entered a number from 1 to 4

        num1 = float(input("Kies en typ het eerste getal: "))
        num2 = float(input("Kies en typ het 2de getal: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))   # Adds 2 numbers and print it

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))   # Subtracts 2 numbers and print it

        elif choice == '3':
            print(num1, "*", num2, "=", multiplies(num1, num2))   # Multiplies 2 numbers and print it

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))  # Divides 2 numbers and print it

        else:
            raise Exception("ERROR geef een getal in")  # Displays an error


    except Exception as s:
        print(s)
        main()
if __name__ == '__main__':  # code to execute if called from command-line
    main()