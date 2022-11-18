#! /usr/bin/zsh

for arg in $@; do

    if [[ -d ${arg} ]]; then
        for entry in ${arg}/*; do
            if [[ -d ${entry} ]]; then
                echo ${entry}
            fi
        done
    else
        echo "${arg} is not a directory"
    fi
done
