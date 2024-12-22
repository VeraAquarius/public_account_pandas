import pandas as pd

# 创建一个包含字符串列表的DataFrame
df = pd.DataFrame({
    'words': [['hello', 'world'], ['pandas', 'is', 'great'], ['data', 'science', 'rocks']]
})

# 使用str.join将每个列表中的字符串元素连接成一个字符串
df['sentence'] = df['words'].apply(' '.join)

# 显示连接后的结果
print("Joined Sentences:\n", df['sentence'])