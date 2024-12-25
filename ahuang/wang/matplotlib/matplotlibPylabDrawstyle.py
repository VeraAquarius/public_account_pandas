import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 使用plt.plot绘制正弦波，设置drawstyle为'steps-post'
plt.plot(x, y, drawstyle='steps-post', label='Sine Wave (steps-post)')

# 添加图例
plt.legend()

# 显示图形
plt.show()