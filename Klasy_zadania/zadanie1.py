# encoding: utf-8
"""class for storing products"""


class Product(object):

    """main class"""

    def __init__(self, name):
        self.name = name
        self.actual_price = 0
        self.actual_quantity = 0

    def add_quantity(self, quantity):
        if type(quantity) == int:
            if quantity > 0:
                self.actual_quantity = self.actual_quantity + quantity
            else:
                print('Podaj liczbe calkowita wieksza od 0')
        else: 
            print('Podaj liczbe calkowita')

    def change_price(self, new_price):
        if type(new_price) == float:
            self.actual_price = new_price
        else:
            print('zly format ceny')

    def sell_one(self):
        if self.actual_quantity > 0:
            self.actual_quantity -= 1
        else:
            print('brak w magazynie')

    def sell_x_pieces(self, quantity):
        if self.actual_quantity >= quantity:
            self.actual_quantity = self.actual_quantity - quantity
        else:
            print('brak odpowiedniej ilosci w magazynie')

    def check_actual_price(self):
        print('Aktualna ilosc = {}'.format(str(self.actual_quantity)))