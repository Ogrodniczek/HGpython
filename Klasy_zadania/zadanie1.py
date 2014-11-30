# encoding: utf-8
"""class for storing products"""


class Product(object):

    def __init__(self, name):
        self.name = name
        self.actual_price = 0
        self.actual_quantity = 0
        self.price_history = []
        self.how_many_at_price = []

    def add_quantity(self, quantity):
        if type(quantity) == int:
            if quantity > 0:
                self.actual_quantity += quantity
            else:
                print('Podaj liczbe calkowita wieksza od 0')
        else: 
            print('Podaj liczbe calkowita')

    def change_price(self, new_price):
        if type(new_price) == float:
            self.actual_price = new_price
        else:
            print('zly format ceny')
        self.price_history.append(new_price)

    def sell_one(self):
        if self.actual_quantity > 0:
            self.actual_quantity -= 1
        else:
            print('brak w magazynie')
        self.how_many_at_price.append([self.actual_price, 1])

    def sell_x_pieces(self, quantity):
        if self.actual_quantity >= quantity:
            self.actual_quantity -= quantity
        else:
            print('brak odpowiedniej ilosci w magazynie')
        self.how_many_at_price.append([self.actual_price, quantity])

    def check_actual_price(self):
        print('Aktualna ilosc = {}'.format(str(self.actual_quantity)))

    def show_price_history(self):
        print('Historia cen : ', self.price_history)

    def show_average_price(self):
        print('Srednia cena = ', sum(self.price_history) / len(self.price_history))

    def sales_history(self):
        print(self.how_many_at_price)