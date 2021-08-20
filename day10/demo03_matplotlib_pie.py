import matplotlib.pyplot as plt
import numpy as np

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# pie

x = np.array([100, 90, 100, 40, 70])
colors = np.array(['#787878', '#784268', '#781278', '#787998',
                   '#781347', '#478278', '#137878', '#ff7878',
                   '#319878', '#648878', '#acf878', '#d32878'])
label = ['Java', 'Python', 'BigData', 'C', 'C++']
percent = 100*x/np.sum(x)
xlabel = ["%s:%.2f%%" % (t, p) for p, t in zip(percent, label)]
plt.pie(x, colors=colors, labels=xlabel, explode=[0.1, 0, 0, 0, 0])

plt.show()
