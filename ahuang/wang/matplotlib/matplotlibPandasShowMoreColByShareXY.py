import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
np.random.seed(0)
df1 = pd.DataFrame({
    'A': np.random.randn(10),
    'B': np.random.randn(10) + 1
})
df2 = pd.DataFrame({
    'A': np.random.randn(10) + 2,
    'B': np.random.randn(10) + 3
})

# 创建一个包含多个子图的图形，设置图形尺寸
fig, axs = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# 在第一个子图中绘制df1
df1.plot(kind='bar', ax=axs[0], title='DataFrame 1')

# 在第二个子图中绘制df2
df2.plot(kind='bar', ax=axs[1], title='DataFrame 2')
print(df1)
print(df2)
# 显示图形
plt.tight_layout()
plt.show()