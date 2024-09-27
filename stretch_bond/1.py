from pymatgen.core.structure import Structure
import numpy as np

def get_atoms_within_xy_distance(cif_file, atom_index, max_distance, min_pair_distance):
    # 读取cif文件并创建结构对象
    structure = Structure.from_file(cif_file)
    
    # 获取指定的原子
    target_atom = structure[atom_index]
    
    # 提取目标原子的xy坐标
    target_xy = np.array([target_atom.coords[0], target_atom.coords[1]])
    
    # 保存符合条件的原子编号和元素信息
    nearby_atoms = []
    
    # 遍历结构中的所有原子
    for i, site in enumerate(structure):
        if i == atom_index:
            continue  # 跳过目标原子本身
        
        # 获取当前原子的xy坐标
        site_xy = np.array([site.coords[0], site.coords[1]])
        
        # 计算与目标原子的xy平面距离
        distance = np.linalg.norm(site_xy - target_xy)
        
        # 如果距离小于指定的阈值，则保存该原子的编号和元素信息
        if distance <= max_distance:
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
                    "pair_id": len(atom_pairs) + 1,  # 配对编号
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
cif_file = "6.cif"            # 替换为你的cif文件路径
atom_index = 79                      # 替换为指定的原子编号（从0开始）
max_distance = 4                  # 指定在xy平面内的最大距离
min_pair_distance = 2.5             # 指定原子对之间的最小距离
distance_increase_percent = 10.0     # 增加距离的百分比
output_file = "new_structure.cif"    # 输出新的cif文件路径

# 获取符合条件的原子对和结构
atom_pairs, structure = get_atoms_within_xy_distance(cif_file, atom_index, max_distance, min_pair_distance)

# 按百分比增加距离并保存新的cif文件
increase_distance_and_save_cif(atom_pairs, structure, distance_increase_percent, output_file)

