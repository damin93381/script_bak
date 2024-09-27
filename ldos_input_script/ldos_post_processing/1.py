# 读取文件并处理
def process_file(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            columns = line.strip().split()  # 以空格分割每一列
            filtered_columns = columns[2::3]  # 保留每3列中的第3列
            f_out.write(" ".join(filtered_columns) + "\n")  # 写入新的文件

# 指定输入和输出文件
input_file = "diag.txt"  # 替换为你的输入文件
output_file = "diagmerge.txt"  # 替换为你想保存的输出文件

# 调用函数处理文件
process_file(input_file, output_file)

print(f"处理完成，结果保存在 {output_file}")
