import os

# 定义文件路径
atom_coordinates_file = 'extracted_atom_coordinates.txt'
vibration_folder = './temp/'
output_folder = 'output_files'
multiplier = 0.5292
# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 读取原子坐标文件内容
with open(atom_coordinates_file, 'r') as file:
    atom_lines = file.readlines()

# 遍历振动文件夹中的所有文件
for vibration_file in os.listdir(vibration_folder):
    if vibration_file.startswith('vibration_') and vibration_file.endswith('.txt'):
        vibration_path = os.path.join(vibration_folder, vibration_file)
        
        # 读取振动文件内容
        with open(vibration_path, 'r') as file:
            vibration_lines = file.readlines()
        
        # 初始化结果列表
        result_lines = []
        
        # 遍历每一行，进行对应列的相加
        for atom_line, vibration_line in zip(atom_lines, vibration_lines):
            atom_data = list(map(float, atom_line.split()[3:6]))
            vibration_data = list(map(float, vibration_line.split()[0:3]))
            result_data = [(a + v*2) * multiplier for a, v in zip(atom_data, vibration_data)]
            result_line = f"{atom_line.split()[0]} {' '.join(map(str, result_data))}\n"
            result_lines.append(result_line)
        
        # 将结果写入新的文件
        output_file = os.path.join(output_folder, vibration_file)
        with open(output_file, 'w') as file:
            file.writelines(result_lines)

print('所有文件已处理并保存到指定文件夹中')