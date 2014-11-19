'''Napisz funkcję zwracającą kolejne liczby ciągu Fibonacciego od 10 do 20.'''
'''http://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego'''
def wypisz_ciag():
    n1 = 0 #F1
    n2 = 1 #F2
    fib = 1 #F3
    while fib < 1000:
        fib = n1 + n2
        n1 = n2 #N-2
        n2 = fib #N-1
        if (fib > 10) and (fib < 20):
            print(fib)
