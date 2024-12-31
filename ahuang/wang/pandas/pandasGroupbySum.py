import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
print(df)
# 使用Pandas groupby进行数据分组，并使用sum计算每个分组的总和
sum_result = df.groupby('Category')['Values'].sum()

# 显示结果
print(sum_result)