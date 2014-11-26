class Zadanie7(object):


    def __init__(self):
        self.liczba = 0
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


##### TO POWYZEJ TE DEFY NARAZIE OLAC SAMA LOGIKA TEGO WHILE MNIE INTERESUJE #####

test = Zadanie7()
wartosc = int(input('Podaj wartosc:'))

while wartosc != 0:
    wartosc = input('Podaj wartosc a zeby wyjsc wpisz 0:')
