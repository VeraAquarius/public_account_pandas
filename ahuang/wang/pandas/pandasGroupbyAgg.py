import pandas as pd
import numpy as np

# 创建一个示例DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 20, 30, 40, 50, 60],
    'More_Values': [100, 200, 300, 400, 500, 600]
}
df = pd.DataFrame(data)
print(df)
# 定义一个自定义聚合函数，计算两列的和与均值
def custom_agg(x):
    return pd.Series({
        'sum_values': x['Values'].sum(),
        'mean_more_values': x['More_Values'].mean()
    })

# 使用Pandas groupby进行数据分组，并使用agg应用自定义聚合函数
result = df.groupby('Category').apply(custom_agg)

# 显示结果
print(result)