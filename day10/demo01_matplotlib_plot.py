import matplotlib.pyplot as plt
import numpy as np

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# plt
x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x, y, c="r")
plt.show()


