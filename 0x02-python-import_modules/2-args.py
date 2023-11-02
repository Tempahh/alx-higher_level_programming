#!/usr/bin/python3
import sys

def print_arg():
    
    if len(sys.argv) - 1 == 1:
        print("{} argument" .format(len(sys.argv) - 1))

    elif len(sys.argv) <= 1:
    
        print("{} arguments." .format(len(sys.argv) - 1))
    else:
        print("{} arguments." .format(len(sys.argv) - 1))

    for i in range(1, len(sys.argv)):
        print("{}: {}" .format(i, sys.argv[i]))

if __name__ == "__main__":
    print_arg()
