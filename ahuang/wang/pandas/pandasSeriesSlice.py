import pandas as pd

# 创建一个包含文本数据的Series
data = pd.Series([
    "Hello World",
    "Pandas is great",
    "Data analysis with Pandas",
    "Python for data science"
])

# 使用str.slice提取每个字符串的前5个字符
first_five = data.str.slice(0, 5)

# 显示提取结果
print("First Five Characters:", first_five)

# 使用str.slice提取每个字符串的最后3个字符
last_three = data.str.slice(-3, None)

# 显示提取结果
print("Last Three Characters:", last_three)