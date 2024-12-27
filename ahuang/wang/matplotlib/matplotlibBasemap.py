import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 创建一个新的图形
plt.figure(figsize=(8, 6))

# 创建Basemap实例，绘制全球地图
m = Basemap(projection='cyl', resolution='c')

# 绘制海岸线
m.drawcoastlines(color='black')

# 绘制国家边界（可选）
m.drawcountries(color='black')

# 填充大陆颜色（可选）
m.fillcontinents(color='coral', lake_color='aqua')


# 显示图形
plt.show()