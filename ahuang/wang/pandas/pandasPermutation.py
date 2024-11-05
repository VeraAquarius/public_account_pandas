import pandas as pd
import numpy as np

# 创建一个DataFrame
df = pd.DataFrame({
    'A': range(1, 11),
    'B': range(11, 21)
})

# 显示原始数据
print("Original DataFrame:")
print(df)

# 使用numpy.random.permutation进行随机重排序
permuted_df = df.iloc[np.random.permutation(df.index)]

# 显示随机重排序后的数据
print("\nDataFrame after Permutation:")
print(permuted_df)

# 使用sample方法随机采样50%的数据
sampled_df = df.sample(frac=0.5, random_state=1)

# 显示随机采样后的数据
print("\nDataFrame after Random Sampling:")
print(sampled_df)