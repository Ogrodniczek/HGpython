#ilosc samochodow
cars = 100
#max ilosc pasazerow
space_in_a_car = 4.0
#ilosc kierowcow
drivers = 30
#ilosc pasazerow
passengers = 90
#nieuzywane samochody
cars_not_driven =  cars - drivers
#samochody w uzyciu
cars_driven = drivers
#max ilosc pasazerow
carpool_capacity = cars_driven * space_in_a_car
#optymalne obsadzenie pasazerow
average_passengers_per_car = passengers / cars_driven


print('There are', cars, 'cars aviable.')
print('There are only', drivers, 'drivers aviable.')
print('There will be', cars_not_driven, 'empty cars today.')
print('We can transport', carpool_capacity, 'people today.')
print('We have', passengers, 'to carpool today.')
print('We need to put about', average_passengers_per_car, 'in one car.')
