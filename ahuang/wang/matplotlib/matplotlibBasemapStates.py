import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 创建一个新的图形
plt.figure(figsize=(10, 8))

# 创建Basemap实例，绘制美国地图
m = Basemap(llcrnrlon=-125, llcrnrlat=20, urcrnrlon=-60, urcrnrlat=50,
            projection='lcc', lat_1=33, lat_2=45, lon_0=-95)

# 绘制海岸线
m.drawcoastlines()

# 绘制州界
m.drawstates(color='black')

# 填充大陆颜色（可选）
m.fillcontinents(color='coral', lake_color='aqua')

# 显示图形
plt.title('Map of the United States with State Boundaries')
plt.show()