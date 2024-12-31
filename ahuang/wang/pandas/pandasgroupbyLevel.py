import pandas as pd

# 创建一个示例DataFrame，包含多级索引
tuples = [('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)]
index = pd.MultiIndex.from_tuples(tuples, names=['Category', 'Subcategory'])
data = {'Values': [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data, index=index)
print(df)
# 使用Pandas groupby进行数据分组，通过level参数指定索引级别
grouped_level = df.groupby(level='Category').sum()

# 显示结果
print(grouped_level)