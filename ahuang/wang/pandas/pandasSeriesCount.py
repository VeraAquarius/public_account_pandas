import pandas as pd

# 创建一个包含文本数据的Series
data = pd.Series([
    "apple, banana, cherry",
    "dog, cat, dog",
    "python, python, python",
    "hello, world, hello"
])

# 使用str.count统计每个字符串中逗号","出现的次数
comma_counts = data.str.count(',')

# 显示逗号出现次数的结果
print("Comma Counts:", comma_counts)

# 使用str.count统计每个字符串中"python"出现的次数
python_counts = data.str.count('python')

# 显示"python"出现次数的结果
print("Python Counts:", python_counts)