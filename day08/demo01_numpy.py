import numpy as np

array = np.array([1, 2, 3, 4, 5])

array2d = np.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10]], dtype=np.int64)

print(array2d.shape)
print(array2d.dtype)

print(np.zeros(shape=(5, 5)))
print(np.empty(shape=(5, 5)))
print(np.ones(shape=(5, 5)))
print(np.identity(5))
print(np.eye(5, 6))
print(np.arange(5))
print(np.arange(0, 5, 0.1))

print(np.zeros_like(array2d))

matrix = np.matrix([[1, 2, 3],
                    [4, 5, 6]])
matrix2 = np.matrix([[1, 2],
                     [3, 4],
                     [5, 6]])
print(matrix * matrix2)

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[1, 2], [3, 4], [5, 6]])
print(array1.dot(array2))

arrayStr = np.array(['111', '222', '333'], dtype=np.str)

print(arrayStr.astype(dtype=np.int))
