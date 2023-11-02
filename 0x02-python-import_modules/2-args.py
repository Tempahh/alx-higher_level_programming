#!/Users/mac/opt/anaconda3/bin/python
import sys

def print_arg():
    print("{} arguments" .format(len(sys.argv) - 1))

    if len(sys.argv) <= 1:
    
        print(".")

    else:
        for i in range(1, len(sys.argv)):
            print("{}: {}" .format(i, sys.argv[i]))

if __name__ == "__main__":
    print_arg()
