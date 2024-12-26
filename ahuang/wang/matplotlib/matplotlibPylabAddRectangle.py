import matplotlib.pyplot as plt

# 创建图形和子图
fig, ax = plt.subplots()

# 绘制矩形，表示x轴上的[2, 4]和y轴上的[1, 3]的区域
ax.add_patch(plt.Rectangle((2, 1), 2, 2, fill=False, edgecolor='r', facecolor='none'))

# 设置坐标轴范围
ax.set_xlim(0, 6)
ax.set_ylim(0, 5)

# 显示图形
plt.show()