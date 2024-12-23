import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建一个新的图形对象
fig = plt.figure(figsize=(10, 6))

# 在图形对象上添加第一个子图
ax1 = fig.add_subplot(2, 1, 1)  # 2行1列的第1个
ax1.plot(x, y1)
ax1.set_title('Sine Wave')

# 在图形对象上添加第二个子图
ax2 = fig.add_subplot(2, 1, 2)  # 2行1列的第2个
ax2.plot(x, y2)
ax2.set_title('Cosine Wave')

# 显示图形
plt.show()