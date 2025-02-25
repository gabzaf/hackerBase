find . -type f -size 55c -newermt "2023-07-18 10:11" -exec basename {} \; | sort | md5sum
