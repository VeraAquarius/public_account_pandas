import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 创建三个DataFrame，分别包含不同的数据
df1 = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100))
})

df2 = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.cos(np.linspace(0, 10, 100))
})

df3 = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.tan(np.linspace(0, 10, 100))
})

# 创建一个包含3个子图的图形，设置图形尺寸
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# 在第一个子图中绘制正弦波
axs[0].plot(df1['x'], df1['y'], color='red')
axs[0].set_title('Sine Wave')
axs[0].set_xlabel('X-axis')
axs[0].set_ylabel('Y-axis')

# 在第二个子图中绘制余弦波
axs[1].plot(df2['x'], df2['y'], color='blue')
axs[1].set_title('Cosine Wave')
axs[1].set_xlabel('X-axis')
axs[1].set_ylabel('Y-axis')

# 在第三个子图中绘制正切波
axs[2].plot(df3['x'], df3['y'], color='green')
axs[2].set_title('Tangent Wave')
axs[2].set_xlabel('X-axis')
axs[2].set_ylabel('Y-axis')

# 自动调整子图间距
plt.tight_layout()

# 显示图形
plt.show()