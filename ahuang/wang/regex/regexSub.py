import re

# 定义一个字符串
text = "Hello, world! Welcome to the world of Python. World domination is next."

# 使用re.sub替换所有出现的"world"为"earth"
replaced_text = re.sub(r'world', 'earth', text)

# 显示替换后的结果
print("Replaced Text:", replaced_text)

# 使用re.subn替换所有出现的"Python"为"Java"，并获取替换次数
replaced_text, num_replacements = re.subn(r'Python', 'Java', text)

# 显示替换后的结果和替换次数
print("Replaced Text:", replaced_text)
print("Number of Replacements:", num_replacements)

# 限制替换次数为2
replaced_text, num_replacements = re.subn(r'\s', '-', text, count=2)

# 显示替换后的结果和替换次数
print("Replaced Text with Limited Count:", replaced_text)
print("Number of Replacements:", num_replacements)