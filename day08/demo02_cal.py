import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array ** 0.5)
print(np.sqrt(array))
print(np.log(array))
print(np.exp(array))

array1 = np.arange(1, 11)
print(array1[0])
print(array1[-1])
print(array1[1:5])
array1[0:5] = 10
print(array1)
array1[:] = 0
print(array1)

array2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array2d[0, 0])
print(array2d[1:, 2:])
print(array2d.T)

array3d = np.arange(1, 21).reshape(2, 2, 5)
print(array3d)
print(array3d[1, 1, 0])
print(array3d[1:2, :, 1:].shape)
