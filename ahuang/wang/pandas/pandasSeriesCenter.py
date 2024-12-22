import pandas as pd

# 创建一个包含文本数据的Series
data = pd.Series([
    "apple",
    "banana",
    "cherry",
    "date"
])

# 使用str.center在两侧填充'*'，使每个字符串长度达到8
centered_data = data.str.center(width=8, fillchar='*')

# 显示居中对齐的结果
print("Centered Text:\n", centered_data)