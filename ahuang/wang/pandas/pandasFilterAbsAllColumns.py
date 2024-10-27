import pandas as pd
import numpy as np

# 创建一个包含异常值的DataFrame
df = pd.DataFrame({
    'A': np.random.randint(0, 5, 10),
    'B': np.random.randint(0, 6, 10)
})

# 检测并过滤至少在一个列中绝对值超过3的行
threshold = 3
filtered_df = df[(df.abs().gt(threshold)).any(axis=1)]

# 显示过滤后的数据
print("Filtered Data (Rows with Absolute Values > 3):")
print(filtered_df)

# 统计过滤后的数据量
print(f"\nFiltered Data Count: {filtered_df.shape[0]}")