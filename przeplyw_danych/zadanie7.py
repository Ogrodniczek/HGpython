class Zadanie7(object):


    def __init__(self):
        self.liczba = 0
        self.liczby_dodatnie = []
        self.liczby_addytywne = []

    def dodaj_do_dodatnich(self, liczba):
            self.liczby_dodatnie.append(liczba)

    def zamien_na_addytywne(self):
        for liczba_dodatnia in self.liczby_dodatnie:
            liczba_dodatnia = - liczba_dodatnia
            self.liczby_addytywne.append(liczba_dodatnia)


##### TO POWYZEJ TE DEFY NARAZIE OLAC SAMA LOGIKA TEGO WHILE MNIE INTERESUJE #####

test = Zadanie7()
wartosc = int(input('Podaj wartosc:'))

while wartosc != 0:
    test.dodaj_do_dodatnich(wartosc)
    test.zamien_na_addytywne()
    wartosc = int(input('Podaj wartosc a zeby wyjsc wpisz 0:'))

print(test.liczby_dodatnie)
print(test.liczby_addytywne)
