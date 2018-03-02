#!/usr/bin/python3
"""
@author Leon F.A. Wetzel
@email leonwetzel@gmail.com
"""

import sys

def main():
    """
    Program which splits strings by commas
    and prints values to standard output.
    """
    for line in sys.stdin:
        # split string
        try:
            delimiter = determine_delimiter(sys.argv[1])
            sentence = [x.strip() for x in line.split(delimiter)]
            # print word per split
            for word in sentence:
                print(word)
        except ValueError:
            sys.write.stderr("Argument invalid or missing!\nPlease enter the command as follows: 'cat YOUR_INPUT.in | python stripper.py -s' OR 'cat YOUR_INPUT.in | python stripper.py -c'")
            sys.exit()

def determine_delimiter(choice):
    """
    Assign delimiter based on user input
    from command line.
    :param: Command line argument indicating
            "-c" (comma as delimiter) or
            "-s" (space as delimiter).
    """
    if choice == "-c":
        delimiter = ','
    elif choice == "-s":
        delimiter = " "
    else:
        delimiter = ","
    return delimiter


if __name__ == "__main__":
    main()
