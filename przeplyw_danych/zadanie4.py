__author__ = 'Kordian'

''' Napisz funkcję f(L) która będzie wyszukiwała liczby addytywne (przeciwne).
Funkcja ma przyjmować iterowalny zbiór liczb całkowitych jako parametr
a zwrócić iterowalalny zbiór dodatnich liczb addytywnych.
Liczba przeciwna to do danej liczby a, to taka liczba –a że zachodzi: a+(-a)=0'''

class Zadanie4(object):


    def __init__(self, liczba):
        self.liczba = liczba
        self.liczby_dodatnie = []
        self.liczby_addytywne = []

    def zamien_na_addytywne(self):
        self.liczby_dodatnie.append(self.liczba)
        for