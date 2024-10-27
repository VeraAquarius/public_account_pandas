import pandas as pd
import numpy as np

# 创建一个包含年龄数据的DataFrame
df = pd.DataFrame({
    "Age": np.random.randint(18, 100, 10)
})

# 使用pandas的cut函数进行面元划分，bins指定区间的数量
# precision参数控制区间边界的精度
df['Age_Bin'] = pd.cut(df['Age'], bins=4, precision=1)

# 显示DataFrame，查看面元划分结果
print("DataFrame with Age Bins:")
print(df)

# 显示每个区间的边界
print("\nInterval Boundaries:")
print(df['Age_Bin'].cat.categories)