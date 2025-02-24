find . -type f -newermt "2023-07-23 10:56" ! -newermt "2023-07-23 10:56" -exec grep -l '^<%GIF' {} + | xargs cat | sort | md5sum
