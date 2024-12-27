import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建一个包含随机数据的Series
data = pd.Series(np.random.randn(100).cumsum(), index=pd.date_range('2023-01-01', periods=100))

# 使用plot方法绘制线图
data.plot(kind='line', title='Random Walk', xlabel='Date', ylabel='Cumulative Sum', grid=True)

# 显示图形
plt.show()