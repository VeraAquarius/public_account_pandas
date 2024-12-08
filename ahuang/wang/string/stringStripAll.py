# 定义一个字符串，包含首尾的空格和特殊字符
text = "   Hello, world!   \n"

# 使用strip方法去除首尾的空白字符
stripped_text = text.strip()

# 显示去除空白字符后的结果
print("Stripped Text:", stripped_text)

# 使用rstrip方法去除右侧的空白字符和换行符
stripped_right = text.rstrip()

# 显示去除右侧空白字符和换行符后的结果
print("Stripped Right:", stripped_right)

# 使用lstrip方法去除左侧的空白字符
stripped_left = text.lstrip()

# 显示去除左侧空白字符后的结果
print("Stripped Left:", stripped_left)

# 定义一个字符串，包含首尾的特殊字符
text_with_special_chars = "---hello world!!!---"

# 使用strip方法去除首尾的特殊字符
stripped_special_chars = text_with_special_chars.strip("-!")

# 显示去除特殊字符后的结果
print("Stripped Special Characters:", stripped_special_chars)