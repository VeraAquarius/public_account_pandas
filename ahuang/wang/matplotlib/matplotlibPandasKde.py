import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
np.random.seed(0)
df = pd.DataFrame({
    'Data1': np.random.normal(0, 1, 1000),
    'Data2': np.random.normal(1, 2, 1000)
})
print(df)

# 绘制核密度估计图
plt.figure(figsize=(12, 6))
df.plot(kind='kde', bw_method='silverman')
plt.title('Kernel Density Estimation of DataFrame Columns')
plt.show()