import pandas as pd

# 创建示例数据
data = pd.Series(['a', 'b', 'c', 'd'])

# 使用 replace 方法替换数据
replaced_data = data.replace('a', 'A')

print("Original Data:")
print(data)
print("\nData After Replacement:")
print(replaced_data)