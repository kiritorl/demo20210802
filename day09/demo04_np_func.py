import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(array + array)
print(np.add(array, array))
print(np.subtract(array, array))
print(np.square(array))
print(np.multiply(array, array))
print(np.divide(array, array))
print(np.dot(array, array))
print(np.power(2, 10))

x = np.arange(0, 10, 1)
y = np.arange(0, 10, 1)
xx, yy = np.meshgrid(x, y)
print(xx, yy)

z = np.arange(10)
# 同时对多个数据进行循环处理
for t in range(10):
    pass

for t1, t2, t3 in zip(x, y, z):
    print(t1, t2, t3)
    pass

score = np.random.randint(0, 100, size=100)
print(score)

# print(np.where(score > 90, "优", "一般"))
print(
    np.where(score > 90, "优", np.where(score > 80, "良好", np.where(score > 70, "一般", np.where(score > 60, "及格", "差")))))

array2d = np.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10]])
print(array2d.sum())
print(np.sum(array2d))

print(np.sum(array2d, axis=0))
print(np.sum(array2d, axis=1))

print(np.mean(array2d))
print(np.mean(array2d, axis=0))

print(np.cumsum(array2d))

arr3d = np.array([[[1, 2],
                   [3, 4]],
                  [[5, 6],
                   [7, 8]],
                  [[9, 10],
                   [11, 12]]])
print('3d', np.sum(arr3d, axis=0))
print('3d', np.sum(arr3d, axis=1))
print('3d', np.sum(arr3d, axis=2))

array = np.random.randint(-50, 100, size=(10,))
print(array)
print(np.argmax(array))
print(np.sign(array))

arr = np.array([-1, 2, -3, 4, 5])
print(np.sum(arr > 0))

arr.sort()
print(arr)

array2d = np.array([[8, 9, 3, 4, 5],
                    [6, 7, 8, 9, 10]])
array2d.sort(axis=0)
print(array2d)

print(np.unique(np.array([1, 1, 2, 3, 4, 5, 5, 8])))
