import re

# 定义一个字符串
text = "Hello, world!"

# 使用re.match检查字符串是否以"Hello"开头
match_result = re.match(r'^Hello', text)

# 显示匹配结果
if match_result:
    print("Match found at the beginning:", match_result.group())
else:
    print("No match found at the beginning.")

# 定义一个包含电子邮件的字符串
email_text = "contact@example.com is the email address."

# 使用re.match提取字符串开头的电子邮件地址
email_match = re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', email_text)

# 显示电子邮件匹配结果
if email_match:
    print("Email address found:", email_match.group())
else:
    print("No email address found at the beginning.")