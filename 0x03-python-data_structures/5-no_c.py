#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        my_string = [x for x in my_string if x.lower() != 'c']
        my_string = ''.join(my_string)
    return (my_string)
