import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建图形和子图
fig, ax = plt.subplots()

# 绘制正弦波
ax.plot(x, y, label='sin(x)')

# 添加图例
ax.legend()

# 添加文本注解，解释一个特定的点
max_point = np.argmax(y)
ax.text(x[max_point], y[max_point], 'Maximum', fontsize=12, color='red',
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(facecolor='yellow', alpha=0.5))

# 显示图形
plt.show()