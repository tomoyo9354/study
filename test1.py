import numpy as np

# a = np.array([[1,2],
#              [0,1]])
# b = np.arange(4).reshape((2,2))
# c = a*b
# c_dot = np.dot(a,b)
# print('a:',a)
# print('b:',b)
# print('c:',c)
# print('c_dot:',c_dot)

# a = np.random.random((2,4))
# print('a:',a)
# print('和为:',np.sum(a))
# print('最大值为:',np.max(a))
# print('最小值为:',np.min(a))

a = np.arange(2,14).reshape(3,4)
print(a)
print('最小值的索引为:',np.argmin(a))
print(np.ndim(a))
print(np.shape(a))
print(a.itemsize)