import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制正弦波
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')

# 保存图形为PNG格式
plt.savefig('sine_wave.png', dpi=300, bbox_inches='tight')

# 保存图形为PDF格式
plt.savefig('sine_wave.pdf')

# 显示图形
plt.show()