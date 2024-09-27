import pandas as pd

# 读取CIF文件
cif_file_path = "./polaron-3.cif"
# 读取文件内容
with open(cif_file_path, "r") as file:
    cif_content = file.readlines()

# 提取所有包含原子位置信息的行
atom_lines = [line for line in cif_content if line.strip() and not line.startswith('_') and not line.startswith('loop_') and not line.startswith('#') and not line.startswith('data_')]

# 提取氮原子行的位置
def extract_atom_indices(cif_lines, atom_symbol):
    atom_indices = []
    for i, line in enumerate(cif_lines):
        if atom_symbol in line.split():
            atom_indices.append(i)
    return atom_indices

# 提取氮原子编号
cu_indices = extract_atom_indices(atom_lines, "Cl")
n_indices = extract_atom_indices(atom_lines, "Co")
c_indices = extract_atom_indices(atom_lines, "C")
o_indices = extract_atom_indices(atom_lines, "O")
cl_indices = extract_atom_indices(atom_lines, "Cl")

# 生成逗号分隔的字符串
cu_indices_str = ','.join(map(str, cu_indices))
n_indices_str = ','.join(map(str, n_indices))
c_indices_str = ','.join(map(str, c_indices))
o_indices_str = ','.join(map(str, o_indices))
cl_indices_str = ','.join(map(str, cl_indices))

print(n_indices_str)
print(cu_indices_str)
print(cl_indices_str)
print(o_indices_str)
print(c_indices_str)

