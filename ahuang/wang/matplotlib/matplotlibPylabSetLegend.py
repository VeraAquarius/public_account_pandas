import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建图形和子图
fig, ax = plt.subplots()

# 绘制正弦波和余弦波，并添加标签
line1, = ax.plot(x, y1, label='sin(x)')
line2, = ax.plot(x, y2, label='cos(x)')

# 添加图例，自动选择最佳位置
legend = ax.legend(loc='best')

# 显示图形
plt.show()