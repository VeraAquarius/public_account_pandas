import pandas as pd

# 创建一个示例DataFrame
data = {
    'Region': ['East', 'West', 'East', 'West', 'East'],
    'Product': ['A', 'A', 'B', 'B', 'C'],
    'Sales': [200, 340, 250, 220, 300]
}
df = pd.DataFrame(data)
print(df)

# 使用Pandas groupby进行数据聚合
grouped_pd = (df.groupby('Region').agg({
    'Sales': ['sum', 'mean'],
    'Product': ['count']
}))

# 显示结果
print(grouped_pd)