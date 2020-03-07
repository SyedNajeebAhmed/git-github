#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""" The collection Module ---
1)Chain Map 2)defaultdict 3)deque 4)named tuple 5)Ordered Dict 6)Counter
"""


# In[1]:


symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
codes


# In[3]:


# List Comprehension for above -- values = [expression for value in collection filter condition]
#general form 1) values = [ ] 2) for value in collection 3) filter(if) condition 4)values.append(expression)
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
codes


# In[4]:


# The same list built by a listcomp and a map/filter composition
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127] # GREATER THAN 127 IS BEYOND ASCII
codes


# In[5]:


symbols = '$¢£¥€¤'
codes = list(filter(lambda symbol : symbol > 127, map(ord, symbols)))
codes


# In[7]:


#Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['s','m','l']
items = [(color, size) for color in colors for size in sizes]
items


# In[8]:


# Generator Expression - comprehension when target is not list.
symbols = '$¢£¥€¤'
codes = tuple(ord(symbol) for symbol in symbols)
codes


# In[13]:


import array
symbols = '$¢£¥€¤'
codes = array.array('I',(ord(symbol) for symbol in symbols))
codes


# In[16]:


#Cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['s','m','l']
for tshirt in (f"{color} {size}" for color in colors for size in sizes):
    print (tshirt)


# In[22]:


# Tuples used as Records

lax_coordinates = (33.9425, -118.408056)

city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids): #As we iterate over the list, passport is bound to each tuple
     print('%s/%s' % passport) #The % formatting operator understands tuples and treats each item as a separate field.
    
for country, _ in traveler_ids: #Here we are not interested in the second item, so it’s assigned to_, a dummy variable.
    print(country)


# In[8]:


# Tuple unpacking

lax_coordinates = (33.9425, -118.408056)

latitude, longitude = lax_coordinates # tuple unpacking

print(latitude)
print(longitude)


# In[1]:


divmod(20, 8) # returns tuple with quotient and remainder


# In[3]:


#Another example of tuple unpacking is prefixing an argument with a star when calling a function:

t = (20, 8)
divmod(*t)
quotient, remainder = divmod(*t)
quotient, remainder


# In[11]:


#Sometimes when we only care about certain parts of a tuple when unpacking, a dummy variable like _ is used as placeholder

import os
_, filename = os.path.split('D:\\najeeb\\pythonBooks\\introduction1.txt')
filename


# In[14]:


#Using * to grab excess items
a, b, *rest = range(5)
print(a,b,rest)
a, *body, c, d = range(5)
*head, b, c, d = range(5)
print(a, body, c, d)
print(head, b, c, d)


# In[34]:


# Nested Tuple Unpacking

metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]
print('{:23} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas: #By assigning the last field to a tuple, we unpack the coordinates
      if longitude <= 0: # limits the output to metropolitan areas in the WesternHemisphere
         print(fmt.format(name, latitude, longitude))


# In[3]:


# Defining and using a named tuple type

from collections import namedtuple 

city = namedtuple('city', 'name country population coordinates')#Two parameters are required to create a named tuple: 
#a class name and a list of field names, which can be given as an iterable of strings or as a single spacedelimitedstring.

tokyo = city('tokyo', 'japan', 100000, (25.8, 78.9)) # instantiating a named tuple from an iterable
print(tokyo)
print(tokyo.population) # You can access the fields by name or position
print(tokyo.country)
print(tokyo.coordinates)
print(tokyo[1])


# In[13]:


# A named tuple type has a few attributes in addition to those inherited from tuple...example shows the most useful: 
#the _fields class attribute, the class method_make(iterable), and the _asdict() instance method
# Named tuple attributes and methods

from collections import namedtuple 
city = namedtuple('city', 'name country population coordinates')
print(city._fields) # _fields is a tuple with the field names of the class

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

delhi = city._make(delhi_data)# _make() allow you to instantiate a named tuple from an iterable; City(*delhi_data)
#would do the same as in previous example

print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)
    
#_asdict() returns a collections.OrderedDict built from the named tuple instance. 
#That can be used to produce a nice display of city data.


# In[15]:


# Basic operations with rows and columns in a numpy.ndarray

import numpy as np 
a = np.arange(12)
print(a)
print("the type is : ", type(a))
print("the shape is : ", a.shape)
a.shape = 3, 4
print("the modified shape is : ", a)
print("\n", a[2], "\n", a[2, 1], "\n", a[:, 1])
print("the transposed array is :", a.transpose())


# In[20]:


# Working with a deque

from collections import deque
dq = deque(range(10), maxlen = 10)

print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 22, 33])
print(dq)

dq.extendleft([10, 20, 30, 40])
print(dq)

