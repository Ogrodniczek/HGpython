"""Program wyszukuje liczbny addytywne"""

if __name__ == '__main__':
    ilosc_liczb = int(0)
    while ilosc_liczb <= 0:
        while True:
            try:
                ilosc_liczb = int(input('Podaj ilosc liczb : '))
                break
            except ValueError:
                print('Wprowadzona wartosc nie jest liczba calkowita')
        except False:
            print('lawl')
