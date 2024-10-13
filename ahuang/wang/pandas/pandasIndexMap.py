import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}, index=['x', 'y', 'z'])

# 使用 index 方法结合函数对行索引进行重命名
df_renamed = df.index.map(lambda x: x.upper())

print("Original Data:")
print(df)
print("\nData After Renaming Index:")
print(df_renamed)
