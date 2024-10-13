import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])

# 使用 rename 方法同时修改行索引和列索引
df_renamed = df.rename(index={'x': 'X', 'y': 'Y'}, columns={'A': 'Alpha', 'B': 'Beta'})

print("Original DataFrame:")
print(df)
print("\nDataFrame After Renaming Index and Columns:")
print(df_renamed)