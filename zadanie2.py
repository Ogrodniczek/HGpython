kot = 0
while True:
    koty = int(input('Podaj liczbe, znajdziesz sie na karuzeli pytan: '))
    kot += koty
    #Sprzwdzanie czy liczba znajduje sie w zasiegu petli
    if kot <= 100:
        print('Daj wincyj do pieca, bo to sie nie skonczy... ')
    else:
        print ('Udalo ci sie, koksownik jest pelen ')
        break
