"""Program zwraca liczby fibonacciego z przedzialu od 10 do 20"""


def ciag_fibonacciego():

    """petla"""

    fib1 = 0
    fib2 = 1
    fib = 0
    tfib = []
    while fib <= 20:
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        if 10 <= fib <= 20:
            tfib.append(fib)
    print(tfib)


if __name__ == '__main__':
    ciag_fibonacciego()
