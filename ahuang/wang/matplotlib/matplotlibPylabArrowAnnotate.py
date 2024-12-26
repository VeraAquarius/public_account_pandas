import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建图形和子图
fig, ax = plt.subplots()

# 绘制正弦波
ax.plot(x, y)

# 添加注解，指向最大值点
max_point = np.argmax(y)
ax.annotate('Maximum', xy=(x[max_point], y[max_point]), xytext=(x[max_point], y[max_point] + 0.2),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='red',
             horizontalalignment='center', verticalalignment='bottom')

# 显示图形
plt.show()