import pandas as pd

# 创建示例数据
data = pd.Series(['a', 'b', 'c', 'd'])

# 定义转换规则
def convert(x):
    return x.upper()

# 使用 map 方法进行数据转换
converted_data = data.map(convert)

print("Original Data:")
print(data)
print("\nData After Conversion:")
print(converted_data)