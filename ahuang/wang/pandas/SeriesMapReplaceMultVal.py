import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    'A': ['a', 'b', 'c', 'd'],
    'B': ['a', 'f', 'g', 'h']
})

# 使用 replace 方法一次性替换多个列的相同值
replaced_df = df.replace(['a','d'], 'A')

print("Original Data:")
print(df)
print("\nData After Replacement:")
print(replaced_df)