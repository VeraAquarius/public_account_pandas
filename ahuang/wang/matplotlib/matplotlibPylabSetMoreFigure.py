import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# 创建一个包含多个子图的图形
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# 在第一个子图中绘制正弦波
axs[0].plot(x, y1, 'r-')
axs[0].set_title('Sine Wave')

# 在第二个子图中绘制余弦波
axs[1].plot(x, y2, 'b-')
axs[1].set_title('Cosine Wave')

# 在第三个子图中绘制正切波
axs[2].plot(x, y3, 'g-')
axs[2].set_title('Tangent Wave')

# 自动调整子图间距
plt.tight_layout()
#这个部分的数据将会添加到最后一个用过的subplot上
# plt.plot([1.5,3.5,2.6,6])
plt.show()