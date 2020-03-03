import numpy as np
before = np.array([[1,2,3,4],[5,6,7,8]])
#print(before.shape)
after = before.reshape((4,2))
after1 = before.reshape((8,1))
after2 = before.reshape((2,2,2))
#print(after, "\n", after1, "\n", after2)

# vertically stacking arrays
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
#print(np.vstack([v1,v2]))
#print(np.vstack([v1,v1,v1,v2,v2,v2]))
# horizontal stacking of arrays
h1 = np.array([1,2,3,4])
h2 = np.array([5,6,7,8])
print(np.hstack([h1,h2]))
h3 = np.ones((2,3))
h4 = np.zeros((2,2))
print(np.hstack([h3,h4]))
