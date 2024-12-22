import pandas as pd

# 创建一个包含文本数据的Series
data = pd.Series(['apple', 'banana', 'cherry'])

# 使用str.repeat将每个字符串重复3次
repeated_data = data.str.repeat(3)

# 显示重复后的结果
print("Repeated Text:", repeated_data)