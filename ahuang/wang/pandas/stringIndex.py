# 定义一个字符串
text = "Hello, welcome to the world of Python."

# 使用index方法查找子串"welcome"的位置
welcome_index = text.index("welcome")

# 显示查找结果
print("Index of 'welcome':", welcome_index)

# 使用index方法查找子串"Python"的位置
python_index = text.index("Python")

# 显示查找结果
print("Index of 'Python':", python_index)

# 尝试使用index方法查找不存在的子串"Java"
try:
    java_index = text.index("Java")
    print("Index of 'Java':", java_index)
except ValueError:
    print("'Java' is not found in the text.")