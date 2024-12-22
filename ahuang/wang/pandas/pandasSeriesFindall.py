import pandas as pd

# 创建一个包含电话号码和电子邮件的Series
data = pd.Series([
    "Contact: 123-456-7890 or email@example.com",
    "Support: 987-654-3210, email: support@example.net",
    "Sales: 555-1234, email: sales@example.io"
])

# 使用str.findall和正则表达式提取所有的电话号码和电子邮件
phone_emails = data.str.findall(r'\b\d{3}-\d{3}-\d{4}\b|\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# 显示提取结果
print("Extracted Phone Numbers and Emails:")
print(phone_emails)