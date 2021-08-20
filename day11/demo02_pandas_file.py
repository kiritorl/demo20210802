import pandas as pd
import numpy as np

df = pd.DataFrame([['Tom', 30],
                   ['Jerry', 20]],
                  index=[1, 2],
                  columns=['name', 'age'])
print(df)
df.to_csv('a.csv', index=False)

df2 = pd.read_csv('a.csv')
print(df2)

df3 = pd.read_json('json.json')
print(df3)

import json
with open("json.json") as file:
    jsonStr = json.load(file)
    pass
df4 = pd.DataFrame(jsonStr)
print(df4)

# excel
qq = pd.ExcelFile('a.xls')
df5 = qq.parse("测试")
print(df5)
