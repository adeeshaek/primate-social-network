
for dir in *;
do 
	for file in *.dot
	do 
	dot -Tpng "$dir/$file" > "$dir/${file%.dot}.png"
	echo "$dir/$file"
	done
done
