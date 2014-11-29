#Popros uzytkownika o podanie liczby X i sprawdz czy liczba X jest: wieksza lub rowna (>=) 10 mniejsza niz 10 lub inne
#dana_liczba = int( input ('Podaj liczbe X: '))
#cos tutaj powinno byc przed if
#if dana_liczba <= 10:
   # print('skurwysynu daj wiecej')
while True:
    try:
        input = int(input('Podaj liczbe X: '))
        #sprawdz czy wpisane dane sa w zasiegu
        if input in range(1,10):
            break
            print('dasz wincyj to pieklo sie skonczy')
        else:
            print('Sorki, troszke za duzo albo to nie liczba')
    except:
        print('Mialy byc liczby oszukancze wstretny, idziesz do wiezienia na kolejke')
        break

#else:
   # print('brawo, podales wiecej niz 10 lub nawet 10')



