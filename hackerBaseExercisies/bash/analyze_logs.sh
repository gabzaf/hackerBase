 find . -type f -printf "%T@ %T+ %f\n" | sort -n | while read -r ts date file; do 
    count=$(awk '{print $1}' "$file" | sort -u | wc -l); 
    echo -n "$date $file $count" | md5sum; 
done
