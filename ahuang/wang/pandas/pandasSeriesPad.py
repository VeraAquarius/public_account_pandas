import pandas as pd

# 创建一个包含文本数据的Series
data = pd.Series([
    "apple",
    "banana",
    "cherry",
    "date"
])

# 使用str.pad在右侧填充空格，使每个字符串长度达到8
padded_right = data.str.pad(width=8, side='right', fillchar=' ')

# 显示右侧填充结果
print("Padded Right:", padded_right)

# 使用str.pad在左侧和右侧填充星号，使每个字符串长度达到8
padded_both = data.str.pad(width=8, side='both', fillchar='*')

# 显示两侧填充结果
print("Padded Both Sides:", padded_both)