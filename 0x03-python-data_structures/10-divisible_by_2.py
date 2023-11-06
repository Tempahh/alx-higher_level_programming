#!/Users/mac/opt/anaconda3/bin/python3

def divisible_by_2(my_list=[]):
    div_by_2 = []
    for nums in range(len(my_list)):
        if my_list[nums] % 2 == 0:
            div_by_2.append(True)
        else:
            div_by_2.append(False)

    return (div_by_2)