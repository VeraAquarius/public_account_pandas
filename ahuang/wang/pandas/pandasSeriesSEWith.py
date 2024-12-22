import pandas as pd

# 创建一个包含文件名的Series
filenames = pd.Series([
    "image1.jpg",
    "image2.png",
    "document1.pdf",
    "script1.py",
    "archive1.tar.gz"
])

# 使用str.endswith检查以'.jpg'结尾的文件名
jpg_files = filenames.str.endswith('.jpg')

# 显示结果
print("Files ending with '.jpg':", jpg_files)

# 使用str.startswith检查以'script'开头的文件名
script_files = filenames.str.startswith('script')

# 显示结果
print("Files starting with 'script':", script_files)