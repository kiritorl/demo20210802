import matplotlib.pyplot as plt
import numpy as np

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# bar

x = np.arange(1, 13)
y = np.random.randint(100, 900, size=(12,))
xlabel = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', '10m', '11m', '12m', ]

ax = plt.subplot()

colors = np.array(['#787878', '#784268', '#781278', '#787998',
                   '#781347', '#478278', '#137878', '#ff7878',
                   '#319878', '#648878', '#acf878', '#d32878'])

bars = ax.bar(x, y)

for bar, color in zip(bars, colors):
    bar.set_color(color)
    pass

ax.set_xlabel("month")
ax.set_ylabel("销售额")
ax.set_title("公司月度销售额（万元）")

ax.set_xticks(x)
ax.set_xticklabels(xlabel)

for x1, y1 in zip(x, y):
    plt.text(x1, y1+0.5, '%d(万元)' % y1, ha='center', va='bottom')
    pass

plt.show()
