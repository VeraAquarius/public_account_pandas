import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, 40, 50, 60],
    'Dates': pd.date_range('20230101', periods=6)
}
df = pd.DataFrame(data)
print(df)
# 使用Pandas groupby进行数据分组，并使用first和last计算每个分组的首尾值
first_result = df.groupby('Category')['Values'].first()
last_result = df.groupby('Category')['Values'].last()

# 显示结果
print("首值结果：\n", first_result)
print("\n尾值结果：\n", last_result)