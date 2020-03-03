'''
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
from collections import namedtuple 
city = namedtuple('city', 'name country population coordinates')
print(city._fields)

"""
User-Defined Callable Types
Not only are Python functions real objects, but arbitrary Python objects may also be
made to behave like functions. Implementing a __call__ instance method is all it takes.
Example 5-8 implements a BingoCage class. An instance is built from any iterable, and
stores an internal list of items, in random order. Calling the instance pops an item.
Example 5-8. bingocall.py: A BingoCage does one thing: picks items from a shuffled list

'''
class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, type):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.type = type
    def getType(self):
        print("the car is of ", self.type, "type")
my_tesla = ElectricCar('tesla', 'model s', 2016, 'sedan')
print(my_tesla.get_descriptive_name())
print(my_tesla.getType())

#3f217296960694f7642692b73225c4cc332c627e719d19c7aab94787845905a2
