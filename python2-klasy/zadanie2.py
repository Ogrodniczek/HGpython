class Shop(object):
    def __init__(self, nazwa_sklepu):
        self.nazwa_sklepu = nazwa_sklepu
        self.nazwa_produktu = ''
        self.aktualna_ilosc = 0
        self.lista_produktow = []
    def dodaj_produkt(self, nazwa):
        self.nazwa_produktu = nazwa

    def dodaj_ilosc(self, produkt, ilosc):
        if produkt == self.nazwa_produktu:
            self.aktualna_ilosc = ilosc
            print('Do produktu {} dodano {} sztuk'.format(self.nazwa_produktu, str(self.aktualna_ilosc)))
        else:
            print('Nie ma podanego przez Ciebie produktu')
    def sprzedaj_produkt(self, produkt, ilosc):
        if (self.aktualna_ilosc >= ilosc) and (self.nazwa_produktu == produkt):
            self.aktualna_ilosc = self.aktualna_ilosc - ilosc
        elif self.aktualna_ilosc <= ilosc:
            print('Nie posiadamy takiej ilosci rzadanego produktu')
        else:
            print('Nie posiadamy podanego przez Ciebie produktu')

    def aktualna_ilosc_produktu(self, produkt):
        if self.nazwa_produktu == produkt:
            print('{} : {}'.format(self.nazwa_produktu, str(self.aktualna_ilosc)))
        else:
            print('Nie ma takiego produktu')

#przyklad
def przyklad():
    sklep1 = Shop('Warzywniak')
    sklep1.dodaj_produkt('marchewka')
    sklep1.dodaj_ilosc('marchewka', 5)
    sklep1.sprzedaj_produkt('marchewka', 4)
    sklep1.aktualna_ilosc_produktu('marchewka')



