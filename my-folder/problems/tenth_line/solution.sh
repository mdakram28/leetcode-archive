# Read from the file file.txt and output the tenth line to stdout.
words=$(head -n10 file.txt | wc -l)
if [ $words -ge 10 ]; then
    head -n10 file.txt | tail -n1
fi