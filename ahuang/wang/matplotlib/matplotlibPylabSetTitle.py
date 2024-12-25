import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体，解决中文显示问题
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 创建数据
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 创建图形和子图
fig, ax = plt.subplots()

# 绘制折线图
ax.plot(x, y)

# 设置中文标题
ax.set_title('折线图示例')

# 显示图形
plt.show()