import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 使用pylab模式绘图，并设置figsize参数
plt.figure(figsize=(10, 6))  # 设置图形尺寸为10x6英寸
plt.plot(x, y)
plt.title('Plot with figsize')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()