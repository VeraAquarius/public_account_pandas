import pandas as pd
import numpy as np

# 创建一个DataFrame对象
df = pd.DataFrame({
    "Age": np.random.randint(18, 100, 10)
})

# 定义年龄的区间边界
bins = [18, 30, 50, 70, 100]
# 为每个区间自定义标签
labels = ['Youth', 'Adult', 'Middle-Aged', 'Senior']

# 使用pandas的cut函数进行面元划分
df['Age_Bin'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)

print(df)