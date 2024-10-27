import pandas as pd
import numpy as np

# 创建一个包含异常值的DataFrame
df = pd.DataFrame({
    "Data": np.random.randint(0, 5, 10)
})


# 检测并过滤绝对值不超过3的数据
threshold = 3
filtered_df = df[(df.Data.abs() <= threshold)]

# 显示原始数据和过滤后的数据
print("Original Data Sample:")
print(df.head())
print("\nFiltered Data Sample:")
print(filtered_df.head())

# 统计过滤前后的数据量
print(f"\nOriginal Data Count: {df.shape[0]}")
print(f"Filtered Data Count: {filtered_df.shape[0]}")