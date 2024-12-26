import matplotlib.pyplot as plt
import numpy as np

# 设置全局参数
plt.rc('font', size=14)  # 设置字体大小
plt.rc('axes', titlesize=16)  # 设置坐标轴标题大小
plt.rc('figure', figsize=(10, 6))  # 设置图形尺寸
plt.rc('lines', linewidth=2, color='blue')  # 设置线条的默认宽度和颜色

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制正弦波和余弦波
plt.plot(x, y1, label='Sine Wave')
plt.plot(x, y2, label='Cosine Wave')

# 添加标题和图例
plt.title('Sine and Cosine Waves')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# 显示图形
plt.show()