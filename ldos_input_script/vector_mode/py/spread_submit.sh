#!/bin/bash

# 获取所有 output_num.txt 文件
cd output/
files=$(ls output_*.txt)

# 遍历每个文件
for file in $files; do
  # 提取文件名中的编号
  num=$(echo $file | grep -oP '(?<=output_)\d+(?=\.txt)')
  
  # 检查是否存在对应编号的文件夹，如果不存在则创建
  dir="ldos_$num"
  if [ ! -d "$dir" ]; then
    mkdir "../$dir"
  fi
  
  # 将文件移动到对应的文件夹中
  cp "$file" "../$dir/ldos.in"
  cp ../mfn-DM.sh "../$dir/"
  cd ../$dir/
  sbatch mfn-DM.sh
  cd ../output/
done