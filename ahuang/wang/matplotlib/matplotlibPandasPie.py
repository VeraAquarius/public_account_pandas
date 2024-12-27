import pandas as pd
import matplotlib.pyplot as plt

# 创建数据
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [15, 30, 45, 10]}
df = pd.DataFrame(data)

# 绘制饼图
plt.figure(figsize=(8, 8))
df.plot(kind='pie', y='Values', autopct='%1.1f%%')
plt.title('Pie Chart of DataFrame')
plt.ylabel('')  # 隐藏y轴标签
plt.show()