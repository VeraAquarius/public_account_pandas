import re

# 定义一个字符串
text = "apple,banana;orange|grape"

# 编译一个正则表达式对象，模式为逗号、分号或竖线
regex = re.compile(r'[,;|]')

# 使用编译的正则表达式对象拆分字符串
fruits = regex.split(text)

# 显示拆分后的结果
print("Fruits:", fruits)

# 定义另一个字符串，使用相同的正则表达式对象拆分
another_text = "Hello, world! Welcome to the world of Python."
spaces = re.compile(r'\s+')

# 使用编译的正则表达式对象拆分字符串
words = spaces.split(another_text)

# 显示拆分后的结果
print("Words:", words)