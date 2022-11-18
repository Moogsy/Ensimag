#! /usr/bin/zsh

for f in ALL/*; do
    mod_date=$(ls -l $f | awk '{print $6, $7, $8}')
    echo "${mod_date}" >> $f
done
