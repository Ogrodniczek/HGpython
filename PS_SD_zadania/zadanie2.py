"""Program sumuje liczby podane przez uzytkownika do momentu az suma bedzie wieksza od 100"""

if __name__ == '__main__':
    suma = float(0)
    while suma <= 100:
        while True:
            try:
                suma += float(input('Podaj liczbe : '))
                break
            except ValueError:
                print('Wprowadzona wartosc nie jest liczba')
    print(suma)