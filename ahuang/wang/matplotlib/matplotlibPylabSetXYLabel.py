import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置中文字体，解决中文显示问题
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建图形和子图
fig, ax = plt.subplots()

# 绘制正弦波
ax.plot(x, y)

# 设置x轴和y轴的标签
ax.set_xlabel('时间 (s)', fontsize=14, color='blue')
ax.set_ylabel('振幅', fontsize=14, color='green')

# 显示图形
plt.show()