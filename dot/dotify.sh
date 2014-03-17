
for dir in *;
do 
	for file in *.dot
	do 
	dot -Tpng "$file" > "${file%.dot}.png"
	echo "$file, $dir"
	done
done