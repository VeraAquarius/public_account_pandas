import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子，确保结果可复现
np.random.seed(0)

# 生成正态分布数据
data = np.random.normal(loc=0, scale=1, size=1000)

# 创建一个Pandas Series
normal_distribution = pd.Series(data)

# 显示数据的前几行
print("Normal Distribution Data:")
print(normal_distribution.head())

# 绘制直方图，查看数据分布
plt.hist(normal_distribution, bins=30, density=True, alpha=0.6, color='g')
plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()