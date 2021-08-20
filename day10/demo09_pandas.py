import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Series
array = pd.Series([1, 2, 3, 4, 5])
print(array.values)
print(array)

array1 = pd.Series([1, 2, 3, 4, 5], index=[0, 'b', '2', 'd', 'e'])
print(array1.values)
print(array1)

print(array1.index)
print(array1['e'])

print(array1 + array1)
print(array + array1)  # NaN缺失值 根据index相处理

print(np.sum(array1))
print(array1['b':'d'])

print(2 * array1)
print(array1 > 3)
print(array1[array1 > 3])

dict1 = {"a": 1, "b": "B", "c": 3}
print(pd.Series(dict1))

print(pd.Series(dict1, index=["b", "b1", "a"]))

s2 = pd.Series(dict1, index=["b", "b1", "a"])
print(pd.notnull(s2))
print(s2[pd.notnull(s2)])

s2.name = "name"
s2.index.name = "index"
print("ssssssssssssssssssssss")
print(s2)

ss2 = pd.Series(['1', '2', '3'], index=["b", "b1", "a"])
print(ss2)
# s3 = s2.reindex([1, 2, 3, 4], method='bfill')          对已有下标进行重新排序
# s4 = s2.reindex([1, 2, 3, 4], method='ffill')
s5 = ss2.reindex(['9', 'b', '7', '6'], fill_value=0)
# print(s3)
# print(s4)
print(s5)

######
# dataframe
df = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], index=['a', 2], columns=['age', 'height', '1', '2', ''])
df1 = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], index=['a', 2], columns=['a', 'height', '2', '1', ''])
print(df)
print(df1)
print(df + df1)
print(df + df)
print(df['age'])
print(df['age'][2])

df1['g'] = [10, 11]
print(df1)

dict1 = {'Beijing': {'2001': 2.4, '2002': 2.9},
         'Tianjin': {'2001': 2.1, '2002': 2.7},
         'Shanghai': {'2001': 2.5, '2002': 2.6}}
df4 = pd.DataFrame(dict1)
print(df4)
print(df4.T)

# 广播
array1d = np.array([1, 2, 3, 4])
array2d = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8]])
array1d2 = np.array([[1],
                     [2]])
print(array1d + array2d)  # 行广播
print(np.add(array1d2, array2d))  # 列广播
