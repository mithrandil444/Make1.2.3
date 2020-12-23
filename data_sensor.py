#!/usr/bin/env python
"""
Info about our project comes here
bron: https://www.tutorialspoint.com/generating-random-number-list-in-python
"""

# IMPORTS
import random
import time

__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


def average(random_list):
    return sum(random_list) / len(random_list)



def data_sensor():
    random_list = []
    while True:
        for i in range(0, 20):
            time.sleep(0.5)
            numbahs = random.randint(1, 30)
            random_list.append(numbahs)
            print(random_list)
        print("the average is:  ", average(random_list))
        print("Press enter for a new list or 'd' to quit.")
        if input() == 'd':
            break

if __name__ == '__main__':  # code to execute if called from command-line
    data_sensor()
