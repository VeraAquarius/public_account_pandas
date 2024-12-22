import pandas as pd
import numpy as np

# 创建一个包含字符串和空值的Series
data = pd.Series(['apple', 'banana', np.nan, 'cherry', 'date'])

# 使用isnull方法检查空值
null_check = data.isnull()

# 显示空值检查结果
print("Null Check:", null_check)

# 使用str.contains方法检查Series中包含'a'的字符串
contains_a = data.str.contains('a')

# 显示包含'a'的检查结果
print("Contains 'a':", contains_a)