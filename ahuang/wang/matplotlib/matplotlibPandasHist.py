import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
np.random.seed(0)
df = pd.DataFrame({
    'Data1': np.random.randn(1000),
    'Data2': np.random.randn(1000) + 1
})

# 绘制直方图
plt.figure(figsize=(12, 6))
df.plot(kind='hist', bins=30, alpha=0.5, layout=(1, 2))
plt.suptitle('Histograms of DataFrame Columns')
plt.show()