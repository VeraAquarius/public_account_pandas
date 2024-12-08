import re

# 定义一个字符串
text = "Hello, my email is example@email.com and my phone number is 123-456-7890."

# 使用re.search查找电子邮件地址
email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# 显示电子邮件地址匹配结果
if email_match:
    print("Email found:", email_match.group())

# 使用re.findall查找所有电话号码
phone_numbers = re.findall(r'\b\d{3}-\d{3}-\d{4}\b', text)

# 显示电话号码匹配结果
print("Phone numbers found:", phone_numbers)

# 使用re.search查找包含特殊字符的URL
url_match = re.search(r'\bhttps?://[^\s/$.?#].[^\s]*\b', text)

# 显示URL匹配结果
if url_match:
    print("URL found:", url_match.group())

# 使用re.search查找包含转义字符的模式
escaped_char_match = re.search(r'\b\d+\b', text)

# 显示包含转义字符的模式匹配结果
if escaped_char_match:
    print("Digits found:", escaped_char_match.group())