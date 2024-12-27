import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建一个包含随机数据的DataFrame
data = pd.DataFrame({
    'A': np.random.randn(100).cumsum(),
    'B': np.random.randn(100).cumsum(),
    'C': np.random.randn(100).cumsum()
})

# 使用plot方法绘制线图
data.plot(kind='line', title='Random Walks', xlabel='Index', ylabel='Cumulative Sum', grid=True)

# 显示图形
plt.show()