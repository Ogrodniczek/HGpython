__author__ = 'Kordian'

''' Napisz funkcję f(L) która będzie wyszukiwała liczby addytywne (przeciwne).
Funkcja ma przyjmować iterowalny zbiór liczb całkowitych jako parametr
a zwrócić iterowalalny zbiór dodatnich liczb addytywnych.
Liczba przeciwna to do danej liczby a, to taka liczba –a że zachodzi: a+(-a)=0'''

class Zadanie4(object):


    def __init__(self, ilosc):
        self.ilosc = ilosc
        self.liczby_dodatnie = []
        self.liczby_addytywne = []

    def dodaj_do_dodatnich(self):
        while self.ilosc > 0:
            self.liczby_dodatnie.append(int(input('Podaj liczbe dodatnia: ')))
            self.ilosc -= 1

    def zamien_na_addytywne(self):
        for liczba_dodatnia in self.liczby_dodatnie:
            liczba_dodatnia = - liczba_dodatnia
            self.liczby_addytywne.append(liczba_dodatnia)




ilosc = int(input('podaj ilosc liczb do dodania:'))
test = Zadanie4(ilosc)
test.dodaj_do_dodatnich()
test.zamien_na_addytywne()
print(test.liczby_dodatnie)
print(test.liczby_addytywne)