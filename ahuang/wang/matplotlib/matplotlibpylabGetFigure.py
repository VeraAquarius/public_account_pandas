import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制图形
plt.plot(x, y)

# 使用plt.gcf()获取当前图形对象
current_figure = plt.gcf()

# 显示图形
plt.show()

# 获取当前图形的尺寸
print("Figure size:", current_figure.get_size_inches())