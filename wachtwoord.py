#!/usr/bin/env python
"""
Info about our project comes here
"""

# IMPORTS
import random, string


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# list


def generatePasssword(num):
    password = ''

    for i in range(num):
        x = random.randint(0,9)

        password += string.printable[x]
    return password

print(generatePasssword(9))



if __name__ == '__generatePassword__':  # code to execute if called from command-line
    generatePasssword()
