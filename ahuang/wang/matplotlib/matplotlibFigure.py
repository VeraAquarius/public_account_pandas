import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 使用pylab模式绘图
plt.plot(x, y)
plt.title('Pylab Mode Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()

# 使用Figure和subplot创建图形
fig, ax = plt.subplots(2, 1)  # 创建一个包含2个子图的Figure

# 在第一个子图上绘图
ax[0].plot(x, y)
ax[0].set_title('Subplot 1')

# 在第二个子图上绘图
ax[1].plot(x, np.cos(x))
ax[1].set_title('Subplot 2')

# 调整子图间距
plt.tight_layout()
plt.show()