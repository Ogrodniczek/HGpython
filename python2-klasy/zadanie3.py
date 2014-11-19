'''prosty kalkulator z prostym interface przy zaimplementowaniu switch'''

def switch(opcja, liczba1, liczba2):

    slownik = dict([('dodawanie', 1), ('odejmowanie', 2), ('mnozenie', 3), ('dzielenie', 4), ('zmiana_liczb', 5)])

    if slownik['dodawanie'] == opcja:
        print('Suma: ', liczba1+liczba2)
    elif slownik['odejmowanie'] == opcja:
        print('Roznica: ', liczba1-liczba2)
    elif slownik['mnozenie'] == opcja:
        print('Iloczyn: ', liczba1*liczba2)
    elif slownik['dzielenie'] == opcja:
        if liczba2 == 0:
            print('Nie dziel cholero przez zero! :D')
            switch(5, liczba1, liczba2)
        print('Iloraz: ', liczba1/liczba2)
    elif slownik['zmiana_liczb'] == opcja:
        liczba1 = int(input('Podaj pierwsza liczbe: '))
        liczba2 = int(input('Podaj druga liczbe: '))
        kalkulator(liczba1, liczba2)
    else:
        print('podano zla opcje...\nPodaj jeszcze raz!')
        kalkulator(liczba1, liczba2)

    kalkulator(liczba1, liczba2)

def kalkulator(liczba1, liczba2):

    print('\nPodane liczby to: ', liczba1, ' i ', liczba2) 
    print('\n\t\tProsty kalkulator')
    print('\t1: Dodawanie')
    print('\t2: Odejmowanie')
    print('\t3: Mnozenie')
    print('\t4: Dzielenie')
    print('\t5: Zmiana wprowadzonych liczb')
    print('\t0: Wyjscie z programu')

    opcja = int(input('wybierz opcje: '))

    if opcja != 0:
        switch(opcja, liczba1, liczba2)
        del liczba1, liczba2
        

def test():

    liczba1 = int(input('Podaj pierwsza liczbe: '))
    liczba2 = int(input('Podaj druga liczbe: '))
    kalkulator(liczba1, liczba2)


