import pandas as pd
import numpy as np

# 创建一个包含年龄数据的DataFrame
df = pd.DataFrame({
    "Age": np.random.randint(18, 100, 100)
})

# 使用pandas的qcut函数进行等频分箱，分成4个区间
df['Age_Qcut'] = pd.qcut(df['Age'], q=4, labels=['Youth', 'Adult', 'Middle-Aged', 'Senior'])

# 显示DataFrame，查看等频分箱结果
print("DataFrame with Age Qcut:")
print(df[['Age', 'Age_Qcut']].head())

# 显示每个区间的样本数量
print("\nSample Counts in Each Bin:")
print(df['Age_Qcut'].value_counts())
