import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建一个包含多个子图的图形，设置图形尺寸和背景颜色
fig, axs = plt.subplots(2, 1, figsize=(8, 6), facecolor='lightblue', dpi=100)

# 在第一个子图中绘制正弦波
axs[0].plot(x, y1, 'r-')
axs[0].set_title('Sine Wave')

# 在第二个子图中绘制余弦波
axs[1].plot(x, y2, 'b-')
axs[1].set_title('Cosine Wave')

# 显示图形
plt.show()