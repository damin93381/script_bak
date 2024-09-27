import os

def remove_lines_with_string(file_path, target_string):
    # 创建一个临时文件
    temp_file_path = file_path + '.tmp'
    
    with open(file_path, 'r') as read_file, open(temp_file_path, 'w') as write_file:
        for line in read_file:
            if target_string not in line:
                write_file.write(line)
    
    # 替换原文件
    os.replace(temp_file_path, file_path)

# 示例用法
file_path = 'example.txt'
target_string = 'delete this string'
remove_lines_with_string(file_path, target_string)