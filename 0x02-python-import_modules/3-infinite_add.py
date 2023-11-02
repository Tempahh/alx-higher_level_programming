#!/usr/bin/python3
import sys
import math
def infi_add():
    sum = 0
    for i in range(1, len(sys.argv)):
        sum = sum + int(sys.argv[i])
    print(sum)
if __name__ == "__main__":
    infi_add()