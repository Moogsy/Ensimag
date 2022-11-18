#!/usr/bin/zsh

if [[ ! -d "ALL" ]]; then
    mkdir ALL
fi

for d in dir*; do
    for f in ${d}/*; do
        mv $f "ALL/${d}_$(basename $f)"
    done
    rmdir $d
done


