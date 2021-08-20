dict1 = {'userName': 'zhang', 'age': 123}
print(dict1['userName'])
print(dict1.get('userName'))
# get key不存在返回None，[]会异常

dict1['money'] = 88888
print(dict1)

v = dict1.pop('userName')
print(v)
print(dict1)

for item in dict1.items():
    print(item)
    pass

dict2 = {'userName': 'li', 'age': 321}
dict1.update(dict2)
print(dict1)

