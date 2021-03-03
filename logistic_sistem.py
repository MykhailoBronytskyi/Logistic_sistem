'''Moin module with Logistic system'''

from typing import List
from order_of_delivery import Location, Item, Vehicle, Order


class LogisticSystem:
    '''Class that controls the delivery prosess
    >>> vehicles = [Vehicle(1), Vehicle(2)]
    >>> logSystem = LogisticSystem(vehicles)

    >>> my_items = [Item('book',110), Item('chupachups',44)]
    >>> my_order = Order(user_name = 'Oleg', location = 'Lviv', postoffice = 53, items = my_items)
    Your order number is 100001.
    >>> logSystem.placeOrder(my_order)
    >>> logSystem.trackOrder(100001)
    Your order #100001 is sent to Lviv. Total price: 154 UAH.

    >>> my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
    >>> my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    Your order number is 100002.
    >>> logSystem.placeOrder(my_order2)
    >>> logSystem.trackOrder(100002)
    Your order #100002 is sent to Odessa. Total price: 164.33 UAH.

    >>> my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
    >>> my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    Your order number is 100003.
    >>> logSystem.placeOrder(my_order3)
    There is no available vehicle to deliver an order.
    >>> logSystem.trackOrder(100003)
    No such order.
    '''

    all_the_orders = []

    def __init__(self, vehicles: List[Vehicle], orders: list = []):
        '''Initialises two data_list of available vehicles and given orders'''
        self.orders = orders[:]
        self.vehicles = vehicles[:]


    def placeOrder(self, new_order: Order):
        '''Try to plase an order to free vehicle. In case of
        unavailable transport prints appropriate messege'''
        for car in self.vehicles:
            if car.isAvailable:
                car.isAvailable = False
                new_order.vehicle = car

                LogisticSystem.all_the_orders += [new_order]  # or just car
                self.orders = LogisticSystem.all_the_orders[:]

                return None
        print('There is no available vehicle to deliver an order.')


    def trackOrder(self, order_id: int):
        '''Find out in what stage is your order now'''
        for order in LogisticSystem.all_the_orders[:]:
            if order.orderid == order_id:
                print(order)
                return
        print('No such order.')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
