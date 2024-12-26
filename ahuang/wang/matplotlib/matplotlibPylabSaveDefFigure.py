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

# 保存图形为PNG格式，设置DPI为300，裁剪边界，设置透明背景
plt.savefig('sine_wave_1.png', dpi=300, bbox_inches='tight', transparent=True)

# 保存图形为PDF格式，设置DPI为150
plt.savefig('sine_wave_1.pdf', dpi=150, bbox_inches='tight')

# 显示图形
plt.show()