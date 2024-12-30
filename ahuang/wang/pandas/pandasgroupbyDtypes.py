import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Integer Values': [10, 20, 30, 40, 50, 60],
    'Float Values': [1.1, 2.2, 3.3, 4.4, 5.5, 6.6],
    'String Values': ['x', 'y', 'x', 'y', 'x', 'y']
}
df = pd.DataFrame(data)

# 使用Pandas groupby进行数据分组
grouped = df.groupby('Category')

# 查看分组后各DataFrame的数据类型
dtypes_by_group = grouped.dtypes

# 显示结果
print(dtypes_by_group)