import re

# 定义一个字符串
text = "Hello, my email is example@email.com and my phone number is 123-456-7890."

# 使用re.search查找电子邮件地址
email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

# 显示电子邮件地址匹配结果
if email_match:
    print("Email found:", email_match.group())
else:
    print("No email found.")

# 使用re.search查找电话号码
phone_match = re.search(r'\b\d{3}-\d{3}-\d{4}\b', text)

# 显示电话号码匹配结果
if phone_match:
    print("Phone number found:", phone_match.group())
else:
    print("No phone number found.")