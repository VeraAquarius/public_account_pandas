import pandas as pd

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Values': [10, 20, 30, 40, 50, 60],
    'More_Values': [100, 200, 300, 400, 500, 600]
}
df = pd.DataFrame(data)

# 定义聚合字典，对不同列应用不同的聚合函数
agg_dict = {
    'Values': ['sum', 'mean', 'max'],
    'More_Values': ['sum', 'mean', 'min']
}

agg_all_dict = ['sum', 'mean', 'max']
# 使用Pandas groupby进行数据分组，并使用agg应用聚合函数于所有列
result = df.groupby('Category').agg(agg_dict)

# 显示结果
print(result)

# 使用Pandas groupby进行数据分组，并使用agg应用聚合函数于所有列
result = df.groupby(['Category','Subcategory']).agg(agg_all_dict)

# 显示结果
print(result)