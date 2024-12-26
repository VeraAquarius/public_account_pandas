import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体参数
plt.rc('font', family='serif', size=14, weight='bold', style='italic')

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制正弦波
plt.plot(x, y)
plt.title('Sine Wave with Custom Font', fontsize=16)
plt.xlabel('X-axis', fontsize=14)
plt.ylabel('Y-axis', fontsize=14)
plt.legend(['Sine Wave'], fontsize=12)

# 显示图形
plt.show()