# encoding: utf-8
"""Program sprawdza czy wprowadzna liczba calkowia jest wieksza lub rowna 10"""


while True:
    try:
        sprawdz_liczbe = int(input('Podaj liczbe calkowita : '))
        if sprawdz_liczbe >= 10:
            print('Jestes zwyciezca')
        else:
            print('umrzyj')
        break
    except ValueError:
        print('To nie jest liczna calkowita')