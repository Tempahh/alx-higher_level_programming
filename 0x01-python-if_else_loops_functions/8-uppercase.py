def uppercase(str):
    for alp in str:
        c = ord(alp)
        if (c >= ord('a')) and (c <= ord('z')):
            alp = chr(c - ord('a') + ord('A'))
        print("{}".format(alp), end='')
    print()