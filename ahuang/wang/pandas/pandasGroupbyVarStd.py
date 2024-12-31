import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)
print(df)
# 使用Pandas groupby进行数据分组，并使用var和std计算每个分组的方差和标准差
var_result = df.groupby('Category')['Values'].var(ddof=1)  # 样本方差
std_result = df.groupby('Category')['Values'].std(ddof=1)  # 样本标准差

# 显示结果
print("方差结果：\n", var_result)
print("\n标准差结果：\n", std_result)