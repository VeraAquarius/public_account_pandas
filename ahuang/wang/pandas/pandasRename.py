import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])

# 使用 rename 方法修改行索引
df_renamed = df.rename(index={'x': 'X', 'y': 'Y'})

print("Original DataFrame:")
print(df)
print("\nDataFrame After Renaming Index:")
print(df_renamed)
