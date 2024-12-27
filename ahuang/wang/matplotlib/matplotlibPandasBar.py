import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建一个包含随机数据的DataFrame
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 36]
})

# 设置Category列为索引
data.set_index('Category', inplace=True)

# 使用plot方法绘制柱状图
data.plot(kind='bar', title='Category Values', xlabel='Category', ylabel='Values', color='skyblue', grid=True)

# 显示图形
plt.show()