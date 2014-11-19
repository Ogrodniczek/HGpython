'''Poproś użytkownika o podanie liczby X i sprawdź czy liczba X jest: 
większa lub równa (>=) 10 mniejsza niż 10 lub inne.'''

class Porownanie(object):
    def __init__(self, x):
        self.x = x
    def sprawdz(self):
        if self.x >= 10:
            print('Podana liczba jest wieksza lub rowna 10')
        elif self.x < 10:
            print('Podana liczba jest mniejsza niz 10')
        else:
            print('Liczba Inna (jakkolwiek to brzmi :P)')

def test():
    liczba = int(input('Podaj liczbe aby sprawdzic jej polozenie wzgledem liczby 10: '))
    l1 = Porownanie(liczba)
    l1.sprawdz()
