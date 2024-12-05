# 定义一个字符串
text = "Hello, welcome to the world of Python. Python is great!"

# 使用count方法统计子串"Python"的出现次数
python_count = text.count("Python")

# 显示统计结果
print("Count of 'Python':", python_count)

# 使用count方法统计子串"o"的出现次数
o_count = text.count("o")

# 显示统计结果
print("Count of 'o':", o_count)

# 使用count方法统计子串"world"的出现次数，限定在前10个字符内
world_count = text.count("world", 0, 10)

# 显示统计结果
print("Count of 'world' within first 10 characters:", world_count)