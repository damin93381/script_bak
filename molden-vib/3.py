# 定义输入文件名
input_file = 'extracted_norm_freq.txt'

# 打开输入文件并读取内容
with open(input_file, 'r') as file:
    lines = file.readlines()

# 初始化字典来存储不同振动模式的数据
vibration_data = {}
current_vibration = None

# 遍历文件内容
for line in lines:
    line = line.strip()
    if line.startswith('vibration'):
        current_vibration = line.split()[1]
        vibration_data[current_vibration] = []
    elif current_vibration:
        vibration_data[current_vibration].append(line)

# 将不同振动模式的数据分别写入不同的文件
for vibration, data in vibration_data.items():
    output_file = f'vibration_{vibration}.txt'
    with open(output_file, 'w') as file:
        for line in data:
            file.write(line + '\n')

print('振动模式数据已分别提取到不同文件中')