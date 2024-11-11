# 定义一个字符串
text = "Hello, welcome to the world of Python."

# 使用find方法查找子串"welcome"的位置
welcome_index = text.find("welcome")

# 显示查找结果
print("Index of 'welcome':", welcome_index)

# 使用find方法查找子串"Python"的位置
python_index = text.find("Python")

# 显示查找结果
print("Index of 'Python':", python_index)

# 使用find方法查找不存在的子串"Java"
java_index = text.find("Java")

# 显示查找结果
print("Index of 'Java':", java_index)