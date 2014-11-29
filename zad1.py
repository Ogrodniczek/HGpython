class Produkt(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.aktualna_cena = 0
        self.aktualna_ilosc = 0
    def dodaj_ilosc(self, ilosc):
        selft.aktualna_ilosc = self.aktualna_ilosc + ilosc
    def zmien_cene(self, nowa_cena):
        selft.aktualna_cena = nowa_cena
    def sprzedaj_sztuke(self):
        self.aktualna_ilosc = self.aktualna_ilosc -1
    def sprzedaj_sztuki(self):
        self.aktualna_ilosc = self.aktualna_ilosc - ilosc
    def sprawdz_aktualna_ilosc(self):
        print('Aktualna ilosc to {}'.firnat(str(self.aktualna_ilosc))





