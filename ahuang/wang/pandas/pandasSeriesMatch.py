import pandas as pd

# 创建一个包含电子邮件的Series
data = pd.Series([
    "email1@example.com",
    "user2@domain.org",
    "invalid-email",
    "name4@site.co.uk"
])

# 使用str.match和正则表达式匹配以字母开头的电子邮件
email_pattern = r'^[a-zA-Z][a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email_matches = data.str.match(email_pattern)

# 显示匹配结果
print("Email Matches:", email_matches)

# 使用str.match和正则表达式匹配以特定数字开头的字符串
number_pattern = r'^\d{3}-'
number_matches = data.str.match(number_pattern)

# 显示匹配结果
print("Number Matches:", number_matches)