'''Wczytuj liczby podane przez użytkownika tak długo dopóki ich suma będzie większa niż 100.'''

class Zadanie2(object):
    def __init__(self, liczba1, liczba2):
        self.liczba1 = liczba1
        self.liczba2 = liczba2
        self.suma = 0
    def sumuj(self):
        self.suma += self.liczba1 + self.liczba2
        while self.suma < 100:
            print('Suma do tej pory wynosi: ', self.suma, '\n')
            self.liczba1 = int(input('Podaj ponownie liczbe 1: '))
            self.liczba2 = int(input('Podaj ponownie liczbe 2: '))
            self.suma += self.liczba1 + self.liczba2
        print('Koncowa suma wynosi: ', self.suma)

def test():
    print('\tProgram sumujacy 2 liczby do momentu suma < 100\n')
    liczba1 = int(input('Podaj liczbe 1: '))
    liczba2 = int(input('Podaj liczbe 2: '))
    sumator = Zadanie2(liczba1, liczba2)
    sumator.sumuj()
