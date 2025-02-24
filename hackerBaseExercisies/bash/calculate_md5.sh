find . -type f -size -97c -exec basename {} \; | sort | md5sum
