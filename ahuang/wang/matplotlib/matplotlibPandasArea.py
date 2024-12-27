import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 创建数据
np.random.seed(0)
index = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)), index=index, columns=list('ABCD'))

# 绘制面积图
plt.figure(figsize=(12, 6))
df.plot(kind='area', stacked=False)
plt.title('Area Chart of DataFrame')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()