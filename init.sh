#!/bin/bash
monthday=${PWD##*/}
for example in `ls -d *`; do
	cd $example
	dirname=${PWD##*/}
	touch ${dirname}.txt
	echo "# ${dirname} 풀이" >> $dirname.txt
	echo "# 2022-${monthday:0:2}-${monthday:2:2}" >> $dirname.txt
	echo "import sys" >> $dirname.txt
	echo "sys.stdin = open('input.txt', 'r')" >> $dirname.txt
	echo "T = int(input())" >> $dirname.txt
	echo "for tc in range(1, T+1):" >> $dirname.txt
	echo "    print('#{} {}'.format(tc, ans))" >> $dirname.txt
	mv $dirname.txt $dirname.py
	cd ..
done
cd $monthday/
rm $monthday.py
rm init.sh
