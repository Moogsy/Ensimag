#! /usr/bin/zsh
echo "$(last | head -n -2 | awk '{print $1}' | sort | uniq -c | sort -k 1 -n)"
