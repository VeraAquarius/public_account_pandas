# 定义一个字符串，包含首尾的空格和特殊字符
text = "   hello world!   \n"

# 使用strip方法去除首尾的空白字符
stripped_text = text.strip()

# 显示去除空白字符后的结果
print("Stripped Text:", stripped_text)

# 定义一个字符串，包含首尾的特殊字符
text_with_special_chars = "---hello world!!!---"

# 使用strip方法去除首尾的特殊字符
stripped_special_chars = text_with_special_chars.strip("-!")

# 显示去除特殊字符后的结果
print("Stripped Special Characters:", stripped_special_chars)