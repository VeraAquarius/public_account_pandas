import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
np.random.seed(0)
data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Values': np.random.randint(10, 50, size=5)}
df = pd.DataFrame(data)

# 绘制横向条形图
plt.figure(figsize=(10, 6))
df.plot(kind='barh', x='Category', y='Values', legend=False)
plt.title('Horizontal Bar Chart with Pandas DataFrame')
plt.xlabel('Values')
plt.ylabel('Category')
plt.show()