for file in *.dot
do 
dot -Tpng "$file" > "${file%.dot}.png"
echo "$file"
done
