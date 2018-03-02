#!/usr/bin/python3
"""
@author Leon F.A. Wetzel
@email leonwetzel@gmail.com
"""
import sys


def main():
    """
    Processes text and counts word(s) per line,
    so the amount of occurences per word can be
    found.
    :return:
    """
    words = []

    for line in sys.stdin:
        new = process(line)
        words.append(new)

    words.sort()
    for item in set(words):
        print("{}\t{}".format(words.count(item),item))

def process(line):
    """
    Processes a line by removing (white)spaces
    and lowering case.
    """
    new = line.rstrip()
    #new = new.replace(" ","")
    new = new.lower()
    return new

if __name__ == "__main__":
    main()
