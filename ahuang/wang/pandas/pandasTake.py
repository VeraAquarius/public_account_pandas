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

# 生成一个随机索引数组
sampler = np.random.permutation(df.index)

# 使用df.take(sampler)进行随机重排序
shuffled_df = df.take(sampler)

# 显示随机重排序后的数据
print("\nDataFrame after Random Shuffling:")
print(shuffled_df)

# 使用df.take(sampler)进行随机采样
sample_size = 5
sampler = np.random.choice(df.index, size=sample_size, replace=False)
sampled_df = df.take(sampler)

# 显示随机采样后的数据
print("\nDataFrame after Random Sampling:")
print(sampled_df)