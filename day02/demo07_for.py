array = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10]]

for row in array:
    for t in row:
        print(t, end=',')
        pass
    print()
    pass

for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=',')
        pass
    print()
    pass

def myRange(start, end, step):
    next = start + step
    while next < end:
        start = next
        yield next    # return
        next = start + step
        pass
    pass

for i in myRange(0, 1, 0.1):
    print(i)
    pass

it = iter(myRange(1, 2, 0.1))
i = next(it)
print(i)
print(next(it))

list1 = [1, 2, 3, 4, 5, 6]
list2 = list1[1:]
print(list2)

list3 = list1[::-1]
print(list3)







