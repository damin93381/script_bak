import numpy as np
from ase.io import read

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
        
        segments.append((start, end))
    
    return segments

# 示例调用
cif_file = './1.cif'  # CIF文件路径
num_segments = 25  # 平行线段数量
segments = generate_parallel_segments(cif_file, num_segments)
atoms = read(cif_file)
cell = atoms.get_cell()
    
# 获取晶胞的三个晶轴
a, b, c = cell[0], cell[1], cell[2]

# 计算晶胞对角线的方向向量
diagonal_direction = a + b + c
# 输出每条线段的坐标
print(diagonal_direction)
print("Generated segments:")
for idx, (start, end) in enumerate(segments, 1):
    print(f"Segment {idx}: Start: {start}, End: {end}")





