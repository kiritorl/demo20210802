import numpy as np

# 线代
array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])
array2 = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(array1.dot(array2))

array = np.array([1, 2, 3])
print(array1.dot(array))

array3 = np.array([1, 2])
print(array3.dot(array1))

print(np.diag([1, 2, 3]))

mat = np.array([[1, 2],
                [3, 4]])
print(np.linalg.det(mat))  # 行列式

matv = np.linalg.inv(mat)  # 矩阵逆
print(np.linalg.inv(mat))
print(mat.dot(matv))

# M.dot(x) = λ*x
print(np.linalg.eig(mat))

print(mat.dot(np.array([-0.82456484, 0.56576746])))  # 列方向特征向量
print(np.array([-0.82456484, 0.56576746]) * -0.37228132)

arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)

w = np.random.uniform(-1, 1, size=(5, 5))
print(w)

# 随机漫步
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = np.random.randint(0, 100, size=(100,))
plt.plot(x, y, c="r")
plt.grid(linestyle="--", c="b")
plt.show()


# 1/(1+e^(-x))  sigmoid

# loss函数  log

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    pass


print(np.log(np.e))
print(np.pi)
