#!/bin/bash

min_size=4000
max_size=6000

find . -type f -size +$min_size"c" -size -$max_size"c" -printf "%f/n" | sort | while read filename; do

md5sum_result=$(echo "$filename" | md5sum)

md5_hash=$(echo "$md5sum_result" | awk '{print $1}')

echo "$filename: $md5_hash"
done
