from pymatgen.core.structure import Structure
import numpy as np

def is_within_rectangle(coords, atom1_coords, atom2_coords):
    """
    判断一个原子是否在两个目标原子连线形成的矩形范围内。
    """
    # 获取矩形的最小和最大x、y坐标
    min_x = min(atom1_coords[0], atom2_coords[0])
    max_x = max(atom1_coords[0], atom2_coords[0])
    min_y = min(atom1_coords[1], atom2_coords[1])
    max_y = max(atom1_coords[1], atom2_coords[1])

    # 判断该原子的坐标是否在这个矩形范围内
    return (min_x <= coords[0] <= max_x) and (min_y <= coords[1] <= max_y)

def get_atoms_in_rectangle(cif_file, atom_index1, atom_index2, min_pair_distance):
    # 读取cif文件并创建结构对象
    structure = Structure.from_file(cif_file)
    
    # 获取两个目标原子
    atom1 = structure[atom_index1]
    atom2 = structure[atom_index2]
    
    atom1_xy = np.array([atom1.coords[0], atom1.coords[1]])
    atom2_xy = np.array([atom2.coords[0], atom2.coords[1]])
    
    # 保存符合条件的原子编号和元素信息
    nearby_atoms = []
    
    # 遍历结构中的所有原子
    for i, site in enumerate(structure):
        if i == atom_index1 or i == atom_index2:
            continue  # 跳过目标原子本身
        
        site_xy = np.array([site.coords[0], site.coords[1]])
        
        # 判断该原子是否在两个目标原子形成的矩形范围内
        if is_within_rectangle(site_xy, atom1_xy, atom2_xy):
            nearby_atoms.append({
                "index": i,
                "element": site.species_string,
                "coords": site.coords  # 保存完整坐标
            })
    
    # 计算所有符合条件的原子两两之间的距离
    atom_pairs = []
    for i in range(len(nearby_atoms)):
        for j in range(i + 1, len(nearby_atoms)):
            atom1 = nearby_atoms[i]
            atom2 = nearby_atoms[j]
            
            # 计算两个原子之间的距离（全三维距离）
            distance = np.linalg.norm(np.array(atom1['coords']) - np.array(atom2['coords']))
            
            # 如果距离大于最小阈值，则保存配对信息
            if distance <= min_pair_distance:
                atom_pairs.append({
                    "pair_id": len(atom_pairs) + 1,
                    "atom1_index": atom1['index'],
                    "atom1_element": atom1['element'],
                    "atom2_index": atom2['index'],
                    "atom2_element": atom2['element'],
                    "distance": distance,
                    "atom1_coords": atom1['coords'],
                    "atom2_coords": atom2['coords']
                })
    
    return atom_pairs, structure

def increase_distance_and_save_cif(atom_pairs, structure, distance_increase_percent, output_file):
    # 按百分比增加两原子之间的距离
    for pair in atom_pairs:
        atom1_coords = np.array(pair['atom1_coords'])
        atom2_coords = np.array(pair['atom2_coords'])
        
        # 计算原来的距离向量
        displacement_vector = atom2_coords - atom1_coords
        
        # 计算需要增加的距离
        increase_factor = 1 + distance_increase_percent / 100.0
        
        # 调整atom2的坐标，使两原子之间的距离按百分比增加
        new_atom2_coords = atom1_coords + increase_factor * displacement_vector
        
        # 更新原子在结构中的坐标
        structure[pair['atom2_index']].coords = new_atom2_coords
    
    # 保存为新的cif文件
    structure.to(fmt="cif", filename=output_file)
    print(f"已保存新的cif文件至: {output_file}")

# 示例用法
cif_file = "example.cif"            # 替换为你的cif文件路径
atom_index1 = 0                     # 第一个目标原子编号
atom_index2 = 1                     # 第二个目标原子编号
min_pair_distance = 2.5             # 指定原子对之间的最小距离
distance_increase_percent = 10.0     # 增加距离的百分比
output_file = "new_structure.cif"    # 输出新的cif文件路径

# 获取符合条件的原子对和结构
atom_pairs, structure = get_atoms_in_rectangle(cif_file, atom_index1, atom_index2, min_pair_distance)

# 按百分比增加距离并保存新的cif文件
increase_distance_and_save_cif(atom_pairs, structure, distance_increase_percent, output_file)
