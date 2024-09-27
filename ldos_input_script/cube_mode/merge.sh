#!/bin/bash
# 定义起始值、结束值和步长
start_i=0.189
end_i=20.79
step_i=3.78

start_j=0.189
end_j=34.4
step_j=5.67
# 使用while循环和bc进行浮点数循环
mkdir exc
current_i=$start_i
while (( $(echo "$current_i <= $end_i" | bc -l) )); do
  current_j=$start_j
  while (( $(echo "$current_j <= $end_j" | bc -l) )); do
    
    p="0.189,$current_j,$current_i"   #12a
    q="24.22,$current_j,$current_i"    #50a
    dir_name="${current_i}-${current_j}"
        
    # gaiming
    (cd "$dir_name" && cp LDOS.txt ../exc/$current_i-$current_j.txt )
    
    # 更新j值
    current_j=$(echo "$current_j + $step_j" | bc)
  done
  
  # 更新i值
  current_i=$(echo "$current_i + $step_i" | bc)
done

cd exc 

paste *.txt > ../a.txt