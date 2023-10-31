#!/usr/bin/python3
for a in range(0, 26):
    d = ord('z') - a
    if a % 2 == 1:
        d = chr(d - ord('a') + ord('A'))
    else:
        d = chr(d)
    print("{}".format(d), end='')
