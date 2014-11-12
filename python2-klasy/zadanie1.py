class Produkt(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.aktualna_ilosc = 0
        self.aktualna_cena = 0
    def dodaj_ilosc(self, ilosc):
        self.aktualna_ilosc = self.aktualna_ilosc + ilosc
    def zmien_cene(self, nowa_cena):
        self.aktualna_cena = nowa_cena
    def sprzedaj_sztuke(self):
        self.aktualna_ilosc = self.aktualna_ilosc - 1
    def sprzedaj_sztuki(self,ilosc)
        self.aktualna_ilosc = self.aktualna_ilosc - ilosc
    def aktualna_ilosc(self):
        print('Aktualna ilosc to {}'.format(self.aktualna_ilosc))



