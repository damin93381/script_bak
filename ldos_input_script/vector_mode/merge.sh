#!/bin/bash

# 创建exc目录
mkdir -p exc

# 遍历ldos_$num目录后的数字编号
for dir in ldos_*; do
  if [ -d "$dir" ]; then
    # 提取目录中的数字编号
    num=$(echo "$dir" | sed 's/ldos_//')
    
    # 在目录中执行命令，将LDOS.txt文件复制到exc目录
    (cd "$dir" && cp LDOS.txt ../exc/$num.txt)
  fi
done

# 进入exc目录
cd exc

# 将所有txt文件合并成一个文件a.txt
paste *.txt > ../a.txt