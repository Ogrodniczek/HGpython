class Produkt(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.aktualna_cena = 0
        self.aktualna_ilosc = 0
    def dodaj_ilosc(self, ilosc):
        if ilosc == type(int):
            if ilosc > 0:
                self.aktualna_ilosc = self.aktualna_ilosc + ilosc
            else:
                print('Podaj liczbe calkowita wieksza od 0')
        else: 
            print('Podaj liczbe calkowita')
    def zmien_cene(self, nowa_cena):
        self.aktualna_cena = nowa_cena
    def sprzedaj_szuke(self):
        self.aktualna_ilosc = self.aktualna_ilosc - 1
    def sprzedaj_sztuki(self, ilosc):
        self.aktualna_ilosc = self.aktualna_ilosc - ilosc
    def sprawdz_aktualna_ilosc(self):
        print('Aktualna ilosc = {}'.format(self.aktualna_ilosc))
