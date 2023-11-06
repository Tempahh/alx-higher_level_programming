#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) < 0:
        return None
    else:
        tuple_result = sentence[0]
        return (len(sentence), tuple_result)
        