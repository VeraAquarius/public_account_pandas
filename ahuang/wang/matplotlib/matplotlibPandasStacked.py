import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
np.random.seed(0)
df = pd.DataFrame({
    'Category A': np.random.randint(10, 50, size=5),
    'Category B': np.random.randint(10, 50, size=5),
    'Category C': np.random.randint(10, 50, size=5)
}, index=['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'])

# 绘制堆叠柱状图
plt.figure(figsize=(10, 6))
df.plot(kind='bar', stacked=True)
plt.title('Stacked Bar Chart of DataFrame')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.show()