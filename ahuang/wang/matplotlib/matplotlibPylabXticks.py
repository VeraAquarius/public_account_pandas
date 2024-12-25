import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制正弦波
plt.plot(x, y)

# 设置x轴的显示范围
plt.xlim(0, 10)

# 设置x轴的刻度位置
plt.xticks([0, 2, 4, 6, 8, 10])
plt.show()

plt.plot(x, y)
# 设置x轴的刻度标签
plt.xticks([0, 2, 4, 6, 8, 10], ['0', '2', '4', '6', '8', '10'])

# 显示图形
plt.show()