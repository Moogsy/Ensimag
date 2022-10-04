#!/usr/bin/python3

import sys

def main():
    _, fname, *_ = sys.argv

    with open(fname, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end='')


if __name__ == "__main__":
    main()
