find . -type f -size -57c -exec cat {} + | sort | md5sum
