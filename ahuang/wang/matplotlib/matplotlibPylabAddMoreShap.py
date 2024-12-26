import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建图形和子图
fig, ax = plt.subplots(figsize=(8, 8))

# 创建一个矩形对象
rectangle = patches.Rectangle((1, 1), 2, 3, linewidth=2, edgecolor='blue', facecolor='lightblue')

# 将矩形添加到子图中
ax.add_patch(rectangle)

# 创建一个圆形对象
circle = patches.Circle((5, 5), radius=1, color='orange', alpha=0.5)

# 将圆形添加到子图中
ax.add_patch(circle)

# 创建一个多边形对象
polygon = patches.Polygon([[3, 5], [4, 7], [5, 5]], closed=True, color='green', alpha=0.6)

# 将多边形添加到子图中
ax.add_patch(polygon)

# 设置坐标轴的范围
ax.set_xlim(0, 7)
ax.set_ylim(0, 8)

# 添加标题
ax.set_title('Shapes Example with Matplotlib Patches')

# 显示图形
plt.grid()
plt.show()