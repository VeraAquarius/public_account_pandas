import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    'A': ['a', 'b', 'c', 'd'],
    'B': ['e', 'f', 'g', 'h']
})

# 使用 replace 方法结合字典进行数据替换
replace_dict = {'a': 'A', 'b': 'B', 'e': 'E', 'f': 'F'}
replaced_df_dict = df.replace(replace_dict)

# 使用 replace 方法不使用字典进行数据替换
replaced_df_no_dict = df.copy()
replaced_df_no_dict['A'] = replaced_df_no_dict['A'].replace('a', 'A')
replaced_df_no_dict['A'] = replaced_df_no_dict['A'].replace('b', 'B')
replaced_df_no_dict['B'] = replaced_df_no_dict['B'].replace('e', 'E')
replaced_df_no_dict['B'] = replaced_df_no_dict['B'].replace('f', 'F')

print("Original Data:")
print(df)
print("\nData After Replacement (Using Dictionary):")
print(replaced_df_dict)
print("\nData After Replacement (Not Using Dictionary):")
print(replaced_df_no_dict)