import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建一个包含日期索引的Series
index = pd.date_range('2023-01-01', periods=100)
data = pd.Series(np.random.randn(100), index=index)

# 使用plot方法绘制线图，使用索引作为横轴
data.plot(kind='line', use_index=True, title='Random Walk with Date Index', ylabel='Values')

# 显示图形
plt.show()