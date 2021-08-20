import numpy as np

array2d = np.arange(12).reshape(3, 4)
print(array2d)

array2d.tofile("a.bin")

rarray2d = np.fromfile("a.bin", dtype=int)
print(rarray2d)
print(rarray2d.reshape(3, 4))

np.save("a.npy", array2d)
b = np.load("a.npy")
print(b)

a = np.arange(20).reshape(4, 5)
b = np.array([1, 2, 3, 4, 5])
c = np.arange(12).reshape(3, 4)

np.savez("a.npz", a, b, c=c)
dictArray = np.load("a.npz")
print(dictArray['arr_0'])
print(dictArray['arr_1'])
print(dictArray['c'])

# 保存为文本文件
np.savetxt("a.csv", array2d, delimiter=",")  # delimiter分隔符 默认空格
arr = np.loadtxt("a.csv", delimiter=",")  # 保存更改分隔符 还原需要更改分隔符
print(arr)
