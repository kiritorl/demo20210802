# 导入requests模块
import requests
import matplotlib.pyplot as plt
import numpy as np

# 通过网络地址访问获取数据
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# 向服务器发送请求
r = requests.get(url)
print('数据访问状态值:> ', r.status_code)
print('成功：正常获取网站数据' if r.status_code == 200 else '错误：无法获取网站数据')
# 将获取的数据转换成json字典
response_dict = r.json()

# 获取所有的<item>标签（1个item即为一条数据）
repo_dicts = response_dict['items']
# 使用推导式获取数据
names = [repo_dict['name'] for repo_dict in repo_dicts]
plot_dicts = [repo_dict['stargazers_count'] for repo_dict in repo_dicts]

# 创建柱状图
x = np.arange(len(names))
plt.bar(x, plot_dicts)

# 创建点线图
plt.plot(x, plot_dicts, 'rp-')

# 使用subplot()方法创建一个画布
ax = plt.subplot()
# 设置y轴的标题
ax.set_ylabel('stargazers_count')
ax.set_xlabel('Github Reponstorys')
# x轴每个标签的具体位置，设置为每个柱的中央
ax.set_xticks(x)
# 设置每个标签的名字
ax.set_xticklabels(names, rotation=90)
# 为图标添加标题
ax.set_title('Github')

# 显示
plt.grid(linestyle='--')
plt.show()
