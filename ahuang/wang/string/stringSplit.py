# 定义一个字符串
text = "hello world, this is a test string"

# 使用split方法拆分字符串，默认以空格为分隔符
words = text.split()

# 显示拆分后的结果
print("Words:", words)

# 使用split方法拆分字符串，指定逗号为分隔符
comma_separated = text.split(',')

# 显示拆分后的结果
print("Comma Separated:", comma_separated)

# 使用split方法拆分字符串，指定空格为分隔符，并限制最大拆分次数
space_separated_limited = text.split(' ', maxsplit=2)

# 显示拆分后的结果
print("Space Separated Limited:", space_separated_limited)