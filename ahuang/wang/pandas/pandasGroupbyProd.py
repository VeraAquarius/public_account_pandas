import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [2, 3, 4, 5, 6, 7]
}
df = pd.DataFrame(data)
print(df)
# 使用Pandas groupby进行数据分组，并使用prod计算每个分组的乘积
prod_result = df.groupby('Category')['Values'].prod()

# 显示结果
print(prod_result)