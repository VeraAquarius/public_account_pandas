import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])

# 使用 lambda 函数对行索引和列名进行重命名
df_renamed = df.rename(index=lambda x: x.upper(), columns=lambda x: x.upper())

print("Original DataFrame:")
print(df)
print("\nDataFrame After Renaming Index and Columns:")
print(df_renamed)