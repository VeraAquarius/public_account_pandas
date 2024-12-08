# 定义一个字符串
text = "Hello, world!"

# 使用startswith方法检查字符串是否以"Hello"开始
starts_with_hello = text.startswith("Hello")

# 显示检查结果
print("Does the text start with 'Hello'?", starts_with_hello)

# 使用endswith方法检查字符串是否以"!"结束
ends_with_exclamation = text.endswith("!")

# 显示检查结果
print("Does the text end with '!'?", ends_with_exclamation)

# 使用startswith方法检查字符串是否以"world"开始，从索引7开始检查
starts_with_world = text.startswith("world", 7)

# 显示检查结果
print("Does the text start with 'world' after index 7?", starts_with_world)

# 使用endswith方法检查字符串是否以多个可能的结束符结束
ends_with_punctuation = text.endswith(("!", "?"))

# 显示检查结果
print("Does the text end with '!' or '?'?", ends_with_punctuation)