import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
np.random.seed(0)
df = pd.DataFrame({
    'Data1': np.random.normal(0, 1, 100),
    'Data2': np.random.normal(1, 2, 100)
})

# 绘制箱型图
plt.figure(figsize=(10, 6))
df.plot(kind='box', vert=True, grid=True)
plt.title('Boxplot of DataFrame Columns')
plt.show()