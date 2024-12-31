import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'A', None],
    'Values': [10, 20, 30, 40, 50, 60, 70, 80]
}
df = pd.DataFrame(data)
print(df)
# 使用Pandas groupby进行数据分组，并使用count统计每个分组的数据项数
count_result = df.groupby('Category').count()

# 显示结果
print(count_result)