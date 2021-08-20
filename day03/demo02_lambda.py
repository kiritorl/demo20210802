func1 = lambda x, y: x + y
print(func1(10, 20))

func2 = lambda x, y: x if x > 0 else y
print(func2(10, 20))

list1 = [1, 2, 3, 4, 5]
list2 = [x ** 2 for x in list1]
