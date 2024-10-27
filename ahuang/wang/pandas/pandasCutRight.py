import pandas as pd
import numpy as np

# 创建一个包含年龄数据的DataFrame
df = pd.DataFrame({
    "Age": np.random.randint(18, 100, 10)
})

# 定义年龄的区间边界
bins = [18, 30, 50, 70, 100]

# 使用pandas的cut函数进行面元划分，设置right=False实现左闭右开的区间
df['Age_Bin_OpenRight'] = pd.cut(df['Age'], bins=bins, labels=['Youth', 'Adult', 'Middle-Aged', 'Senior'], right=True)
# 设置right=False实现左闭右开的区间
df['Age_Bin_ClosedRight'] = pd.cut(df['Age'], bins=bins, labels=['Youth', 'Adult', 'Middle-Aged', 'Senior'], right=False)

# 包含最低端点
df['Age_Bin_IncludeLowest'] = pd.cut(df['Age'], bins=bins, labels=['Youth', 'Adult', 'Middle-Aged', 'Senior'], right=True, include_lowest=True)

# 显示DataFrame，查看面元划分结果
print("DataFrame with Age Bins:")
print(df)
