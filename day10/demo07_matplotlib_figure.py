import matplotlib.pyplot as plt
import numpy as np

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False
figure = plt.figure()

ax = figure.add_subplot(2, 2, 1)
x = np.arange(1, 13)
y = np.random.randint(100, 900, size=(12,))
xlabel = ['1m', '2m', '3m', '4m', '5m', '6m', '7m', '8m', '9m', '10m', '11m', '12m', ]

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

ax2 = figure.add_subplot(2, 2, 2)
x = np.array([100, 90, 100, 40, 70])
colors = np.array(['#787878', '#784268', '#781278', '#787998',
                   '#781347', '#478278', '#137878', '#ff7878',
                   '#319878', '#648878', '#acf878', '#d32878'])
label = ['Java', 'Python', 'BigData', 'C', 'C++']
percent = 100*x/np.sum(x)
xlabel = ["%s:%.2f%%" % (t, p) for p, t in zip(percent, label)]
ax2.pie(x, colors=colors, labels=xlabel, explode=[0.1, 0, 0, 0, 0])

ax3 = figure.add_subplot(2, 1, 2)
x = np.random.randn(1, 1000)
y = np.random.randn(1, 1000)

x1 = np.random.randn(1, 1000)
y1 = np.random.randn(1, 1000)

ax3.scatter(x, y, c="r", alpha=0.5, s=20, marker="+")
ax3.scatter(x1, y1, c="b", alpha=0.5, s=20, marker="p")

plt.show()
