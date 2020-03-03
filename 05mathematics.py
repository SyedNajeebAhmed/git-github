import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
c = np.array([1,2,3,4])
d = np.array([1,2,3,4])
e = np.array([1,2,3,4])
"""print(a + 2)
print(b - 2)
print(c * 2)
print(d / 2)
print(e ** 2)
print(a + b)
print(np.cos(a))
print(np.sin(a))"""

# linear algebra

f = np.ones((2,3))
g = np.full((3,2), 4)
#print(f,"\n",g,"\n", np.matmul(f,g)) # row 0 x col 0 and row 1 x col 1 f's col and g's rows to be matched

# finding determinant
h = np.identity(4)
#print(np.linalg.det(h))

# statistics
stat = np.array([[1,2,12,-1],[5,9,7,8]])
print(np.min(stat), np.max(stat))
print(np.min(stat, axis=0),"\n", np.max(stat, axis=1),"\n", np.sum(stat),"\n", np.sum(stat, axis=1),"\n",np.sum(stat, axis=0))
