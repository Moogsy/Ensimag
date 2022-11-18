#!/usr/bin/zsh

for num in $(seq ${1}); do
    wget http://xkcd.com/${num} -O - | grep hotlink | grep -o 'http.*jpg' | tr ">" "\n" | head -n 1 >> links.txt
done
