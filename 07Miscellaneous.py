import numpy as np
"""
filedata = np.genfromtxt('08data.txt', delimiter=',')
#print(filedata)
print(filedata.astype('int32'))

# boolean masking and advance indexing
#print(filedata > 50)
#print(filedata[filedata > 10])
print(np.any(filedata > 200, axis=0)) # axis = 0 compares col wise.
print(np.any(filedata > 100, axis=1)) # axis = 1 compares row wise
print(np.all(filedata > 7, axis=0)) # axis = 0 compares col wise.
print(np.all(filedata > 10, axis=1)) # axis = 1 compares row wise

# we can index with a list in NumPy
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,4,6]]) # gives element of the particular position indices passed in the list


01 02 03 04 05
06 07 08 09 10
11 12 13 14 15 
16 17 18 19 20
21 22 23 24 25 
26 27 28 29 30


"""
# accessing 11,12,16,17
a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(a)
print(a[2:4,0:2])
# accessing 2,8,14,20
print(a[[0,1,2,3],[1,2,3,4]])
# accessing 4,5,24,25,29,30
print(a[[0,4,5],3:])
