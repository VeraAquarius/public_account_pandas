import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建一个包含指数增长数据的Series
x = np.linspace(1, 10, 100)
y = np.exp(x)  # 指数函数

# 创建一个Pandas Series
data = pd.Series(y)

# 使用plot方法绘制对数y轴的图形
data.plot(kind='line', logy=True, title='Exponential Growth with Logarithmic Y-axis', xlabel='X-axis', ylabel='Y-axis (log scale)')

# 显示图形
plt.show()