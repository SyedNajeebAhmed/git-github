import numpy as np 
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
# get a specific element(row, column)
print(a[1,5]) # 1st row , 5th column
print(a[1,-2])
# get a specific row
print(a[0,:]) # all the elements of 0th row
# get a specifc column
print(a[:, 2]) # all the elements of 2nd column
# slicing operations array[specific row, start index:end index:step value]
print(a[1, 2:5:2])
print(a[0, 2:-2:2])
# accessing specific element array[row,index position of element to access]
#array[:, index position of element to access] - : -> represents columns
a[1,5] = 20
print(a)
a[:, 2] = [2,6]
print(a)
