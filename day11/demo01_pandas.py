import pandas as pd
import numpy as np

s1 = pd.Series([10, 2, 3, 4, 5], index=list("bacde"))
print(s1)

print(s1.sort_values())
print(s1.sort_index())

s2 = s1.drop("c")
print(s2)

df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6]], index=[1, 2], columns=list("abc"))
print(df)

df2 = df.drop(columns=['a'])
print(df2)
df3 = df.drop(['a'], axis=1)
print(df3)

df4 = pd.DataFrame([[1, 2, 3],
                    [4, 5, 6]], index=[1, 2], columns=list("abc"))

df5 = pd.DataFrame([[1, 2, 3],
                    [4, 5, 6]], index=[1, 2], columns=list("abf"))

df6 = df4.add(df5, fill_value=0)
print(df6)

print(df4.loc[2])
print(df4 - df4.loc[1])

df4 = pd.DataFrame([[7, 2, 8],
                    [1, 5, 6]], index=[1, 2], columns=list("abc"))
print(df4.sort_values(by=['c']))
