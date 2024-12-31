import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# 使用Pandas groupby进行数据分组，并使用apply和transform

# apply函数：返回每个分组的最大值和最小值
result_apply = df.groupby('Category').apply(lambda x: x[['Values']].agg(['max', 'min']))

# transform函数：返回每个分组的数值相对于该组均值的比例
result_transform = df.groupby('Category')['Values'].transform(lambda x: x / x.mean())

# 显示结果
print("apply结果：\n", result_apply)
print("\ntransform结果：\n", result_transform)