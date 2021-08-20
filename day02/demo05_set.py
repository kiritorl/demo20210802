set1 = {1, 2, 3, 4, 5, 7, 7, 7, 7}
print(set1)

set2 = set()  # 空集合
dict1 = {}  # 空字典 / dict()

set3 = {1, 2, 3, 8, 9}

print(set1 | set3)
print(set1 & set3)
print(set1 - set3)

print(set1.discard(10000))   # remove

set1.update([10, 11, 12])
print(set1)




