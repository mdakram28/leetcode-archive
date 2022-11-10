# Read from the file file.txt and print its transposed content to stdout.
cols=$(head -n1 file.txt | grep -o " " | wc -l)
cols=$((cols + 1))
# echo $cols

for r in $(seq 1 $cols); do
    # echo "ROW: " $r
    cat file.txt | awk -v r=$r '{printf $r " "}' | tr '\n' ' ' | xargs
done