import numpy as np
from ase.io import read
import os

def generate_parallel_segments(cif_file, num_segments):
    # 读取CIF文件并获取晶胞信息
    atoms = read(cif_file)
    cell = atoms.get_cell()
    
    # 获取晶胞的三个晶轴
    a, b, c = cell[0], cell[1], cell[2]

    # 计算晶胞对角线的方向向量
    diagonal_direction = a + b + c

    # 生成线段的起点和终点
    segments = []
    
    # 在对角线方向上均匀选择点
    for i in range(num_segments):
        # 计算比例
        fraction = (i + 1) / (num_segments + 1)

        # 生成线段的起点和终点，确保两端在对角线上
        start = fraction * diagonal_direction
        end = (1 - fraction) * diagonal_direction
        
        # 将坐标转换为数组格式
        start_str = ','.join(map(str, start))
        end_str = ','.join(map(str, end))
        
        segments.append((start_str, end_str))
    
    return segments

def replace_lines_in_files(input_file, output_file_prefix, segments):
    # 创建以 output_file_prefix 命名的文件夹
    if not os.path.exists(output_file_prefix):
        os.makedirs(output_file_prefix)
    
    # 读取指定文件的内容
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # 对每个线段生成一个新的文件
    for idx, (start, end) in enumerate(segments, 1):
        # 替换第7和第8行的内容
        lines[6] = f"{start}\n"
        lines[7] = f"{end}\n"
        
        # 生成新的文件名
        output_file = os.path.join(output_file_prefix, f"{output_file_prefix}_{idx}.txt")
        
        # 将修改后的内容写入新的文件
        with open(output_file, 'w') as file:
            file.writelines(lines)

# 示例调用
cif_file = './1.cif'  # CIF文件路径
num_segments = 32  # 平行线段数量
segments = generate_parallel_segments(cif_file, num_segments)

input_file = './ldos.in'  # 输入文件路径
output_file_prefix = 'output'  # 输出文件前缀

replace_lines_in_files(input_file, output_file_prefix, segments)