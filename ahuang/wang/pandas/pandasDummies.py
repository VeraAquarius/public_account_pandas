import pandas as pd
import numpy as np

# 创建一个包含分类数据的DataFrame
df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']
})

# 使用Pandas的get_dummies函数创建哑变量矩阵
dummy_matrix = pd.get_dummies(df['Color'], prefix='Color')

# 显示哑变量矩阵
print("Dummy Matrix:")
print(dummy_matrix)

# 创建指标矩阵，这里我们选择'Blue'作为参考类别
indicator_matrix = pd.get_dummies(df['Color'], prefix='Color', drop_first=True)

# 显示指标矩阵
print("\nIndicator Matrix:")
print(indicator_matrix)