import numpy as np

boolArray2d = np.array([[True, False, True, False],
                        [True, False, True, False]])
intArray2d = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8]])
print(intArray2d[boolArray2d])

print(intArray2d > 2)  # 返回bool数组
print(intArray2d[intArray2d % 2 == 0])

intArray = np.array([1, 3, 6, 7, 9])
mask = ((intArray % 2 == 0) & (intArray > 2))
print(mask)
print(intArray[mask])
