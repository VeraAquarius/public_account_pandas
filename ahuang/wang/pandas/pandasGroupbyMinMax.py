import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# 使用Pandas groupby进行数据分组，并使用min和max计算每个分组的最小值和最大值
min_result = df.groupby('Category')['Values'].min()
max_result = df.groupby('Category')['Values'].max()
print(df)
# 显示结果
print("最小值结果：\n", min_result)
print("\n最大值结果：\n", max_result)