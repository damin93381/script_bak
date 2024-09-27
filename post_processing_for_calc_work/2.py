import os

def delete_files_with_string_in_name(directory, target_string):
    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件名是否包含特定字符串
        if target_string in filename:
            file_path = os.path.join(directory, filename)
            # 确保只处理文件
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")

# 示例用法
directory = '/path/to/directory'
target_string = 'delete_this_string'
delete_files_with_string_in_name(directory, target_string)