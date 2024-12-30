import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# 使用Pandas groupby进行数据分组并计算平均值
mean_values = df.groupby('Category')['Values'].mean()

# 显示结果
print(mean_values)