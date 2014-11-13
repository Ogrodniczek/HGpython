class Produkt(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.aktualna_cena = 0
        self.aktualna_ilosc = 0
        self.historia_cen = []

    def dodaj_ilosc(self, ilosc):
        self.aktualna_ilosc = self.aktualna_ilosc + ilosc

    def zmien_cene(self, nowa_cena):
        self.aktualna_cena = nowa_cena
        self.historia_cen.append(nowa_cena)

    def sprzedaj_sztuke(self):
        self.aktualna_ilosc = self.aktualna_ilosc - 1
            if self.aktualna_ilosc < 0:
                print('ilosc w magazynie nie moze byc ujemna')

    def sprzedaj_sztuki(self, ilosc):
        self.aktualna_ilosc = self.aktualna_ilosc - ilosc
            if self.aktualna_ilosc < 0:
                print('ilosc w magazynie nie moze byc ujemna')

    def sprawdz_aktualna_ilosc(self):
        print('Aktualna ilosc to {}'.format(self.aktualna_ilosc))

    def sprawdz_srednia_cene(self):
        srednia_cena = 0
        ilosc_cen = 0
        for i in range(len(self.historia_cen)):
            srednia_cena = srednia_cena + self.historia_cen[i]
            ilosc_cen = ilosc_cen + 1
        print('Srednia cena wynosi: ', srednia_cena/ilosc_cen)

    def pokaz_historie_cen(self):
        for i in range(len(self.historia_cen)):
            print(i, ': ', self.historia_cen[i])

#Przyklad uzycia
#def przyklad():
produkt1 = Produkt('zeszyt')
produkt1.dodaj_ilosc(5)
produkt1.zmien_cene(5)
produkt1.zmien_cene(10)
produkt1.sprzedaj_sztuke()
produkt1.sprawdz_aktualna_ilosc()
produkt1.pokaz_historie_cen()
produkt1.sprawdz_srednia_cene()


