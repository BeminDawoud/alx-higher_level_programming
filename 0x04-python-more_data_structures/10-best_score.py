#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = 0
        key = ""
        for k, v in a_dictionary.items():
            if v > best:
                best = v
                key = k
        return key
    return None
