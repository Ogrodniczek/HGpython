"""Program sprawdza czy wprowadzna liczba calkowia jest wieksza lub rowna 10"""

while True:
    try:
        spr = int(input('Podaj liczbe calkowita : '))
        if  spr >= 10:
            print('Jestes zwyciezca')
        else:
            print('umrzyj')
        break
    except ValueError:
        print('To nie jest liczna calkowita')
