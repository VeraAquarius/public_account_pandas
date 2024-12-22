import pandas as pd

# 创建一个包含大小写混合文本的Series
data = pd.Series([
    "Hello World",
    "PYTHON is great",
    "pandas Is Fun"
])

# 使用str.lower将所有字符串转换为小写
lower_case = data.str.lower()

# 显示小写转换结果
print("Lower Case Conversion:", lower_case)

# 使用str.upper将所有字符串转换为大写
upper_case = data.str.upper()

# 显示大写转换结果
print("Upper Case Conversion:", upper_case)