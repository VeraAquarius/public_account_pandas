import re

# 定义一个包含多种分隔符的字符串
text = "apple,banana;orange|grape"

# 使用re.split拆分字符串，模式为逗号或分号或竖线
fruits = re.split(r'[,;|]', text)

# 显示拆分后的结果
print("Fruits:", fruits)

# 定义一个包含日期和时间的字符串
datetime_str = "2024-05-19 14:30:00"

# 使用re.split拆分日期和时间
date_time = re.split(r'\s+', datetime_str)

# 显示拆分后的结果
print("Date and Time:", date_time)

# 定义一个包含HTML标签的字符串
html_str = "<html><body><h1>Hello, World!</h1></body></html>"

# 使用re.split拆分HTML标签，模式为"<.*?>"
html_parts = re.split(r'<.*?>', html_str)

# 显示拆分后的结果
print("HTML Parts:", html_parts)