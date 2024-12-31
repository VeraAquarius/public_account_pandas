import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
print(df)
# 使用Pandas groupby进行数据分组，并使用as_index=False返回无索引的聚合数据
result = df.groupby('Category', as_index=False)['Values'].sum()

# 显示结果
print(result)

# 使用Pandas groupby进行数据分组，并使用as_index=True返回无索引的聚合数据
result = df.groupby('Category')['Values'].sum()

# 显示结果
print(result)