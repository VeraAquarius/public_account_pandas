import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# 创建一个图形和子图
fig, ax = plt.subplots(figsize=(8, 8))

# 创建一个圆形对象，圆心在(0, 0)，半径为1
circle = patches.Circle((0, 0), radius=1, color='blue', alpha=0.5)

# 将圆形添加到子图中
ax.add_patch(circle)

# 设置坐标轴的范围
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# 设置坐标轴的比例相等
ax.set_aspect('equal', adjustable='box')

# 添加标题
ax.set_title('Circle Example with patches.Circle')

# 显示图形
plt.grid()
plt.show()