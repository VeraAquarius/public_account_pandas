import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建图形和子图
fig, ax = plt.subplots()

# 绘制正弦波
ax.plot(x, y)

# 设置x轴的刻度位置
ax.set_xticks([0, np.pi, 2 * np.pi])

# 设置x轴的刻度标签，包括旋转角度和字体大小
ax.set_xticklabels(['0', 'π', '2π'], rotation=45, fontsize=12)

# 显示图形
plt.show()