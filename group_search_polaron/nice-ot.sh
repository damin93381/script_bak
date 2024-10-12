interval1=30
num=4
for otfile in ./ot/vib*; do
    i=$(echo "$otfile" | sed 's/[^0-9]*//g') 
    mkdir $i
    cp cp2k-DM.sh freq-RESTART.wfn $otfile $i/
	j=$(ls $i/ | grep vib)
	cd $i
    sbatch cp2k-DM.sh $j
	cd ..
    squeue > lalala.txt
    mc=$(grep -c "cp2k-DM." "lalala.txt")
    until [ "$mc" -lt "$num" ]; do
        squeue > lalala.txt
        mc=$(grep -c "cp2k-DM." "lalala.txt")
        sleep $interval1                                    
    done 
done