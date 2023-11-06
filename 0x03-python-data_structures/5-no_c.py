#!/Users/mac/opt/anaconda3/bin/python3

def no_c(my_string):
    new_string = ""
    for alphas in my_string:
        if alphas != "C" and alphas != "c":
            new_string += alphas
    return new_string
