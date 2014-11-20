"""Program wyszukuje liczbny addytywne"""

if __name__ == '__main__':
    ilosc_liczb = int(0)
    tablica = []
    odwrotna_tablica = []
    while ilosc_liczb <= 0:
        while True:
            try:
                ilosc_liczb = int(input('Podaj ilosc liczb : '))
                break
            except ValueError:
                pass
    for i in range(0, ilosc_liczb):
        while True:
            try:
                liczba =  int(input('Podaj liczbe nr ' + str(i+1) + ' : ' ))
                break
            except ValueError:
                pass
        tablica.append(liczba)
    for n in range(0, ilosc_liczb):
        odwrotna_liczba = - int(tablica[n])
        odwrotna_tablica.append(odwrotna_liczba)
    for x in range(0, ilosc_liczb):
        print(tablica[x], odwrotna_tablica[x])
