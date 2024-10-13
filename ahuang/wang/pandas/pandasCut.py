import pandas as pd
import numpy as np

# 创建示例数据
data = np.random.rand(100)
bins = [0, 0.25, 0.5, 0.75, 1]

# 使用 cut 函数进行离散化
discretized_data = pd.cut(data, bins)

# 使用 qcut 函数进行面元化
quantile_data = pd.qcut(data, 4)

print("Original Data:")
print(data[:10])
print("\nDiscretized Data:")
print(discretized_data[:10])
print("\nQuantile Data:")
print(quantile_data[:10])