#!/usr/bin/zsh

for file in *; do
    start=${file}
    stop=$(echo "${file}" | sed 's/ //g')

    if [[ $start != $stop ]]; then
        mv $start $stop
    fi
done
