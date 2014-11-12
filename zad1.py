class Produkt(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.aktualna_cena = 0
        self.aktualna_ilosc = 0
    def dodaj_ilosc(self, ilosc):
        self.aktualna_ilosc = self.aktualna_ilosc + ilosc
    def zmien_cene(self, nowa_cena):
        self.aktualna_cena = nowa_cena
    def sprzedaj_sztuke(self):
        self.aktualna_ilosc = self.aktualna_ilosc - 1
        if self.aktualna_ilosc < 0:
            print('ty gupi ciulu')
    def sprzedaj_sztuki(self, ilosc):
        self.aktualna_ilosc = self.aktualna_ilosc - ilosc
    def sprawdz_aktualna_ilosc(self):
        print('Aktualna ilosc to {}'.format(self.aktualna_ilosc))

#Przyklad uzycia
def przyklad():
    produkt1 = Produkt('zeszyt')
    produkt1.dodaj_ilosc(5)
    produkt1.zmien_cene('5.50')
    produkt1.sprzedaj_sztuke()
    produkt1.sprawdz_aktualna_ilosc()


