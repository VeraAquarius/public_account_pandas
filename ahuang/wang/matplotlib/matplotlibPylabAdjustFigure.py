import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建一个包含多个子图的图形
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# 在第一个子图中绘制正弦波
axs[0].plot(x, y1, 'r-')
axs[0].set_title('Sine Wave')

# 在第二个子图中绘制余弦波
axs[1].plot(x, y2, 'b-')
axs[1].set_title('Cosine Wave')

# 调整子图之间的间距和子图与图形边缘的距离
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.6)

# 显示图形
plt.show()