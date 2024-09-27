import numpy as np
from ase.io import read
from ase.geometry import cellpar_to_cell

def generate_parallel_segments(cif_file, num_segments):
    # 读取CIF文件并获取晶胞信息
    atoms = read(cif_file)
    cell = atoms.get_cell()
    
    # 获取晶胞的角点坐标，分别为原点和对角点
    origin = np.array([0.0, 0.0, 0.0])
    diag = np.sum(cell, axis=0)  # 对角点
    
    # 生成一条从原点到对角点的线段
    central_segment = (origin, diag)
    print(f"Central segment from {origin} to {diag}")
    
    # 根据要求生成平行线段
    segments = []
    
    # 每一条线段都平行于中心线段，从晶胞内均匀取 num_segments 条
    for i in range(1, num_segments + 1):
        fraction = i / (num_segments + 1)
        translation_vector = fraction * diag  # 平移的向量
        
        segment_start = origin + translation_vector
        segment_end = diag + translation_vector
        
        segments.append((segment_start, segment_end))
    
    return central_segment, segments

# 示例调用
cif_file = './1.cif'  # CIF文件路径
num_segments = 5  # 平行线段数量
central_segment, segments = generate_parallel_segments(cif_file, num_segments)

# 输出每条线段的坐标
print("Central segment coordinates:")
print(f"Start: {central_segment[0]}, End: {central_segment[1]}")
print("\nGenerated parallel segments:")
for idx, (start, end) in enumerate(segments, 1):
    print(f"Segment {idx}: Start: {start}, End: {end}")


