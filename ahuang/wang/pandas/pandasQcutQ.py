import pandas as pd
import numpy as np

# 创建一个包含年龄数据的DataFrame
df = pd.DataFrame({
    "Age": np.random.randint(18, 100, 100)
})

# 设置自定义的分位数
quantiles = [0.05, 0.3, 0.6, 0.95]

# 使用pandas的qcut函数进行等频分箱，按照自定义的分位数划分
df['Age_Qcut'] = pd.qcut(df['Age'], q=quantiles, labels=['Lowest', 'First Quartile', 'Highest'])

# 显示DataFrame，查看等频分箱结果
print("DataFrame with Custom Quantile Bins:")
print(df[['Age', 'Age_Qcut']].head())

# 显示每个区间的样本数量
print("\nSample Counts in Each Bin:")
print(df['Age_Qcut'].value_counts())