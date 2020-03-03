import numpy as np
a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a.ndim)
print(a.shape)
print(a)
# accessing a specific element
print(a[1,0,2]) # gives 9 from outside, element, row, element pos. in row
print(a[:,1,1])
print(a[:,1,2]) #a[:->all elements of col, row position, element index in row specified]
print(a[:,0,1])
print(a[:,:,1])#a[:->all elements of col, all row, element index in row specified]
# replacing
a[1,:,:] = [[7,8,6],[1,0,0]]
print(a[1,:,:])
