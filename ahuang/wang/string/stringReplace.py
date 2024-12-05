# 定义一个字符串
text = "Hello, world! Welcome to the world of Python."

# 使用replace方法替换子串"world"为"earth"
replaced_text = text.replace("world", "earth")

# 显示替换后的结果
print("Replaced Text:", replaced_text)

# 使用replace方法替换子串"Python"为"Java"，并且只替换第一次出现的子串
replaced_text_once = text.replace("Python", "Java", 1)

# 显示替换后的结果
print("Replaced Text (once):", replaced_text_once)

# 使用replace方法替换所有出现的子串"o"为"0"
replaced_text_all = text.replace("o", "0")

# 显示替换后的结果
print("Replaced Text (all 'o'):", replaced_text_all)