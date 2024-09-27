# 读取文件并处理，将每行处理后的数据求和作为第三列，保留源文件的前两列
def process_file_and_add_sum(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            columns = line.strip().split()  # 以空格分割每一列
            
            # 提取前两列
            first_two_columns = columns[:2]
            
            # 从第四列开始，保留每三列中的第三列
            filtered_columns = columns[3::3]
            
            # 对保留的列进行数值求和（假设都是数值类型）
            numeric_data = [float(value) for value in filtered_columns]  # 保留的数据列进行求和
            total_sum = sum(numeric_data)
            
            # 将前两列和总和形成新的行
            new_line = first_two_columns + [str(total_sum)]
            
            # 写入新的文件
            f_out.write(" ".join(new_line) + "\n")

    print(f"处理完成，结果保存在 {output_file}")

# 指定输入和输出文件
input_file = "c.txt"  # 替换为你的输入文件
output_file = "output.txt"  # 替换为你想保存的输出文件

# 调用函数处理文件
process_file_and_add_sum(input_file, output_file)


