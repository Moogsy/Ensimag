#! /usr/bin/zsh

if [[ ${1} -le ${2} ]]
then
    echo "${1} is less than ${2}"
else
    echo "${1} is bigger than ${2}"
fi
