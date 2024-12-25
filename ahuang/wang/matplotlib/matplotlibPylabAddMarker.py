import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制正弦波，自定义颜色、线型和标记
plt.plot(x, y1, color='red', linestyle='-', marker='o', label='Sine Wave')
plt.plot(x, y2, color='blue', linestyle='--', marker='x', label='Cosine Wave')

# 添加图例
plt.legend()

# 显示图形
plt.show()