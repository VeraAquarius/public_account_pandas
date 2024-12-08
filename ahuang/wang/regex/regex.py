import re

# 定义一个字符串
text = "Hello, world! Welcome to the world of Python."

# 使用search方法查找第一个数字
numbers = re.search(r'\d+', text)
if numbers:
    print("Found number:", numbers.group())

# 使用match方法检查字符串是否以'Hello'开头
match_result = re.match(r'^Hello', text)
if match_result:
    print("Match found at the beginning:", match_result.group())

# 使用split方法以空白字符分割字符串
words = re.split(r'\s+', text)
print("Split words:", words)