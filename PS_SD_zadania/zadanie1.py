while True:
    try:
        x = int(input('Podaj liczbe calkowita : '))
        if x >= 10:
            print('Jestes zwyciezca')
        else:
            print('umrzyj')
        break
    except ValueError:
        print('To nie jest liczna calkowita')
