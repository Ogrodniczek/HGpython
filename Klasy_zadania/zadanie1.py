class Produkt(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.aktualna_cena = 0
        self.aktualna_ilosc = 0
    def dodaj_ilosc(self, ilosc):
        if type(ilosc) == int:
            if ilosc > 0:
                self.aktualna_ilosc = self.aktualna_ilosc + ilosc
            else:
                print('Podaj liczbe calkowita wieksza od 0')
        else: 
            print('Podaj liczbe calkowita')
    def zmien_cene(self, nowa_cena):
        if type(nowa_cena) == float:
            self.aktualna_cena = nowa_cena
        else:
            print('zly format ceny')
    def sprzedaj_szuke(self):
        if self.aktualna_ilosc > 0:
            self.aktualna_ilosc = self.aktualna_ilosc - 1
        else:
            print('brak w magazynie')
    def sprzedaj_sztuki(self, ilosc):
        if self.aktualna_ilosc >= ilosc:
            self.aktualna_ilosc = self.aktualna_ilosc - ilosc
        else:
            print('brak odpowiedniej ilosci w magazynie')
    def sprawdz_aktualna_ilosc(self):
        print('Aktualna ilosc = {}'.format(str(self.aktualna_ilosc)))
