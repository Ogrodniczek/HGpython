# encoding: utf-8
"""Program wypisuje uzytkownikow z systemu i ich domyslna powloke"""


def lista_uzytkownikow():
    """funkcja zwaraca uzytkowniko i powloke systemu w formie listy"""
    tablica = []
    handler = open('/etc/passwd', 'r')
    for users in handler:
        tablica.append(users.split(":"))
    n = 0
    while n+1 <= len(tablica):
        print(tablica[n][0], " : ", tablica[n][5])
        n += 1


if __name__ == '__main__':
    lista_uzytkownikow()
