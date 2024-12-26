import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# 创建图形和子图
fig, ax = plt.subplots(figsize=(8, 8))

# 定义多边形的顶点
vertices = np.array([[1, 1], [2, 4], [5, 2], [4, 1], [3, 0]])

# 创建多边形对象
polygon = patches.Polygon(vertices, closed=True, color='lightblue', edgecolor='blue', alpha=0.5)

# 将多边形添加到子图中
ax.add_patch(polygon)

# 设置坐标轴的范围
ax.set_xlim(0, 6)
ax.set_ylim(0, 5)

# 添加标题
ax.set_title('Polygon Example with patches.Polygon')

# 显示图形
plt.grid()
plt.show()