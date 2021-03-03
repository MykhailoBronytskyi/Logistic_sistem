'''Module that creates basic objects like Location, Vehicle and Item
to create NovaPoshta Logistic System'''

from typing import List

class Location:
    '''Location were to deliver a thing
    >>> place = Location('Lwiw', 121)
    >>> place.__class__.__name__
    'Location'
    '''
    def __init__(self, city: str=None, postoffice: int=None):
        '''Initialises a place for a deliver
        >>> place = Location('Lwiw', 121)
        >>> print(place.city, place.postoffice)
        Lwiw 121

        >>> place = Location()
        >>> print(place.city, place.postoffice)
        None None
        '''
        self.city = city
        self.postoffice = postoffice


class Item:
    '''Creates an item object for further delivery
    >>> thing = Item('orange', 15)
    >>> thing.__class__.__name__
    'Item'
    '''
    def __init__(self, name: str='No_thing', price: float=0):
        '''Initialises name and price for an item
        >>> thing = Item('orange', 15)
        >>> print(thing.name, thing.price)
        orange 15
        '''
        self.name = name
        self.price = price

    def __str__(self) -> str:
        '''Prints information messege to a user
        >>> thing = Item('orange', 15)
        >>> print(thing)
        The item orange has 15 cost.
        ''' 
        return f'The item {self.name} has {self.price} cost.'


class Vehicle:
    '''Initialises a vehicle object for further delivery of an item
    >>> transport = Vehicle(17)
    >>> transport.__class__.__name__
    'Vehicle'
    '''

    # vehicleNo = 0
    def __init__(self, vehicleNo: int, isAvailable: bool=True):
        '''Initialises properties for a vehhiacle.
        Number of car gives the user.
        BUT!!! Each vehicle has to have unique number.

        >>> transport = Vehicle(17)
        >>> print(transport.vehicleNo, transport.isAvailable)
        17 True
        >>> transport = Vehicle(19, False)
        >>> print(transport.vehicleNo, transport.isAvailable)
        19 False
        '''
        self.isAvailable = isAvailable

        # Vehicle.vehicleNo += 1
        self.vehicleNo = vehicleNo


class Order:
    '''An object that has all the infomation about
    user's order
    >>> orange = Item('orange', 15)
    >>> hat = Item('hat', 35)
    >>> fridge = Item('fridge', 1000)

    >>> order = Order('John', 'Lviv', 121, [orange, hat, fridge])
    Your order number is 100001.
    '''
    
    order_id = 100000


    def __init__(self, user_name: str, location: Location, postoffice: int, items: list, vehicle: object=None):
        '''Initialises an order information
        >>> orange = Item('orange', 15)
        >>> hat = Item('hat', 35)
        >>> fridge = Item('fridge', 1000)

        >>> my_order = Order('John', 'Lviv', 121, [orange, hat, fridge])
        Your order number is 100002.

        >>> print(my_order.user_name, my_order.location.city ,my_order.orderid)
        John Lviv 100002
        '''
        self.user_name = user_name
        self.location = Location(location, postoffice)
        self.items = items[:]

        Order.order_id += 1
        self.orderid = Order.order_id
        self.vehicle = vehicle
        print(f'Your order number is {self.orderid}.')
 

    def calculateAmount(self) -> float:
        '''Calculates the total prise of delivery
        >>> orange = Item('orange', 15)
        >>> fridge = Item('fridge', 1000)

        >>> order = Order('John', 'Lviv', 121, [orange, fridge])
        Your order number is 100005.
        >>> order.calculateAmount()
        1015
        '''

        total_price = 0
        for item in self.items:
            total_price += item.price
        
        return total_price

        
    def assignVehicle(self, vehicle: Vehicle):
        '''To assign given Vehicle to a delivery
        >>> orange = Item('orange', 15)
        >>> order = Order('John', 'Lviv', 121, [orange])
        Your order number is 100004.

        >>> car = Vehicle(10)
        >>> print(order.vehicle)
        None
        >>> order.assignVehicle(10)
        >>> print(order.vehicle.vehicleNo)
        10
        '''
        self.vehicle = Vehicle(vehicle)


    def __str__(self) -> str:
        '''Prints information messege to a user
        >>> orange = Item('orange', 15)
        >>> order = Order('John', 'Lviv', 121, [orange])
        Your order number is 100003.

        >>> print(order)
        Your order #100003 is sent to Lviv. Total price: 15 UAH.
        '''
        price = self.calculateAmount()
        return f'Your order #{self.orderid} is sent to {self.location.city}. Total price: {price} UAH.'

    # def __repr__(self):
    #     return 'Second yes'

# item = Item('a_thing', 10)
# my_order = Order('A', 'Lwiw', [item])
# print(my_order.calculateAmount())
# print(my_order)
# # my_order()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
