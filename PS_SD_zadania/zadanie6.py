"""Program returns fibonacci numbers in between 10 and 20"""


def fibonacci_sequence():

    """main loop"""

    fibonacci_1 = 0
    fibonacci_2 = 1
    fibonacci_list =[]
    while fibonacci_2 <= 20:
        fibonacci_sum = fibonacci_1 + fibonacci_2
        fibonacci_1 = fibonacci_2
        fibonacci_2 = fibonacci_sum
        if 10 <= fibonacci_sum <= 20:
            fibonacci_list.append(fibonacci_sum)
    print(fibonacci_list)


if __name__ == '__main__':
    fibonacci_sequence()
