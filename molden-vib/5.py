import os

# 定义文件路径
input_file = 'diag.inp'
vibration_folder = 'output_files'
output_folder = 'diag'

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 读取输入文件内容
with open(input_file, 'r') as file:
    input_lines = file.readlines()

# 提取 &COORD 和 &END COORD 之间的部分
start_idx = end_idx = None
for i, line in enumerate(input_lines):
    if '&COORD' in line:
        start_idx = i + 1
    elif '&END COORD' in line:
        end_idx = i
        break

# 遍历振动文件夹中的所有文件
for vibration_file in os.listdir(vibration_folder):
    if vibration_file.startswith('vibration_') and vibration_file.endswith('.txt'):
        vibration_path = os.path.join(vibration_folder, vibration_file)
        
        # 读取振动文件内容
        with open(vibration_path, 'r') as file:
            vibration_lines = file.readlines()
        
        # 替换 5.py 文件中 &COORD 和 &END COORD 之间的部分
        new_input_lines = input_lines[:start_idx] + vibration_lines + input_lines[end_idx:]
        
        # 将结果写入新的文件
        output_file = os.path.join(output_folder, vibration_file.replace('.txt', '.inp'))
        with open(output_file, 'w') as file:
            file.writelines(new_input_lines)

print('所有文件已处理并保存到指定文件夹中')