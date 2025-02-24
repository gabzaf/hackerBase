find . -type f -size +55c -size -98c -print0 | sort -z | xargs -0 cat | md5sum
