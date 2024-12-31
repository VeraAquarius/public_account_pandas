import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# 定义一个自定义转换函数，计算每个分组的数值相对于该组均值的比例
def relative_to_mean(x):
    return x / x.mean()

# 使用Pandas groupby进行数据分组，并使用transform应用自定义转换函数
transformed_df = df.groupby('Category')['Values'].transform(relative_to_mean)

# 显示结果
print(transformed_df)