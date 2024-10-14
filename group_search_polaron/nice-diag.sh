interval1=30
num=4
for diagfile in ./diag/vib*; do
    i=$(echo "$diagfile" | sed 's/[^0-9]*//g') 
    mkdir $i/diag
    cp "$diagfile" "$i/diag/"
    cd $i
    cp cp2k-DM.sh diag/
    cp 777-RESTART.wfn diag/freq-RESTART.wfn
    cd diag
	j=$(ls | grep vib)
    sbatch cp2k-DM.sh $j
	cd ../../
    squeue > lalala.txt
    mc=$(grep -c "cp2k-DM." "lalala.txt")
    until [ "$mc" -lt "$num" ]; do
        squeue > lalala.txt
        mc=$(grep -c "cp2k-DM." "lalala.txt")
        sleep $interval1                                    
    done 
done
rm lalala.txt