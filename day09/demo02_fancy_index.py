import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array[[0, 2, 4]])

array2d = np.array([[1, 2],
                    [3, 4],
                    [5, 6],
                    [7, 8],
                    [9, 10]])
print(array2d[[1, 0, 3, 4], [0, 1, 1, 0]])
print(array2d[[1, 0, 3]])

array3d = np.arange(24).reshape((2, 3, 4))
print(array3d)
print(array3d.T)
print(array3d.T.shape)

print(array3d.transpose(2, 1, 0))
print(array3d.transpose(0, 2, 1))
