# encoding: utf-8
"""Additive inverse from list"""


def additive_inverse():
    """This module inverts numbers in list and prints original list along with inverted list

    how_many_to_inverse: stores how many numbers will be inverted
    numbers_to_inverse: list of numbers to inverse"""
    how_many_to_inverse = int(0)
    numbers_to_inverse = []
    while how_many_to_inverse <= 0:
        while True:
            try:
                how_many_to_inverse = int(input('How many to inverse : '))
                break
            except ValueError:
                pass
    for number_to_inverse in range(0, how_many_to_inverse):
        while True:
            try:
                numbers_to_inverse.append(int(input(str(number_to_inverse+1) + ' number to inverse : ')))
                break
            except ValueError:
                pass
    for number_in_numbers_to_inverse in range(0, how_many_to_inverse):
        print(numbers_to_inverse[number_in_numbers_to_inverse], - numbers_to_inverse[number_in_numbers_to_inverse])

if __name__ == "__main__":
    additive_inverse()