# 定义输入和输出文件名
input_file = 'freq-VIBRATIONS-1.molden'
output_file = 'extracted_atom_coordinates.txt'

# 打开输入文件并读取内容
with open(input_file, 'r') as file:
    lines = file.readlines()

# 初始化标志和结果列表
atom_section = False
atom_coordinates = []

# 遍历文件内容
for line in lines:
    # 检查是否进入 [Atoms] AU 部分
    if '[Atoms] AU' in line:
        atom_section = True
        continue
    
    # 如果在 [Atoms] AU 部分，提取原子坐标信息
    if atom_section:
        if line.strip() == '':
            break
        atom_coordinates.append(line.strip())

# 将提取的原子坐标信息写入新的文件
with open(output_file, 'w') as file:
    for coord in atom_coordinates:
        file.write(coord + '\n')

print(f'原子坐标信息已提取到 {output_file}')