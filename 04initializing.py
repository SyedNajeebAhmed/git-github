import numpy as np
# all zeros matrix
a = np.zeros((2,2)) # 2d array
b = np.zeros((2,2,2)) # 3d array
c = np.zeros((2,3,2,2)) # 4d array
#print(a,"**\n",b,"**\n",c)
# all ones matrix
d = np.ones((2,2)) # 2d array
e = np.ones((2,2,2)) # 3d array
f = np.ones((2,3,2,2), dtype='int32') # 4d array
#print(d,"**\n",e,"**\n",f)
# any other number
g = np.full((2,2),99, dtype = 'float32')
#print(g)
# any other number full_like
h = np.array([[2,2,2],[3,3,3]])
i = np.full_like(h, 4) # or i = np.full(h.shape, 4)
#print(i)
# generating random decimal no.s
j = np.random.rand(4,2,2) # pass the shape as parameter
#print(j)
k = np.random.random_sample(h.shape)
#print(k)
l = np.random.randint(7)
m = np.random.randint(7, size=(3,3))
n = np.random.randint(-4,7, size=(3,3))
#print(l,"\n",m,"\n",n)
# the identity matrix
o = np.identity(5)
#print(o)
# repeat an array
p = np.array([[1,2,3,4],[5,6,7,8]])
q = np.repeat(p,3, axis=0)
#print(q)
# game
output = np.ones((5,5))
zero = np.zeros((3,3))
zero[1,1] = 9
#print(output, "\n", zero)
output[1:4, 1:4] = zero
#print(output)
r = np.array([1,2,3])
s = r
s[0] = 100
#print(s, "\n,", r)
t = np.array([1,2,3])
u = t.copy()
u[0] = 100
#print(t, "\n,", u)

