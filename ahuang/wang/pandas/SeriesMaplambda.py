import pandas as pd

# 创建示例数据
data = pd.Series(['a', 'b', 'c', 'd'])

# 使用 map 方法结合 lambda 函数进行数据转换
converted_data = data.map(lambda x: x.upper())

print("Original Data:")
print(data)
print("\nData After Conversion:")
print(converted_data)



