x = raw_input('Podaj liczbe : '))
if type(x) == int or type(x) == float:
    if x >= 10.0:
        print('Jestes zwyciezca')
    else:
        print('Umrzyj')
else:
    print(x, ' nie jest liczba')
