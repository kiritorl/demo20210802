import numpy as np
import pandas as pd

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.mean(array))
print(np.median(array))

s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(s1.describe())

print(array - array.mean())  # 偏差
print(array.var())  # 方差
print(array.std())

array1 = np.array([1, 2, 3])
array2 = np.array([3, 4, 5])
array3 = np.array([3, 6, 7])
print(np.cov(array1, array2))  # 协方差
array4 = np.array([array1,
                   array2,
                   array3])
print(np.corrcoef(array4))  # 相关性
